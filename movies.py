import fresh_tomatoes
import media

#Passing various arguments to the Movie class and initializing them with different variables

#1. Bajirao Mastani
bajirao = media.Movie("Bajirao Mastani",
                      "Love Story of a Maratha Warrior", "http://images.indianexpress.com/2015/11/bajirao-mastani.jpg",
                      "https://www.youtube.com/watch?v=eHOc-4D7MjY", "7.2")
#2. Rockstar
rockstar = media.Movie("Rockstar", "Story of heartbreak and chasing your dreams",
                       "https://upload.wikimedia.org/wikipedia/en/6/68/Rockstar-Movie-Poster.jpg",
                       "https://www.youtube.com/watch?v=bD5FShPZdpw", "7.6")
# 3. Guardians of Galaxy
guard = media.Movie("Guardians of Galaxy",
                         "A team of superheroes guarding the galaxy",
                    "http://t2.gstatic.com/images?q=tbn:ANd9GcQW3LbpT94mtUG1PZIIzJNxmFX399wr_NcvoppJ82k7z99Hx6in",
                    "https://www.youtube.com/watch?v=d96cjJhvlMA", "8.1")
# 4. Jungle Book 2016
mowgli = media.Movie("Jungle Book 2016",
                     "Story of Mowgli and his adventures as he is brought up by pack of wolves",
                     "http://t1.gstatic.com/images?q=tbn:ANd9GcQgNaB5wtt0G7_mTFVygkFtmjWut_Z0QSz2GzDsHeiZDHno4fjh",
                     "https://www.youtube.com/watch?v=5mkm22yO-bs", "7.6")
# 5. Avengers Age of Ultron
ultron = media.Movie("Avengers-Age of ultron","A Team of Superheroes to fight an AI system ready to destroy the world",
                     "http://t0.gstatic.com/images?q=tbn:ANd9GcRlGeugacRkKznDOtRhUCVt0AkrOTPbaaKwF9xgGZgNViyC_Xko",
                     "https://www.youtube.com/watch?v=tmeOjFno6Do", "7.5")
# 6 . Drishyam
drishyam = media.Movie("Drishyam", "Visuals can be deceptive",
                       "http://t1.gstatic.com/images?q=tbn:ANd9GcTkMKFMrv9gfroA4CC9c9C_d8I1NrhiGgVhYGL7xMWO5oylqi4_",
                       "https://www.youtube.com/watch?v=AuuX2j14NBg", "8.7")

  # Using List for calling each instance of Movie class into our web page
movies = [bajirao, rockstar, guard, mowgli, ultron, drishyam]

# Using the open_movies_page method present in fresh_tomatoes.py file to open the web page
fresh_tomatoes.open_movies_page(movies)
