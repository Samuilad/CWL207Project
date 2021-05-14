from imdb import IMDb


class Actor:

    def __init__(self, name):
        self.name = str(name)
        self.average_money_made = 0
        self.movie_Ids = []
        self.average_rating_by_movie = 0

    def calculate_average_adjusted_gross(self):
        """
        :return: average adjusted gross amount based off of the movies they appear in
        """
        money_made = 0
        for ids in self.movie_Ids:
            if ids in movie_ids_and_money.keys():
                money_made += movie_ids_and_money[ids]
        self.average_money_made = money_made / len(self.movie_Ids)

    def calculate_average_rating(self):
        """
        :return: average rating for actor based off the movie ratings they appear in
        """
        ia = IMDb()
        rating_sum = 0
        for ids in self.movie_Ids:
            rating_sum += ia.get_movie(ids)['rating']
        self.average_rating_by_movie = rating_sum / len(self.movie_Ids)


movie_ids_and_money = {'0284137': 2865500000, '1187043': 2695000000, '0248126': 1727000000, '1166100': 1705000000,
                       '0441048': 1467800000, '0234000': 1387600000, '1024943': 1332100000,
                       '0254481': 1300900000, '1182937': 1287000000, '0456144': 1274000000, '0213890': 1247800000,
                       '0238936': 1224100000, '0488798': 1121000000, '0871510': 1181400000,
                       '0169102': 1054800000, '0807758': 1034000000, '1146325': 1033700000, '0420332': 1009200000,
                       '0439662': 1000800000, '1017456': 970900000, '0451833': 952200000,
                       '0461936': 941400000, '0405508': 936900000, '0986264': 935800000, '0449994': 932500000,
                       '1275863': 910100000, '0473367': 907500000, '0248185': 890000000,
                       '1252596': 847000000, '0995031': 840500000, '0347473': 837500000, '0449999': 828800000,
                       '1084972': 828200000, '0806088': 820900000, '0300028': 812500000,
                       '0307873': 798600000, '0419058': 797500000, '0448206': 775200000, '1092005': 768400000,
                       '0151150': 766200000, '0418362': 762500000, '0499375': 746100000,
                       '0805184': 744600000, '0422091': 742000000, '0250690': 741400000, '0294662': 729000000,
                       '1185420': 724700000}