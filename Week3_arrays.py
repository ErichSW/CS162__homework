import numpy as np

def array_generator():
    # Generate a 5x5 array filled with zeros
    random_array = np.random.randint(0, 99, size=(5, 5), dtype=int)
    this_item = random_array[2, 3]
    array_sum = np.sum(random_array)
    array_mean = np.mean(random_array, axis=1)
    array_max = np.max(random_array, axis=0)
    return random_array, this_item, array_sum, array_mean, array_max


array, item, sum, mean, max = array_generator()
print(array)
print()
print("Value at row 2, column 3:", item)
print("Sum of all elements in the array:", sum)
print("Mean of each row in the array:", mean)
print("Highest number in each column:", max)

