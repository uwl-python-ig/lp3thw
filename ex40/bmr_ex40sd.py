rule = "-" * 15
short_rule = "-" * 5

class Song(object):

    def __init__(self, lyrics, title):
        self.lyrics = lyrics
        self.title = title

    def sing_me_a_song(self):
        print(self.title, "\n", rule)
        for line in self.lyrics:
            print(line)

    def song_lines(self):
        print("That particular song had", len(self.lyrics), "lines.")

song1 = [
    "This is song 1",
    "It's a beautiful song",
    "It has three lines",
    "Oh yes",
    "I've got to keep singing",
    "Because I don't want the song to end yet"
    ]

song1Title = "Song The Firste"

song2 = [
    "Song 2 is also beautiful",
    "The words rhyme so well",
    "Rhyming is subjective",
    "Wouldn't you say?"
    ]

song2Title = "Song The Seconde"

one = Song(song1, song1Title)
two = Song(song2, song2Title)

one.sing_me_a_song()
print(short_rule)
one.song_lines()
print(rule)
two.sing_me_a_song()
print(short_rule)
two.song_lines()
