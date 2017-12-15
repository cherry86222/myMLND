import fresh_tomatoes
import media

Thor = media.Movie("Thor",
	"A marvel story of thor",
	"https://fsmedia.imgix.net/99/13/42/3b/5ccf/4e04/aa4d/7b21323cd5f0/chris-hemsworth-as-thor.jpeg",
	"https://www.youtube.com/watch?v=ue80QwXMRHg")

#print(toy_story.storyline)

panda = media.Movie("Kung Fu Panda",
	"A panda 's funny story",
	"http://www.gstatic.com/tv/thumb/movieposters/175618/p175618_p_v8_ad.jpg",
	"https://www.youtube.com/watch?v=C1bRkCenm20")
#print(avatar.storyline)

#avatar.show_trailer()

sunrise = media.Movie("Love before sunrise",
	"A story about love during the trip",
	"http://i.imgur.com/tocI1Ep.jpg",
	"https://www.youtube.com/watch?v=25v7N34d5HE")



movies = [Thor,panda,sunrise]
fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.__doc__)
#print(media.Movie.__name__)
#print(media.Movie.__module__)