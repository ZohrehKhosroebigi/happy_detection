import os
import datetime
class Writelogs():
    def writing(self,msg1,msg2):
        if not os.path.exists("logs"):
            os.mkdir("logs")
        logfile = open('logs/log.txt', 'a')
        logfile.write("<-----" + str(datetime.datetime.now()) + "----->" + ' \n')
        logfile.write(msg1+'\n'+msg2+'\n')
        #return
