from __future__ import print_function
import yaml
import os
import webbrowser

from keras.models import model_from_yaml
from betago.model import KerasBot
from betago.dataloader.processor import SevenPlaneProcessor

processor = SevenPlaneProcessor()

model_file = 'model_zoo/idiot_bot.yml'
weight_file = 'model_zoo/idiot_weights.hd5'

with open(model_file, 'r') as f:
    yml = yaml.load(f)
    model = model_from_yaml(yaml.dump(yml))
    model.load_weights(weight_file)

# Open web frontend and serve model
webbrowser.open('file://' + os.getcwd() + '/ui/demoBot.html', new=2)
go_model = KerasBot(model=model, processor=processor)