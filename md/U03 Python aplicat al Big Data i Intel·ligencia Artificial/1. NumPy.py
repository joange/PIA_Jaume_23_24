import numpy as np

# Introducció a NumPy
print(np.__version__)
list_1 = [True, "2", 3.0, 4]
print([type(item) for item in list_1])

# array([1, 4, 2, 5, 3])
np.array([1, 4, 2, 5, 3])

# array([3.14, 4.  , 2.  , 3.  ])
np.array([3.14, 4, 2, 3])

# array([1., 2., 3., 4.], dtype=float32)
np.array([1, 2, 3, 4], dtype='float32')

# array([[2, 3, 4],
#        [4, 5, 6],
#        [6, 7, 8]])
np.array([range(i, i + 3) for i in [2, 4, 6]])

#array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
np.zeros(10, dtype=int)

# array([[1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1.]])
np.ones((3, 5), dtype=float)

# array([[3., 3., 3., 3., 3.],
#       [3., 3., 3., 3., 3.],
#       [3., 3., 3., 3., 3.]])
np.full((3, 5), 3.)

# array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18])
np.arange(0, 20, 2)

# array([0.  , 0.25, 0.5 , 0.75, 1.  ])
np.linspace(0, 1, 5)

# array([[0.13718193, 0.00357101, 0.01323657],
#        [0.39090681, 0.21454034, 0.74277238],
#        [0.38737056, 0.96167256, 0.50637694]])
np.random.random((3, 3))

# matriu de 3x3 amb valors enters aleatòris
np.random.randint(0, 10, (3, 3))

mu, sigma = 0, 0.1
s = np.random.normal(mu, sigma, 10000)
import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(s, 100, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
            np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
      linewidth=2, color='r')
plt.show()

# Manipulació d'arrays
array_1 = np.random.randint(10, size=(3, 4, 5))  # Array de tres dimensions
print("número de dimensions: ", array_1.ndim)
print("forma:", array_1.shape)
print("tamany: ", array_1.size)

print("tipus de dades:", array_1.dtype)
print("tamany d'element:", array_1.itemsize, "bytes")
print("tamany total:", array_1.nbytes, "bytes")

# Accés
array = np.random.randint(10, size=6)
print(array)
print(array[3])
print(array[-2])

array = np.random.randint(10, size=(3, 4))
print(array)
print(array[2, 0])
print(array[2, -1])

array[0, 0] = 12
print(array)

array[0, 0] = 3.14159
print(array)

x2 = np.array([[12,  5,  2,  4],
    [ 7,  6,  8,  8],
    [ 1,  6,  7,  7]])

x2[:, 0]
x2[1, :]

x2_sub = x2[:2, :2]
x2_sub[0, 0] = 99
x2

x2_sub_copy = x2[:2, :2].copy()
x2_sub_copy[0, 0] = 42
x2
x2_sub_copy

grid = np.arange(1, 10).reshape(3, 3)
grid

x = np.array([1, 2, 3])
x
x.reshape((1, 3))


arrays = [np.random.rand(3, 4) for _ in range(10)]
arrays
np.stack(arrays, axis=2).shape