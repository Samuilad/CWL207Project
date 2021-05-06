from imdb import IMDb


class Actor:
    money_made = 0
    movie_Ids = []

    def __init__(self, name):
        self.name = name


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
print(movie['box office'].keys())
budget = movie['box office']['Cumulative Worldwide Gross'].split()

money = budget[0][1:-1]

movieIDsSmall = ['0238936']


def find_movies_played_by_actor(movie_ids):
    """
    parameter: movie object list
    returns a dictionary that holds actor names as keys and the movies they appear in as values
    """
    actors = {}
    for id in movie_ids:
        for actor in ia.get_movie(id)['cast']:
            if not (actor in actors.keys()):
                actors[actor['name']] = Actor(actor)
                actors[actor['name']].movie_Ids.append(id)
            else:
                actors[actor['name']].movie_Ids.append(id)
    return actors


def calculate_average_movie_grossing_per_actor(actors):
    relevant_actors = []
    for actor in actors.keys():
        if len(actors[actor].movie_Ids) >= 5:
            print(actor)

            for id in actors[actor].movie_Ids:
                if 'Cumulative Worldwide Gross' in ia.get_movie(id)['box office'].keys():
                    gross_data = ia.get_movie(id)['box office']['Cumulative Worldwide Gross'].split()
                    actors[actor].money_made += int(gross_data[0][1:-1].replace(',',''))

            actors[actor].money_made = actors[actor].money_made / len(actors[actor].movie_Ids)
            print(actors[actor].money_made)
            relevant_actors.append(actors[actor])

    return relevant_actors


actors_in_movies = find_movies_played_by_actor(movieIDsSmall)
print(ia.get_movie(actors_in_movies["Shah Rukh Khan"].movie_Ids[9])['box office'].keys())

#calculate_average_movie_grossing_per_actor(actors_in_movies)
