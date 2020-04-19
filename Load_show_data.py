from load_data import load_dataset
import numpy as np
import matplotlib.pyplot as plt
class Loaddata():##  Load data
    def __init__(self):
        X_train_orig = ""
        Y_train_orig = ""
        X_test_orig = ""
        Y_test_orig = ""
        classes = ""
    @property
    def load(self):
        self.X_train_orig,self.Y_train_orig,self.X_test_orig,self.Y_test_orig,self.classes =load_dataset()
        return self.X_train_orig,self.Y_train_orig,self.X_test_orig,self.Y_test_orig,self.classes
#show an image of x_train to user

    def showpic(self,idx):
        print(self.X_train_orig[idx].shape)
        plt.imshow(self.X_train_orig[idx])
        #plt.show()
        print(f'y= {np.squeeze(self.Y_train_orig[:,idx])}')


    def __str__(self):
        try:
            return f'Orginal data inclueds: X_train_orig shape {self.X_train_orig.shape}\n Y_train_orig shape{self.Y_train_orig.shape}\n X_test_orig shape{self.X_test_orig.shape}\n Y_test_orig shape {self.Y_test_orig.shape}\n, Classes is: {self.classes}\n number of training examples= {self.X_train_orig.shape[0]}\n number of test examples= {self.X_test_orig.shape[0]}'
        except Exception as err:
            print(err)

    def __repr__(self):
        try:
            return f'{self.X_train_orig}{self.Y_train_orig}{self.X_test_orig}{self.Y_test_orig}{self.classes}{self.X_train_orig.shape[0]}{self.X_test_orig.shape[0]}'
        except Exception as err:
            print(err)