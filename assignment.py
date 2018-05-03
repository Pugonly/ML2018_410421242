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

for h in range(300):
    for w in range(400):
        data[h*400+w][0]=arrkey1[h][w]
        data[h*400+w][1]=arrkey2[h][w]
        data[h*400+w][2]=arrI[h][w]
        temp[h*400+w]=arrEprime[h][w]


x=np.array([0,0,0])
maxlimit=10
temp_x0=10
temp_x1=10
temp_x2=10

epoch=1
while epoch <maxlimit and abs(x[0]-temp_x0)> 0.00001 and abs(x[1]-temp_x1)>0.00001 and abs(x[2]-temp_x2)>0.00001:
    temp_x0=x[0]
    temp_x1=x[1]
    temp_x2=x[2]
    for i,w in enumerate(data):
        t=x[0]*w[0]+x[1]*w[1]+x[2]*w[2]
        k=temp[i]-t
        x=x+0.00001*k*w
    epoch+=1

print(x[0],x[1],x[2])
