import numpy as np


#Rearranging elements

a = np.arange(12)
print(a)
print(np.flip(a))

a = a.reshape((4,3),order='C')    #Same as a = np.resize(a,(4,3))

#You can also call these ndarray instance's method
#via numpy (np in this case) class,
#which is: a = np.reshape(a,(4,3))

print(a)

print(np.ravel(a))


###Transpose-like operations

a = np.arange(24).reshape(2,3,4)
print(a)
print('a shape:',a.shape)
print("\n")
print(a.T)		#Same as print(np.transpose(a,(2,1,0)))
print('a.T shape:',a.T.shape)


print('a shape:',a.shape)

b = np.moveaxis(a,1,0)		#Same as b=np.swapaxes(a,1,0)
print('b shape:',b.shape)


a = np.ones((3,4,5,6))
print('a shape:',a.shape)

b = np.rollaxis(a,3)
print('np.rollaxis(a,3) shape:',b.shape)

b = np.rollaxis(a,3,2)
print('np.rollaxis(a,3,2) shape:',b.shape)
