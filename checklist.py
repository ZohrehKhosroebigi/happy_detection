from keras_applications.densenet import preprocess_input
from matplotlib import image
from matplotlib.pyplot import imshow
from writing import Writelogs

from Load_show_data import *
from Normalization import *
from model import Happymodel
from user_model import Usertest

# Load data
myload = Loaddata()
myload.load
print(myload)
myload.showpic(11)
# Normal data
mynorm = NoramlPic(myload.load)
mynorm.norm
print(mynorm)
# Test model
# input_shape, ziropad, no_filter, conv_filter_size, conv_stride, conv_activ_func, pool_filter_size,fully_activ_func, modelname
mymodel = Happymodel(mynorm.X_train.shape[1:], 3, 32, 7, 1, 'relu', 2, 'sigmoid', 'HappyModel')
mymodel.happymodel()
mymodel.compilemodel()
mymodel.trainmodel(mynorm.X_train, mynorm.Y_train, 20, 64)
mymodel.evaluatemodel(mynorm.X_test, mynorm.Y_test)
# user
#mytest = Usertest()
#mytest.usrtest(mymodel.model_)
#mymodel.model_.summary()
#plot_model(mymodel.model_, to_file='HappyModel.png')
#SVG(model_to_dot(mymodel.model_).create(prog='dot', format='svg'))
