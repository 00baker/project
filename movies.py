import webbrowser
class Movie():
	""" This is movie website """
	def __init__(self, movie_title, movie_storyline, poster_image, trailer):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_url = trailer

	def show(self):
		webbrowser.open(self.trailer_url)
