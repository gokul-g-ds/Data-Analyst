-- Array slicing

import numpy as np
a = np.array([100,200,300,400,500])
print(a[1:4])
print(a[3:4])
print(a[0:2])

[200 300 400]
[400]
[100 200]

--step slicing

import numpy as np
a = np.array([100,200,300,400,500])
print(a[1:4])
print(a[::2])
print(a[0:4:2])

[200 300 400]
[100 300 500]
[100 300]

--negative indexing 

import numpy as np
a = np.array([100,200,300,400,500])
print(a[::-1])
print(a[4:2:-1])

[500 400 300 200 100]
[500 400]

--2d array slicing

import numpy as np
a = np.array([[100,200,300,400,500],
              [12,13,14,15,16]])
print(a[0,2])
print(a[1,4])

300
16

--Row slicing

import numpy as np
a = np.array([[100,200,300,400,500],
              [12,13,14,15,16],
              [11,14,17,13,16]])
print(a[0:2])
print(a[1])
print(a[0:1])

[[100 200 300 400 500]
 [ 12  13  14  15  16]]
[12 13 14 15 16]
[[100 200 300 400 500]]

--Both row and column slicing

import numpy as np
a = np.array([[100,200,300,400,500],
              [12,13,14,15,16],
              [11,14,17,13,16]])
print(a[0:2,0:3])
print(a[1:2,3:])

[[100 200 300]
 [ 12  13  14]]
[[15 16]]

--Boolean indexing 

import numpy as np
a = np.array([[100,200,300,400,500],
              [12,13,14,15,16],
              [11,14,17,13,16]])
print(a > 14)

[[ True  True  True  True  True]
 [False False False  True  True]
 [False False  True False  True]]
 
 





