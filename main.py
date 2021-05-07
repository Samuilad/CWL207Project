from imdb import IMDb

import matplotlib.pyplot as plt

from Data_Sorting import find_movies_played_by_actor

ia = IMDb()

# 47 movie Ids

movieIDs = ['0284137', '1187043', '0248126', '1166100', '0441048', '0234000', '1024943',
            '0254481', '1182937', '0456144', '0213890', '0238936', '0488798', '0871510',
            '0169102', '0807758', '1146325', '0420332', '0439662', '1017456', '0451833',
            '0461936', '0405508', '0986264', '0449994', '1275863', '0473367', '0248185',
            '1252596', '0995031', '0347473', '0449999', '1084972', '0806088', '0300028',
            '0307873', '0419058', '0448206', '1092005', '0151150', '0418362', '0499375',
            '0805184', '0422091', '0250690', '0294662', '1185420']


movieIDsSmall = ['0284137', '1187043', '0248126', '1166100', '0441048']



# x axis values
actors = []
# corresponding y axis values
average_earning = []

# x-coordinates of left sides of bars
left = []

actors_in_movies = find_movies_played_by_actor(movieIDs)

for actor in actors_in_movies.keys():
    i = 1
    if len(actors_in_movies[actor].movie_Ids) >= 6:
        left.append((i * .5) + 1)
        i += 1
        actors_in_movies[actor].calculate_average_movie_rating()
        actors.append(str(actors_in_movies[actor].name))
        average_earning.append(actors_in_movies[actor].average_money_made)
        print("{} 's movies made {} on average!".format(actors_in_movies[actor].name,actors_in_movies[actor].average_money_made))

# plotting a bar chart
plt.barh(actors, average_earning)

# naming the x-axis
plt.xlabel('Adjusted Gross in Rs (Billion(s))')
# naming the y-axis
plt.ylabel('Actor / Actress')
# plot title
plt.title('Average Adjusted Gross per Actor / Actress')

plt.tight_layout()

# function to show the plot
plt.show()