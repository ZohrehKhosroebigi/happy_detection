from Load_show_data import *
from Normalization import *
#Load data
myload=Loaddata()
myload.load
print(myload)
myload.showpic(11)
#Normal data
mynorm=NoramlPic(myload.load)
mynorm.norm
print(mynorm)
