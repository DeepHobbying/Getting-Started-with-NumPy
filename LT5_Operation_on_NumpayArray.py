import numpy as np

#Basic Operations
###########################################################################################
import numpy as np

a = np.array([20,30,40,50])
b = np.arange(4)

print("a =",a)
print("b =",b)
print("a+b =",a+b)
print("b to the power 2",b**2)
print("a*b =",a*b)

###########################################################################################

b = b.T
print("a matrix multiplication with b =",a@b)		# @ operator, works in python >=3.5
print("a matrix multiplication with b =",a.dot(b))	# drop method. same as np.dot(a,b)
# np.matmul(a,b) will also do the same thing

###########################################################################################

a = np.ones((1,3), dtype=int)
b = np.random.random((1,3))
print(b)
b += a
print("after opertaion:")
print(b)

try:
    a += b
    print(a)
except Exception  as exp:
    print(exp)
    

###########################################################################################

b = np.arange(12).reshape(3,4)
print(b)
print("sum of each column:")
print(b.sum(axis=0))
print("cumulative sum along each row:")
print(b.cumsum(axis=1))

###########################################################################################


#Universal Functions
###########################################################################################
a = np.arange(3)
print(a)
print(np.exp(a))

###########################################################################################


#Broadcasting
###########################################################################################
a = np.arange(12).reshape(3,4)
print(a)
b = a + 2   #same as a + np.array([2])
print("broadcast happened when we perform a + 2")
print(b)
###########################################################################################
