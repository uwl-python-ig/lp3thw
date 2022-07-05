# EXERCISE 43 VIDEO GAME - BMR version
import bmr_ex43_scenes
from sys import exit


class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map # an instance of Map(object) !!!

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

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


