# import os.path
# import numpy as np
# import collections

# datasets = [[1,np.random.random_integers(7,9),np.random.random_integers(2,6),np.random.random_integers(23,28)] for _ in range(100000)]#np.random.random_integers(1,14,1000) + np.random.random_integers(60,100,1000)


# # np.set_printoptions(precision=5)
# # np.set_printoptions(suppress=True)
# print (datasets)
# print (len(datasets))
# np.savetxt("clean.txt", datasets, fmt='%i', delimiter=" ")

import time
from firebase import firebase 
import numpy as np

firebase = firebase.FirebaseApplication('https://storage-97729.firebaseio.com',None)

for _ in range(10000):
    # phrandom = np.random.random_integers(7,9)
    # turbidityrandom = np.random.random_integers(2,6)
    # temprandom = np.random.random_integers(23,28)
    # timestr = time.strftime("%Y-%m-%d %I:%M:%S")
    format_list = [np.random.random_integers(7,9),np.random.random_integers(2,6),np.random.random_integers(23,28),time.strftime("%Y-%m-%d %I:%M:%S")]

    data = {"value" : "{} {} {} {}".format(*format_list)}
    print(data)
    firebase.post('/FXRD3214',data)
    time.sleep(5)


