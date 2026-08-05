-Aggregate functions

--np.sum()

import numpy as np
b = np.array([50,60,70])
print(np.sum(b))

180

--np.maen(average)

import numpy as np
b = np.array([50,60,70,80,90,100])
print(np.mean(b))

75.0

--min and max

import numpy as np
b = np.array([50,60,70,80,90,100])
print(np.min(b))
print(np.max(b))

50
100

--np.median(middle value)

import numpy as np
b = np.array([50,60,80,90,100])
print(np.median(b))

80.0

--np.std

import numpy as np
b = np.array([50,60,70,80,90,100])
print(np.std(b))

17.07825127659933


--np.var()

import numpy as np
b = np.array([50,60,70,80,90,100])
print(np.var(b))

291.6666666666667

--axis parameter 2d

import numpy as np
a = np.array([[10,20,30,40,50],[1,2,3,4,5]])
print(np.sum(a,axis=0))
print(np.sum(a,axis=1))

--3d

import numpy as np
a = np.array([[[10,20,30],
               [40,50,60]]
              ,[[15,25,35],
                [45,55,65]]])
print(np.sum(a,axis = 0))
print(np.sum(a,axis = 1))
print(np.sum(a,axis = 2))


[[ 25  45  65]
 [ 85 105 125]]
[[ 50  70  90]
 [ 60  80 100]]
[[ 60 150]
 [ 75 165]]

--argmin and argmax (finding min value and max value indexing)

import numpy as np
a = np.array([2,3,67,99,45,33,78,94,])
print(np.argmin(a))
print(np.argmax(a))

0
3



