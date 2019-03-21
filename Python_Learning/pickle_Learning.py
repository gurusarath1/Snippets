# Created by Guru Sarath
# 18 December 2018

import pickle

ExampleDict = {1:'A',2:'B',0:'A',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H'}

pickle_file = open('PickledFile.pickle','wb')

pickle.dump(ExampleDict, pickle_file)

pickle_file.close()

#------------

fileX = open('PickledFile.pickle', 'rb')
obj = pickle.load(fileX)
print(obj)
fileX.close()