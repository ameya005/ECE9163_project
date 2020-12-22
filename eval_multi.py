"""
Eval script
"""

import keras
import sys
from PIL import Image
from eval import data_preprocess
import numpy as np

model_path = './models/multi_trigger_multi_target_bd_net.h5'
rep_model_path = './models/multi_trigger_multi_target_bd_net_repaired.h5'

img = np.array(Image.open(sys.argv[1]))
img = np.expand_dims(img, 0) # bs, sx, sy, ch
img = data_preprocess(img)

orig_model = keras.models.load_model(model_path)
rep_model = keras.models.load_model(rep_model_path)

orig_pred = np.argmax(orig_model.predict(img), axis=1)
rep_pred = np.argmax(rep_model.predict(img), axis=1)

if orig_pred == rep_pred:
    print(orig_pred)
else:
    print(-1)


