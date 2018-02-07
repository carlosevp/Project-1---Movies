import Media
import fresh_tomatoes

toy_story=Media.Movie("Toy Story",
                      "A story of a boy and his toys that come to life",
                      "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                      "https://www.youtube.com/watch?v=vwyZH85NQC4");
#print(toy_story.storyline)

avatar=Media.Movie("Avatar",
                   "A marine on an alian planet",
                   "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                   "http://www.youtube.com/watch?v=9ceBgWV8io")
#print(avatar.storyline)
#avatar.show_trailer()


movies=[toy_story, avatar]
#fresh_tomatoes.open_movies_page(movies)

#print(Media.Movie.VALID_RATINGS)

print(Media.Movie.__doc__)
print(Media.Movie.VALID_RATINGS[2])
