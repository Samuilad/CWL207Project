import matplotlib.pyplot as plt

from imdb import IMDb

from Data_Sorting import Actor


def find_movies_played_by_actor(movie_ids):
    """
    :param movie_ids:
    :return: a dictionary that holds actor names as keys and the movies they appear in as values
    """
    ia = IMDb()
    actors = {}
    for ids in movie_ids:
        for actor in ia.get_movie(ids)['cast']:
            if not (actor['name'] in actors.keys()):
                actors[actor['name']] = Actor(actor['name'])
                actors[actor['name']].movie_Ids.append(ids)
            else:
                actors[actor['name']].movie_Ids.append(ids)
    return actors


class Graphs:

    def __init__(self, movie_ids):
        self.actors_in_movies = find_movies_played_by_actor(movie_ids)

    def plot_average_actor_adjusted_gross_graph(self):
        """
        Graphs the average adjusted gross per actor based on the movies they are in
        :return: Bar graph of average adjusted gross amount as x-axis and actor / actress as y-axis
        """

        actors = []

        average_earning = []

        left = []

        for actor in self.actors_in_movies.keys():
            i = 1
            if len(self.actors_in_movies[actor].movie_Ids) >= 6:
                left.append((i * .5) + 1)
                i += 1
                self.actors_in_movies[actor].calculate_average_adjusted_gross()
                actors.append(str(self.actors_in_movies[actor].name))
                average_earning.append(self.actors_in_movies[actor].average_money_made)

        plt.barh(actors, average_earning)

        plt.xlabel('Adjusted Gross in Rs (Billion(s))')

        plt.ylabel('Actor / Actress')

        plt.title('Average Adjusted Gross per Actor / Actress')

        plt.tight_layout()

        plt.show()

    def plot_average_actor_rating_by_movie(self):
        """
        Graphs the average rating per actor based on the movies they are in
        :return: Bar graph of average rating as x-axis and actor / actress as y-axis
        """

        actors = []

        average_rating = []

        left = []

        for actor in self.actors_in_movies.keys():
            i = 1
            if len(self.actors_in_movies[actor].movie_Ids) >= 6:
                left.append((i * .5) + 1)
                i += 1
                self.actors_in_movies[actor].calculate_average_rating()
                actors.append(str(self.actors_in_movies[actor].name))
                average_rating.append(self.actors_in_movies[actor].average_rating_by_movie)

        plt.barh(actors, average_rating)

        plt.xlabel('Average Rating Out of 10')

        plt.ylabel('Actor / Actress')

        plt.title('Average Rating Per Actor / Actress')

        plt.tight_layout()

        plt.show()


