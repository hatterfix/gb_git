from model_elements import ModelElements
from scene import Scene

class ModelStore(ModelElements):
    def __init__(self):
        self.scenes = []

    def add_scene(self, scene):
        self.scenes.append(scene)

    def remove_scene(self, scene):
        self.scenes.remove(scene)
