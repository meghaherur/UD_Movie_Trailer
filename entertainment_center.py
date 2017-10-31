import media
import fresh_tomatoes

# Creating Movie instance Toy Story:

toy_story = media.Movie("Toystory", "1.5 hr",
                        "https://lumiere-a.akamaihd.net/v1/images"
                        "/open-uri20150422-20810-m8zzyx_5670999f.jpeg"
                        "?region=0%2C0%2C300%2C450",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")

# Creating Movie instance Inception:

Inception = media.Movie("Inception", "2.0 hr",
                        "https://cdn.empireonline.com/jpg/80/0/0/1000/"
                        "563/0/north/0/0/0/0/0/t/films/27205/images"
                        "/s2bT29y0ngXxxu2IA8AOzzXTRhd.jpg",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")

# Creating Movie Instance Moana:

moana = media.Movie("Moana", "1.75 hr",
                    "http://cdn5.thr.com/sites/default/files"
                    "/2016/09/moana_still_h_2016.jpeg",
                    "https://www.youtube.com/watch?v=LKFuXETZUsI")

# Creating Movie List for website

movie_list = [toy_story, Inception, moana]

# Calling html code to display
fresh_tomatoes.open_movies_page(movie_list)


