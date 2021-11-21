import numpy as np

a = np.array([2,3,4])
print(a)

b = np.arange(1, 12, 2) # from 1 to 12, in step of 2
print(b)

np.random.shuffle(b) # in place shuffle
print("shuffle the array in random order", b)

rand_num = np.random.choice(b) # in place shuffle
print("Pick a random number from the array", rand_num)

c = np.linspace(1, 12, 6) # space from 1.0 to 12.0 with even spacing upto 6 elements
print(c)

d = c.reshape(3, 2) # reshape one-dimensional array to 2 dimensional array
print(d)
print(d.size) # size of the array - total number of elements across column and rows
print(d.shape) # shape of the matrix
print(d.dtype) # data type used for elements, typically np.float64 is the type use by default

print(d.itemsize) # amount of size in memory for one element

e = np.array([(1.5, 2, 3), (4, 5, 6)]) # creating 2-dimensional array
print(e)
print(e < 4) # compare each element of array and returns a true/false as an array

f = e * 3
print(f)

print(np.zeros((3, 4))) # 3, 4 matrix with all 0s
print(np.ones((3, 2))) # 3, 2 matrix with all 1s
print(np.ones(10)) # 1-dim matrix/vector, with all 1s

# explicitly set data type to int16 (instead of float64)
g = np.array([1, 2, 3], dtype=np.int16)
print(g)

rand_array = np.random.random((2, 3))
np.set_printoptions(precision=2, suppress=True) # precision is set to 2 decimal places and suppress scientific notification (e)
print("random array", rand_array)

rand_int_array = np.random.randint(0, 15, 5) # 5 random int from 0 to 15
print("5 random int", rand_int_array)
print("sum of random int", rand_int_array.sum())
print("min among random int", rand_int_array.min())
print("max among randmon int", rand_int_array.max())
print("mean of all random int", rand_int_array.mean())
print("variance of all random int", rand_int_array.var())
print("std deviation of all random int", rand_int_array.std())

rand_int_array_2 = np.random.randint(1, 15, 6)
rand_int_array_2 = rand_int_array_2.reshape(3,2)
print("random int in an array\n", rand_int_array_2)
print("random int in a matrix of 3x2\n", rand_int_array_2)
print("sum of row values in the matrix\n", rand_int_array_2.sum(axis=1))
print("sum of column values in the matrix\n", rand_int_array_2.sum(axis=0))