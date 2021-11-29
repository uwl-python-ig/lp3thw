# Gothons from Planet Percal #25 - BMR version

class Scene(object):

    # OK, obviously we are going to wan't a description for each scene right??
    # Is this the place where we will want to specify what scene is next??
    def __init__(self, description, next_scene):
        self.description = description
        self.next_scene = next_scene

    def enter(self):
        print(self.description)

class Engine(object):

    def __init__(self, scene_map):
        # what does the scene_map param do??
        pass

    def play(self):
        pass

# Child classes Death, CentralCorridor, LaserWeaponArmory, TheBridge, EscapePod
class Death(Scene):

    def enter(self):
        pass

class CentralCorridor(Scene):

    # let's add next_scene to the args
    def __init__(self, description, next_scene):
        super().__init__(description, next_scene)

    # we have the enter method from Scene above

class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass

class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

"""
a_map = Map('central_corridor')
a_game = Engine(a_map) # missing an argument
a_game.play()
"""
