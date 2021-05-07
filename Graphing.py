import matplotlib.pyplot as plt

from imdb import IMDb

from Data_Sorting import Actor


class Graphs:

    def __init__(self, movie_ids):
        self.actors_in_movies = self.find_movies_played_by_actor(movie_ids)

    def plot_average_actor_adjusted_gross_graph(self):

        actors = []

        average_earning = []

        left = []

        for actor in self.actors_in_movies.keys():
            i = 1
            if len(self.actors_in_movies[actor].movie_Ids) >= 6:
                left.append((i * .5) + 1)
                i += 1
                self.actors_in_movies[actor].calculate_average_movie_rating()
                actors.append(str(self.actors_in_movies[actor].name))
                average_earning.append(self.actors_in_movies[actor].average_money_made)
                print("{} 's movies made {} on average!".format(self.actors_in_movies[actor].name,
                                                                self.actors_in_movies[actor].average_money_made))

            plt.barh(actors, average_earning)

            plt.xlabel('Adjusted Gross in Rs (Billion(s))')

            plt.ylabel('Actor / Actress')

            plt.title('Average Adjusted Gross per Actor / Actress')

            plt.tight_layout()

            plt.show()

    def find_movies_played_by_actor(self, movie_ids):
        """
        parameter: movie object list
        returns a dictionary that holds actor names as keys and the movies they appear in as values
        """
        ia = IMDb()
        actors = {}
        for ids in movie_ids:
            for actor in ia.get_movie(ids)['cast']:
                if not (actor['name'] in actors.keys()):
                    actors[actor['name']] = Actor(actor)
                    actors[actor['name']].movie_Ids.append(ids)
                else:
                    actors[actor['name']].movie_Ids.append(ids)
        return actors
