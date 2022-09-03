
class Region(object):
    pass

class Grasslands(Region):
    
    # better to implement vars in the parent class, then override values in child classes?
    appellation = "the grasslands"
    description = 'golden wheat stretches out as far as the eye can see in every direction'
    # add adjacent region(s) to create choice of where to go next
    creatures = ['unicorn']

class Mountains(Region):

    appellation = "The Mountains"
    description = 'Graggy granite peaks'
    # add adjacent region(s) to create choice for where to go next
    creatures = ['troll']

