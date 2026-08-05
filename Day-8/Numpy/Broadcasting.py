-- Array Broadcasting 

import numpy as np
a = np.array([[1],
             [2],
             [3]])
b = np.array([10,20,30])
print(a + b)

[[11 21 31]
 [12 22 32]
 [13 23 33]]

--scalar broadcasting

import numpy as np
a = np.array([[1],
             [2],
             [3]])

print(a + 5)

[[6]
 [7]
 [8]]
 
--Incompatible Shape

import numpy as np
a = np.array([12,13,14])
b = np.array([10,20])

print(a + b)

ValueError: operands could not be broadcast together with shapes (3,) (2,) 

--shapes

import numpy as np
a = np.array([12,13,14])
b = np.array([10,20])
print(a.shape)
print(b.shape)


(3,)
(2,)

--np.newaxis

  import numpy as np
  a = np.array([12,13,14,15,16,17])
  print(a[3:,np.newaxis])
  
  [[15]
 [16]
 [17]]


  import numpy as np
  a = np.array([12,13,14,15,16,17])
  print(a[3:0:-1,np.newaxis])
  
  [[15]
 [14]
 [13]]






