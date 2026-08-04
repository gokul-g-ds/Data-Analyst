--1 dimension array 

import numpy as np
arr = np.array([10,20,30,40,50])
print(arr)
print(arr.shape)
print(arr.ndim)

[10 20 30 40 50]
(5,)
1


--2 dimensional array

import numpy as np
a = np.array ([[1,2,3],[4,5,6]])
print(a)
print(a.shape)
print(a.ndim)

[[1 2 3]
 [4 5 6]]
(2, 3)
2

-- 3 dimensional array

import numpy as np
a = np.array ([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(a)
print(a.shape)
print(a.ndim)

[[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]]
(2, 2, 3)
3

-- finding size of array

import numpy as np
a = np.array([[1,2,3],[4,5,6]])
print(a)
print(a.size)

[[1 2 3]
 [4 5 6]]
6

--reshape 

import numpy as np
a = np.array([[1,2,3],[4,5,6]])
b = a.reshape(1,6)
c = b.reshape(3,2)
print(a)
print(b)
print(c)

[[1 2 3]
 [4 5 6]]
[[1 2 3 4 5 6]]
[[1 2]
 [3 4]
 [5 6]]


--flatten()

import numpy as np
a = np.array([[[1,2,3],[4,5,6]],
              [[1,2,3],[1,2,3]]])

b = a.flatten()
print(b)

[1 2 3 4 5 6 1 2 3 1 2 3]


-- ravel

import numpy as np
a = np.array([[[1,2,3],[4,5,6]],
              [[1,2,3],[1,2,3]]])

b = a.ravel()
a[0,0,1] = 100
print(b)

[  1 100   3   4   5   6   1   2   3   1   2   3]



