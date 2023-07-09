class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_to_genres(genre)
        Song.add_song_to_count()
        Song.add_to_artists(artist)

    @classmethod
    def add_song_to_count(cls, inc = 1):
        cls.count += inc

    @classmethod
    def add_to_genres(cls, genre):
        if not genre in cls.genres:
            cls.genres.append(genre)
            cls.genre_count[genre]=1
        else:
            cls.genre_count[genre] = cls.genre_count[genre] +1

    @classmethod
    def add_to_artists(cls, artist):
        if not artist in cls.artists:
            cls.artists.append(artist)
            cls.artist_count[artist] =1
        else:
            cls.artist_count[artist] = cls.artist_count[artist]+1

            