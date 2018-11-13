import numpy as np

####Adding and removing elements


#1. insert(arr, obj, values[, axis])

a = np.array([[1, 1], [2, 2], [3, 3]])
print(a)
print("\n")
print(np.insert(a, 1, 5))
print("\n")
print(a)
print("\n")
print(np.insert(a, 1, 5,axis=0))
print("\n")
print(np.insert(a, 1, 5,axis=1))
print("\n")
print(np.insert(a, [1], [[1],[2],[3]], axis=1))

#2. append(arr, values[, axis])

x = np.array([[1,2,3]])
y = np.array([[4,5,6],[7,8,9]])

print(np.append(x,y,axis=0))

#3. delete(arr, obj[, axis])

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(a)
print("\n")
b = np.delete(a, 1)
print(b)
print("\n")
b = np.delete(a, 1, axis=0)
print(b)

#4. unique(ar[, return_index, return_inverse, ...])

a = np.unique([1, 1, 2, 2, 3, 3])
print(np.unique(a))

print("\n")
a = np.array([[1, 0, 0], [1, 0, 0], [2, 3, 4]])
print(a)
print("\n")
print(np.unique(a, axis=0))


####Joining arrays


#1. concatenate((a1, a2, ...)[, axis])

#2. vstack(tup)

a = np.arange(16).reshape(4,4)
b = np.random.random(12).reshape(3,4)
print('a shape:',a.shape)
print('b shape:',b.shape)

c = np.vstack((a,b))    #Same as c = np.concatenate((a,b),axis=0)
print('c shape:',c.shape)

#3. hstack(tup)

a = np.arange(15).reshape(3,5)
b = np.random.random(12).reshape(3,4)
print('a shape:',a.shape)
print('b shape:',b.shape)

c = np.hstack((a,b))    #Same as c = np.concatenate((a,b),axis=1)
print('c shape:',c.shape)
