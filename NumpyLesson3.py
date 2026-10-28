import numpy as np

#broadcasting
array1 = np.array([[1,2,3,4],
                   [5,6,7,8],
                   [9,10,11,12],
                   [13,14,15,16]])
array2 = np.array([[1], [2], [3], [4]])
print(array1.shape) #dimentions
print(array2.shape)
print(array1*array2)
print(array1 @ array2)

#aggregate functions
array = np.array([[1,2,3,4,5],
                  [6,7,8,9,10]])
# print(np.sum(array))
# print(np.mean(array))
# print(np.std(array))
# print(np.var(array))
# print(np.min(array))
# print(np.max(array))
# print(np.argmin(array))
# print(np.argmax(array))
print(np.sum(array, axis=1))

#filtering
ages = np.array([[21,17,19,20,16,30,18,65],
                 [39, 22, 15, 99, 18, 19, 20, 21]])
teenagers = ages[ages<18]
adults = np.where((ages >= 18) & (ages <65), ages, 0)
evens = ages[ages % 2 == 0]
print(teenagers)
print(adults)
print(evens)

#random numbers
rng = np.random.default_rng(seed = 1)
print(rng.integers(1,7))
print(rng.integers(low =1, high =101, size = (3,2))) #Integer numbers
print(np.random.uniform(low = 0.0, high = 100.0, size = 3)) #Real numbers
arraay = np.array([1,2,3,4,5])
rng1 = np.random.default_rng()
rng1.shuffle(arraay)
print(arraay)
fruits = np.array(["apple", "orange", "banana", "coconut", "pineapple"])
fruit = rng1.choice(fruits)
fruits = rng1.choice(fruits, size = 3)
print(fruit)
print(fruits)