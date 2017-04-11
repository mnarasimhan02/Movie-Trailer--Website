import media
import fresh_tomatoes
# Movie objects to store different movie details

inglo_bas = media.Movie("Inglorious Basterds",
             			"2009 American-German war film written",
             			"https://furiousreviews.files.wordpress.com/2015/03/7736093674_2e8414a35c_o.jpg",
	    	 			"https://www.youtube.com/watch?v=KnrRy6kSFF0")
avatar = media.Movie("Avatar",
        			 "A marine on Align planet",
	 				 "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
	 				 "https://www.youtube.com/watch?v=d1_JBMrrYw8")
rogue_nation = media.Movie("Mission: Impossible – Rogue Nation",
              		   	   "American action spy film",
	           			   "https://images-na.ssl-images-amazon.com/images/M/MV5BOTFmNDA3ZjMtN2Y0MC00NDYyLWFlY2UtNTQ4OTQxMmY1NmVjXkEyXkFqcGdeQXVyNTg4NDQ4NDY@._V1_UX182_CR0,0,182,268_AL_.jpg",
	                       "https://www.youtube.com/watch?v=nmC6rZyByzk")
pirates_of_carribbean = media.Movie("Dead Men Tell No Tales (2017)",
                        			"Is a series of fantasy swashbuckler films",
	                    			"https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-12561-nie8b7_49ceb417.jpeg?region=0%2C0%2C300%2C450",
	                    			"https://www.youtube.com/watch?v=KtsNKGrUMtk")
lego_batman = media.Movie("The LEGO Batman Movie",
              			  "2017 3D computer-animated superhero comedy film",
	          			  "https://images-na.ssl-images-amazon.com/images/M/MV5BMTcyNTEyOTY0M15BMl5BanBnXkFtZTgwOTAyNzU3MDI@._V1_UX182_CR0,0,182,268_AL_.jpg",
	          			  "https://www.youtube.com/watch?v=_pc2-y8WJn8")
django_unchained = media.Movie("Django unchained",
                  			   "American revisionist Western film",
	                           "https://secure.netflix.com/us/boxshots/ghd/70230640.jpg",
	              			   "https://www.youtube.com/watch?v=ztD3mRMdqSw")
movies=[inglo_bas,avatar,rogue_nation,pirates_of_carribbean,lego_batman,django_unchained]

# Call fresh_tomatoes to render html with the movie objects
fresh_tomatoes.open_movies_page(movies)
