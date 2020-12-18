import numpy as np

arr = np.arange(0, 10)
arr + 5 # adds 5 to each element
arr * arr # operations value by value for the same index
print(1 / arr) # numpy allos dividing by 0 assigning nan or inf as value. Regular Python would throw an exception

np.sqrt(array) # square root of every value
np.sin(array) # sin of every value
np.log(array) # log of every value
# ..

arr.sum() # sums every value
arr.mean() # average
arr.var() # variance
arr.std() # standard deviation

arr2d = np.arange(0, 25).reshape(5, 5)
arr2d.sum() # sums all
arr2d.sum(axis = 0) # sums the colums (across rows)
arr2d.sum(axis = 1) # sums the rows (across columns)