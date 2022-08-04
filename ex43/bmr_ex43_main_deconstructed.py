# EXCERCISE 43 VIDEO GAME - BMR
# SEE
# https://forum.learncodethehardway.com/t/yet-another-engine-post-ex43/5274/5
# "Try doing this on every line of code that has more than 1 dot until you start to see how the chains of dots work."

import bmr_ex43_scenes
from sys import exit

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map # I don't understand how the connection is made to the Map class here

    def play(self):
        # current_scene = self.scene_map.opening_scene()
        the_map = self.scene_map
        print("the map", the_map)
        the_opening_func = the_map.opening_scene # calling/using a Map class method here, ZS says, "no () to call it!"
        print("the opening function", the_opening_func)
        current_scene = the_opening_func()
        print("the current scene", current_scene)
        # last_scene = self.scene_map.next_scene('finished')
        the_map = self.scene_map
        print("the map", the_map)
        the_next_func = the_map.next_scene
        print("the next function", the_next_func)
        last_scene = the_next_func('finished')
        print("the last scene", last_scene)

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        
        current_scene.enter()

class Map(object):

    scenes = {
        'dark_forest': bmr_ex43_scenes.DarkForest() ,
        'the_river': bmr_ex43_scenes.TheRiver() ,
        'death': bmr_ex43_scenes.Death() ,
        'finished': bmr_ex43_scenes.Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('dark_forest')
a_game = Engine(a_map)
a_game.play()


