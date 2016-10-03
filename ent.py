import fresh
import movies

toy_story = movies.Movie("Toy Story",
	"Story",
	"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
	"https://www.youtube.com/watch?v=KYz2wyBy3kc"
	)
avatar = movies.Movie("Avatar",
	"aliens",
	"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
	"https://www.youtube.com/watch?v=5PSNL1qE6VY"
	)
hangover = movies.Movie("Hangover",
	"Enjoyment",
	"https://upload.wikimedia.org/wikipedia/en/b/b9/Hangoverposter09.jpg",
	"https://www.youtube.com/watch?v=tcdUhdOlz9M"
	)
home_alone = movies.Movie("Home Alone",
	"Kid alone in the home",
	"https://upload.wikimedia.org/wikipedia/en/7/76/Home_alone_poster.jpg",
	"https://www.youtube.com/watch?v=CK2Btk6Ybm0"
	)
m = [toy_story, avatar, hangover, home_alone]
fresh.open_movies_page(m)