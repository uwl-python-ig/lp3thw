
class Region(object):
    pass

class Grasslands(Region):
    
    appellation = "The Grasslands"
    description = 'Golden wheat stretches out as far as the eye can see in every direction'
    adjacent = ['Mountains']
    
    # ok this works but why not implement describe() in the parent class??
    def describe(self):
        print(Grasslands.description)

class Mountains(Region):

    appellation = "The Mountains"
    description = 'Graggy granite peaks'
    adjacent = ['Grasslands']

    def describe(self):
        print(Mountains.description)