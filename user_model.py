import numpy as np
from keras_applications.densenet import preprocess_input
from matplotlib import image
from matplotlib.pyplot import imshow
class Usertest():
    def usrtest(self,predictmodel):
        img_path = 'image/1.jpg'
        img = image.load_img(img_path, target_size=(64, 64))
        imshow(img)
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        print(predictmodel.predict(x))