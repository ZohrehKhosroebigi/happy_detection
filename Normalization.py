from  one_hot import convert_to_one_hot
class NoramlPic():
    def __init__(self, myobj):
        X_train = ""
        Y_train = ""
        X_test = ""
        Y_test = ""
        classes = ""
        try:
            self.X_train, self.Y_train, self.X_test, self.Y_test, self.classes =  myobj
        except Exception as err:
            print(err)
    @property
    def norm(self):
        self.X_train=self.X_train/255.
        self.X_test=self.X_test/255.
        self.Y_train=self.Y_train.T
        self.Y_test=self.Y_test.T
        ##self.Y_train=convert_to_one_hot(self.Y_train,len(self.classes)).T
        ##self.Y_test = convert_to_one_hot(self.Y_test, len(self.classes)).T
        self.classes = self.classes
        return self.X_train,self.X_test,self.Y_train,self.Y_test,self.classes

    def __str__(self):
        return f'---information of normal---- number of training examples = {self.X_train.shape[0]}\nnumber of test examples = {self.X_test.shape[0]}\nX_train shape :  {self.X_train.shape}\n' \
               f'Y_train shape: {self.Y_train.shape}\n X_test shape: {self.X_test.shape}\n Y_test shape: {self.Y_test.shape}\n classes shape: {self.classes.shape} len classes is: {len(self.classes)}\n '
    def __repr__(self):
        return f'{self.X_train}{self.Y_train}{self.X_test}{self.Y_test}{self.classes}{self.X_train.shape[0]}{self.X_test.shape[0]}'



