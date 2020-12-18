# https://numpy.org/doc/stable/
import numpy as np

mylist = [1,2,3]
myarray = np.array(mylist)

my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(my_matrix)
my_array = np.array(my_matrix)
print(my_array)

np.arange(0, 10, 2) # creates array 0 to 9 in steps of 2
np.zeros(5) # array with 5 zeros
np.zeros((2,5)) # array with 2 rows of 5 zeros each

np.linspace(0, 10, 11) # evenly spaced array from 0 to 10 with 11 numbers (includes 0 and 10)

np.eye(5) # identity matrix: matrix 5x5 with zeros and ones in the diagonal

np.random.rand(1) # array with 1 number with random uniform distribution over [0, 1)
np.random.rand(5, 6) # matrix 5 rows, 6 columns with random uniform distribution over [0, 1)

np.random.randn(10) # array with 10 numbers according to standard normal distribution

np.random.randint(0, 101, 5) # 5 random integers between 0 and 101
np.random.randint(0, 101, (4,5)) # 4 by 5 matrix with random integers between 0 and 101

np.random.seed(42) # predefining the seed we can reproduce random numbers
print(np.random.rand(4))
print(np.random.rand(4))

arr = np.arange(0, 25)
arr.shape
arr.reshape(5,5) # reshapes previous array into a 5 by 5 matrix (still 25 numbers)
arr.shape

ranarr = np.random.randint(0, 101, 10)
ranarr.max() # get the max number
ranarr.min()
ranarr.argmax() # get the index of the max number
ranarr.argmin()
ranarr.dtype # precission of the number (data type)
