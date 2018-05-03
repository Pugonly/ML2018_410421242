from PIL import Image
import numpy as np
import scipy.misc


key1 = Image.open("key1.png")
key2 = Image.open("key2.png")
Eprime = Image.open("Eprime.png")
I = Image.open("I.png")


arrkey1=np.asarray(key1).copy()
arrkey2=np.asarray(key2).copy()
arrEprime=np.asarray(Eprime).copy()
arrI=np.asarray(I).copy()

data=np.zeros((120000,3),int)
temp=np.zeros((120000,1),int)

