#############################
##I. Conversion from other Python structures (e.g., lists, tuples)

import numpy as np

x = [1,3,6,9]
a = np.array(x)
print(a)


x = [1.0,3,6,9]
a = np.array(x)
print(a)


##############################
#important attributes of a ndarray object:

import numpy as np
x = [[1,2,3],[4,5,6]]
a = np.array(x)


print(a.ndim)

print(a.shape)

print(a.size)

print(a.dtype)

import numpy as np
x=(1,2,3)
print(np.int_(a))
print(np.array(a,dtype=np.float64))

print(a.itemsize)

print(a.dtype.itemsize)


##############################
##II. Intrinsic numpy array creation objects (e.g., arange, ones, zeros, etc.)

import numpy as np
print(np.arange( 10, 30, 5 ))
print(np.arange( 0, 2, 0.3 ))	# it accepts float arguments
print(np.linspace( 0, 2, 9 ))   # 9 numbers from 0 to 2

##############################
import numpy as np
a = np.zeros((4,3))
print("Array created with numpy.zeros function\n",a)

a = np.ones(3)
print("Array created with numpy.ones function\n",a)

a = np.empty((2,4))
print("Array created with numpy.empty function\n",a)


##############################
##III. Use of special library functions (e.g., random)


import numpy as np
print(np.random.random((1,3)))
