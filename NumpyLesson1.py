import numpy as np

# array = np.array([1, 2, 3, 4])
# array*=2
# print(array)
# print(array.ndim)

# array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F']], 
#                   [['G', 'H', 'I'], ['M', 'N', 'P']]])
# print(array.ndim)
# print(array.shape) #blocks/layers-rows-columns
# print(array[0][0][0]) #chain indexing
# print(array[1,1,0]) #multidimentional indexing
# word = array[0,0,0] + array[1,1,1] + array[1,0,1]
# print(word)

array = np.array([[1,2,3,4], 
                  [5,6,7,8], 
                  [9,10,11,12], 
                  [13,14,15,16]])

#   array[start:end:step]
# print(array[::-2]) #rows selection
# print(array[:,1:4:2])
# print(array[:, ::-2])
print(array[0:2, 0:4])