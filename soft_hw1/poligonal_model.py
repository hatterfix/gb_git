from model_elements import ModelElements
from texture import Texture
from poligon import Poligon

class PoligonalModel(ModelElements):
    def __init__(self, texture, poligon):
        self.texture = texture
        self.poligon = poligon
