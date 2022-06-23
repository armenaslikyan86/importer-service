from psd_tools import PSDImage
from flask import json

class ImporterService:

    def __init__(self):
        self.psd = PSDImage.open('rich-text.psd')
        self.psd.composite().save('rich-text.png')

    def get_layers(self):
        data = {}
        for layer in self.psd:
            data[json.dumps(layer.__repr__())] = json.dumps(layer.composite().__repr__())
        return data


