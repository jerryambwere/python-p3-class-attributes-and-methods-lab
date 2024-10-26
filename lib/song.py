class Song:
    count = 0  # Class variable to keep track of the number of songs
    genres = []  # Class variable to store unique genres
    artists = []  # Class variable to store unique artists
    genre_count = {}  # Class variable for genre count
    artist_count = {}  # Class variable for artist count

    def __init__(self, name, artist, genre) -> None:
        self.name = name
        self.artist = artist
        self.genre = genre
        
        Song.add_song_to_count()  # Increment the song count
        Song.add_to_genres(genre)  # Add genre to the unique genres list
        Song.add_to_artists(artist)  # Add artist to the unique artists list
        Song.add_to_genre_count(genre)  # Update genre count
        Song.add_to_artist_count(artist)  # Update artist count

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1  # Increment the count by one

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:  # Check for uniqueness
            cls.genres.append(genre)  # Add genre if it's not already in the list

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:  # Check for uniqueness
            cls.artists.append(artist)  # Add artist if it's not already in the list

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1  # Increment the count for existing genre
        else:
            cls.genre_count[genre] = 1  # Initialize count for new genre

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1  # Increment count for existing artist
        else:
            cls.artist_count[artist] = 1  # Initialize count for new artist

    @classmethod
    def show_song_count(cls):
        print(f"Total number of songs: {cls.count}")

    @classmethod
    def show_genres(cls):
        print("Unique genres:", cls.genres)

    @classmethod
    def show_artists(cls):
        print("Unique artists:", cls.artists)

    @classmethod
    def show_genre_count(cls):
        print("Genre counts:", cls.genre_count)

    @classmethod
    def show_artist_count(cls):
        print("Artist counts:", cls.artist_count)

# Example Usage
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
another_song = Song("Lose Yourself", "Eminem", "Rap")
pop_song = Song("Shape of You", "Ed Sheeran", "Pop")

# Displaying counts and lists
Song.show_song_count()  # Output: Total number of songs: 3
Song.show_genres()      # Output: Unique genres: ['Rap', 'Pop']
Song.show_artists()     # Output: Unique artists: ['Jay-Z', 'Eminem', 'Ed Sheeran']
Song.show_genre_count() # Output: Genre counts: {'Rap': 2, 'Pop': 1}
Song.show_artist_count() # Output: Artist counts: {'Jay-Z': 1, 'Eminem': 1, 'Ed Sheeran': 1}
