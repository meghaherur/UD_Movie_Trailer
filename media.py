import webbrowser


class Movie_Parent():
    """This is a parent class"""
    def __init__(self, movie_title, run_time):  # Class Constructor
        self.title = movie_title
        self.running_time = run_time


class Movie(Movie_Parent):
    """ This is a movie class to capture all details about movie"""
    """ This is a child Class"""

    def __init__(self, movie_title, run_time,
                 poster_image, trailer_youtube):  # Child constructor
        Movie_Parent.__init__(self, movie_title, run_time)
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):  # Class Method
        webbrowser.open(self.trailer_youtube_url)
