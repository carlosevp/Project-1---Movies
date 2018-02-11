import webbrowser

class Movie():
    """ Provide movie related info """			# Docstring for the class Movie.
	# Defines a global variable with the ratings. Following PEP8 recommendation - all capital letters.
    VALID_RATINGS = ["G","PG","PG-13","R"]
	# Defines init, with all the required arguments
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube): 
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Defines the show_trailer function, which will open the youtube trailer defined on the Movie object.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

