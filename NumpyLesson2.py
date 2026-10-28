import numpy as np

#Scalar arithmetic

array = np.array([1,2,3])

print(array+1)
print(array -2)
print(array*3)
print(array/4)
print(array**5)

#Vectorized math funcs
print(np.sqrt(array))
arrayhihi = np.array([1.01, 2.5, 3.99])
print(np.round(arrayhihi))
print(np.floor(arrayhihi)) #round down
print(np.ceil(arrayhihi)) #round up
print(np.pi)

#EXERRCISE
print(np.pi*array**2)

#Element-wise arithmetic
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])
print(array1+array2)
print(array1-array2)
print(array1*array2)
print(array1/array2)
print(array1**array2)

#Comparison operators
scores = np.array([91,55,100,73,82,64])
print(scores == 100)
print(scores< 70)
scores[scores<90] =0
print(scores)