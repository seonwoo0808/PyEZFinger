#   © 2021 정선우 <seonwoo0808@kakao.com>
#   datapackage\fingerrecognize\fingerrecognize.py

import os
import numpy as np

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import keras
try:    
    model = keras.models.load_model(os.path.abspath(os.path.dirname(__file__)) + '\\finger_model.h5')
except:
    print("You Need to Download and Place Model File")
    exit()
labels = [False, True]

class Finger():
    def __init__(self, image):
        self.finger = self.make_numpy_image(image)
        self.label = None
    def edit_label(self, label):
        self.label = label
    def make_numpy_image(self, image):
        image = image.convert('L')
        image = image.resize((90, 90))
        numpy_image = np.array(image)
        numpy_image = numpy_image.reshape((90, 90, 1))
        return np.expand_dims(numpy_image, axis=0) / 255
    def compare(self, otherfinger):
        if type(otherfinger) == Finger:
            y_predict = model.predict([self.finger, otherfinger.finger])
            if y_predict[0][0] > 0.6:
                result = True
            else:
                result = False
            return result_object(result,y_predict[0][0])
        else:
            raise TypeError("parameter must be Finger object!")
class result_object:
    def __init__(self,match,ratio):
        self.match = match
        self.ratio = ratio