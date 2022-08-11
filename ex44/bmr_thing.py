# bmr_thing.py
from bmr_speaking import Voice

print("instantiate Voice")
voice = Voice()
print("call Voice method say_hey()")
voice.say_hey()

class BirdVoice(object):
    def __init__(self):
        self.voice = Voice()
    def say_hey(self):
        self.voice.say_hey()
    def chirp(self):
        print("chirp")

print("instantiate bird_voice")
birdie = BirdVoice()
print("call Voice method say_hey()")
birdie.say_hey()
print("call BirdVoice method chirp()")
birdie.chirp()

"""
QUESTIONS:
- Why no init in Voice? (or in ex44e > Other?)
- Why init in BirdVoice?
    + Because self.voice needs to be instantiated as class Voice, so that
    the methods say_hey, say_bye can be called...
"""