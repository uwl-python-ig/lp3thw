# Gothons from Planet Percal #25 - BMR version

class Scene(object):

    def enter(self):
        pass

# class Engine *was* here--does it need to be here??

# Child classes Death, CentralCorridor, LaserWeaponArmory, TheBridge, EscapePod

class Death(Scene):

    def enter(self):
        pass

class CentralCorridor(Scene):

    def enter(self):
        # Test
        print("You find yourself in the central corridor of this spaceship...")
        # Ah... of course this string is not returned yet
        # This is because class Engine has not been defined yet!

class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass

class Engine(object):

    def __init__(self, scene_map):
        pass

    def play(self):
        pass

class Map(object):
    # Map questions:
    # I don't understand why the Map class needs a start_scene attribute as well as an opening_scene method

    # NOTE001
    # ALRIGHT I'm going to cheat a bit and grab the "answer" for class Map as a way to get started

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        # still need to define finished
        # 'finished': Finished(),

    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
