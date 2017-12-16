import fresh_tomatoes
import media

"""This is to define three instances from class Movie in file media. It passes the 
defined parameter in to the class and initiate the instances"""
Thor = media.Movie("Thor", 
    "A marvel story of thor", 
    "https://fsmedia.imgix.net/99/13/42/3b/5ccf/4e04/aa4d/7b21323cd5f0/chris-hemsworth-as-thor.jpeg", 
    "https://www.youtube.com/watch?v=ue80QwXMRHg")


panda = media.Movie("Kung Fu Panda",
	"A panda 's funny story",
	"http://www.gstatic.com/tv/thumb/movieposters/175618/p175618_p_v8_ad.jpg",
	"https://www.youtube.com/watch?v=C1bRkCenm20")


sunrise = media.Movie("Love before sunrise",
	"A story about love during the trip",
	"http://i.imgur.com/tocI1Ep.jpg",
	"https://www.youtube.com/watch?v=25v7N34d5HE")

"""This is to define the list of movies to store three instances of Movie class"""
movies = [Thor, panda, sunrise]

"""This is to open the movie page from the method open_movies_page in fresh_tomatoes
and pass the parameter of list movies containing three instances"""
fresh_tomatoes.open_movies_page(movies)