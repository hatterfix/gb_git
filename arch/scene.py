from model_elements import ModelElements
from poligonal_model import PoligonalModel
from flash import Flash
from camera import Camera

class Scene(ModelElements):
    def __init__(self, poligonal_model, flash, camera):
        self.poligonal_model = poligonal_model
        self.flash = flash
        self.camera = camera
