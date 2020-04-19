from writing import Writelogs
from keras import layers
from keras.layers import Input, Dense, Activation, ZeroPadding2D, BatchNormalization, Flatten, Conv2D
from keras.layers import AveragePooling2D, MaxPooling2D, Dropout, GlobalMaxPooling2D, GlobalAveragePooling2D
from keras.models import Model
from keras.preprocessing import image
from keras.utils import layer_utils
from keras.utils.data_utils import get_file
from keras.applications.imagenet_utils import preprocess_input
#import pydot
from IPython.display import SVG
from keras.utils.vis_utils import model_to_dot
from keras.utils import plot_model
#from kt_utils import *
import keras.backend as K
K.set_image_data_format('channels_last')
#import matplotlib.pyplot as plt
#from matplotlib.pyplot import imshow
class Happymodel():

    def __init__(self,input_shape,ziropad,no_filter,conv_filter_size,conv_stride,conv_activ_func,pool_filter_size,fully_activ_func,modelname):
        try:
            self.input_shape=input_shape
            self.ziropad=ziropad
            self.no_filter=no_filter
            self.conv_filter_size=conv_filter_size
            self.conv_stride=conv_stride
            self.conv_activ_func=conv_activ_func
            self.pool_filter_size=pool_filter_size
            self.fully_activ_func=fully_activ_func
            self.modelname=modelname
        except Exception as err:
            preprocess_input(err)
    def happymodel(self):
        """
        Implementation of the HappyModel.

        Arguments:
        input_shape -- shape of the images of the dataset
            (height, width, channels) as a tuple.
            Note that this does not include the 'batch' as a dimension.
            If you have a batch like 'X_train',
            then you can provide the input_shape using
            X_train.shape[1:]
        """
        ###Returns:
        # model -- a Model() instance in Keras
        """

        ### START CODE HERE ###
        # Feel free to use the suggested outline in the text above to get started, and run through the whole
        # exercise (including the later portions of this notebook) once. The come back also try out other
        # network architectures as well. 
        """
        self.X_input = Input(self.input_shape)
        self.X = ZeroPadding2D((self.ziropad, self.ziropad))(self.X_input)
        # CONV -> BN -> RELU Block applied to X
        self.X = Conv2D(self.no_filter, (self.conv_filter_size, self.conv_filter_size), strides=(self.conv_stride,self.conv_stride), name='conv0')(self.X)
        self.X = BatchNormalization(axis=3, name='bn0')(self.X)
        self.X = Activation(self.conv_activ_func)(self.X)

        # MAXPOOL
        self.X = MaxPooling2D((self.pool_filter_size, self.pool_filter_size), name='max_pool')(self.X)

        # FLATTEN X (means convert it to a vector) + FULLYCONNECTED
        self.X = Flatten()(self.X)
        self.X = Dense(1, activation=self.fully_activ_func, name='fc')(self.X)

        # Create model. This creates your Keras model instance, you'll use this instance to train/test the model.
        self.model_ = Model(inputs=self.X_input, outputs=self.X, name=self.modelname)
        print("-----initialzing model is done----")
        return self.model_

    def compilemodel(self):
        self.model_.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
        return self.model_
    def trainmodel(self,x_train,y_train,epoch,batch_size):
        self.model_.fit(x=x_train, y=y_train, epochs=epoch, batch_size=batch_size)
        return self.model_

    def evaluatemodel(self,x_test,y_test):
        preds = self.model_.evaluate(x=x_test, y=y_test)
        mywriting=Writelogs()
        mywriting.writing("Loss = " + str(preds[0]),"Test Accuracy = " + str(preds[1]))
        #print("------results-------")
        #print("Loss = " + str(preds[0]))
        #print("Test Accuracy = " + str(preds[1]))
        return self.model_


