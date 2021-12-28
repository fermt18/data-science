import numpy as np

arr = np.arange(0,11)
arr[8] # get the value at index 8
arr[1:5] # get an array from index 1 to 5
arr[:5] # get an array from index 0 to 5
arr[5:] # get an array from index 5 to end
arr[0:5] = 100 # assign 100 to first 5 postions
arr[:] = 100 # assign 100 to all postions
print(arr)

# all previous operations work with pointers and this affects original array arr even when saved to other variables
arr_copy = arr.copy() # hard copy of the array

arr_2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
arr_2d[0] # get first row
arr_2d[1,1] # get the row 1, column 1 element
arr_2d[:2] # get row 0 and 1 up to but no including index 2
arr_2d[:2,1:] # get row 0 and 1 up to but no including index 2, get columns from 1 to the end

arr = np.arange(1,11)
arr > 4 # where is arr greater than 4
bool_arr = arr > 4
arr[bool_arr] # array which locations coincide with bool_arr = True
arr[arr > 4] # same as above