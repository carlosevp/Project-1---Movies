import media				# Importing media.py so we can use the class Movie.
import fresh_tomatoes		# Importing fresh_tomatoes.py so we can use the open_movies_page to generate the HTML website.

# Variable names should be lowercase, with words separated by underscores as necessary to improve readability.

starwars_ep1=media.Movie("Star Wars: Phantom Menace",
                      "Episode 1",
                      "https://upload.wikimedia.org/wikipedia/en/4/40/Star_Wars_Phantom_Menace_poster.jpg",
                      "https://www.youtube.com/watch?v=0MTp807E7_k");

starwars_ep2=media.Movie("Star Wars: Attack of the Clones",
                   "Episode 2",
                   "https://upload.wikimedia.org/wikipedia/en/3/32/Star_Wars_-_Episode_II_Attack_of_the_Clones_%28movie_poster%29.jpg",
                   "https://www.youtube.com/watch?v=5NWacXGA4nY")

starwars_ep3=media.Movie("Star Wars: Revenge of the Sith",
                      "Episode 3",
                      "https://upload.wikimedia.org/wikipedia/en/9/93/Star_Wars_Episode_III_Revenge_of_the_Sith_poster.jpg",
                      "https://www.youtube.com/watch?v=-lnegsUlzjM");

starwars_ep4=media.Movie("Star Wars: A New Hope",
                   "Episode 4",
                   "https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",
                   "https://www.youtube.com/watch?v=H38MpZtujJc")

starwars_ep5=media.Movie("Star Wars: Empire Strikes Back",
                      "Episode 5",
                      "https://upload.wikimedia.org/wikipedia/en/3/3c/SW_-_Empire_Strikes_Back.jpg",
                      "https://www.youtube.com/watch?v=Ft9a-CfdZi8");

starwars_ep6=media.Movie("Star Wars: Return Of The Jedi",
                   "Episode 6",
                   "https://upload.wikimedia.org/wikipedia/en/b/b2/ReturnOfTheJediPoster1983.jpg",
                   "https://www.youtube.com/watch?v=5UfA_aKBGMc")

starwars_ep7=media.Movie("Star Wars: The Force Awakens",
                      "Episode 7",
                      "https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg",
                      "https://www.youtube.com/watch?v=UitsQDWSlUg");

starwars_ep8=media.Movie("Star Wars: The Last Jedi",
                   "Episode 8",
                   "https://upload.wikimedia.org/wikipedia/en/7/7f/Star_Wars_The_Last_Jedi.jpg",
                   "https://www.youtube.com/watch?v=Q0CbN8sfihY&t=5s")

# Array with all the movies to display.
movies=[starwars_ep1,starwars_ep2,starwars_ep3,starwars_ep4,starwars_ep5,starwars_ep6,starwars_ep7,starwars_ep8]		
# Generates the HTML webpage with the movies defined in the array.
fresh_tomatoes.open_movies_page(movies)


