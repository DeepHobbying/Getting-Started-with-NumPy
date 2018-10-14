import numpy as np

a = np.arange(10)
print(a)
print(a[5])         #get 5th indexed or 6th element
print(a[2:6])       #get from 2nd to 6th element
print(a[:8:3])      #get from start to index 8, exclusive, get every 3rd element
print(a[-1])        #get last element
print(a[-3:-1])     #get 3rd positioned element from right till last positioned element (excluding itself)
print(a[ : :-1])    #reversed a

##########################################################

a = np.arange(10,1,-1)
my_list=[4,8,1]

print(a)
print(a[my_list])

##########################################################

a = np.arange(35).reshape(5,7)
print(a)

print(    a[3,4]    )
print(    a[0:3,1:3]    )
print(    a[np.array([0,2,4]), np.array([0,1,2])]    )
print(    a[::3,1:6:3]    )

##########################################################

a = np.arange(10)
cond = a>5
print(a)
print(cond)
print(a[cond])
