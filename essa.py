
import numpy as np
np.random.seed(50)

#X=np.random.randint(0,100,(8,8))
#print(X)
X_re=np.random.randint(0,100,(4,4))
#print(X_re)
Y_re=np.random.randint(0,100,(4,4))
#print(X_re)

def Hossam (X_re,Y_re):
    Z= np.dot(X_re,Y_re)
    return Z

res=Hossam (X_re,Y_re)
print(res)
