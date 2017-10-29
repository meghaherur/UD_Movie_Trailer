
import webbrowser

class Movie_Parent():
    def __init__(self,movie_title,run_time):
      self.title=movie_title
      self.running_time=run_time

class Movie(Movie_Parent):
    """ This is a movie class to capture all details about movie""" 
   
    def __init__(self,movie_title,run_time,poster_image,trailer_youtube):
       Movie_Parent.__init__(self,movie_title,run_time)
       self.poster_image_url = poster_image
       self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
       webbrowser.open(self.trailer_youtube_url)
        
