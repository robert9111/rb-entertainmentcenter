import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title #Designate title
        self.storyline = movie_storyline #Designate storyline
        self.poster_image_url = poster_image #Designate poster image
        self.trailer_youtube_url = trailer_youtube #Designate youtube trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
