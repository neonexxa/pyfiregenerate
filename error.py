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
import smtplib
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("-e", "--errorornot", required = True)
args = vars(ap.parse_args())


firebase = firebase.FirebaseApplication('https://storage-97729.firebaseio.com',None)

if (args["errorornot"] == "e"):
    data = "Signal Lost"
    print(data)
    firebase.put('','/error',data)
if (args["errorornot"] == "o"):
    data = "ok"
    print(data)
    firebase.put('','/error/',data)
    # pass
    # time.sleep(5)
    # pass
# for _ in range(1):
    # phrandom = np.random.random_integers(7,9)
    # turbidityrandom = np.random.random_integers(2,6)
    # temprandom = np.random.random_integers(23,28)
    # timestr = time.strftime("%Y-%m-%d %I:%M:%S")
    # format_list = [np.random.random_integers(3,5),np.random.random_integers(900,1055),np.random.random_integers(20,25),time.strftime("%Y-%m-%d %I:%M:%S")]

    





