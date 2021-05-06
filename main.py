from imdb import IMDb

ia = IMDb()
# 47 movie Ids
movieIDs = ['0284137', '1187043', '0248126', '1166100', '0441048', '0234000', '1024943',
            '0254481', '1182937', '0456144', '0213890', '0238936', '0488798', '0871510',
            '0169102', '0807758', '1146325', '0420332', '0439662', '1017456', '0451833',
            '0461936', '0405508', '0986264', '0449994', '1275863', '0473367', '0248185',
            '1252596', '0995031', '0347473', '0449999', '1084972', '0806088', '0300028',
            '0307873', '0419058', '0448206', '1092005', '0151150', '0418362', '0499375',
            '0805184', '0422091', '0250690', '0294662', '1185420']

movie = ia.get_movie('1187043')

budget = movie['box office']['Cumulative Worldwide Gross'].split()

print(budget[0][1:-1])

movieIDsSmall = ['0284137', '1187043', '0248126', '1166100', '0441048', '0234000', '1024943']


def get_movies_list(movie_ids):
    """
    takes in movie Ids
    returns a list of movie objects
    """
    movies = []
    for id in movie_ids:
        movies.append(ia.get_movie(id))
    return movies


def sort_characters_to_movies(movies):
    """
    parameter: movie object list
    returns a dictionary that holds actor names as keys and the movies they appear in as values
    """
    actors = {}
    for movie in movies:
        for actor in movie['cast']:
            if not (actor in actors.keys()):
                titles = [movie]
                actors[actor] = titles
            else:
                actors[actor].append(movie)
    return actors


actors_in_movies = sort_characters_to_movies(get_movies_list(movieIDs))

for key in actors_in_movies.keys():
    if len(actors_in_movies[key]) >= 5:
        print(len(actors_in_movies[key]))
