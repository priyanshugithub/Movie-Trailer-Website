#This file defines the Movie class and its content 

#defining class movie
#This class contains variables for the title of the movie, its storyline
#the poster image of movie, its youtube trailer url and also its IMDb
#rating
class Movie() :
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_rating) : #required variables declared
          #variables initialized
          self.title = movie_title
          self.storyline = movie_storyline
          self.poster_image_url = poster_image
          self.trailer_youtube_url = trailer_youtube
          self.rating = movie_rating

    def show_trailer(self) : #defining function to display trailer
          webbrowser.open(self.trailer_youtube_url)   #using the python function to open webbrowser
                                                              #with youtube trailer of the given instance
 
