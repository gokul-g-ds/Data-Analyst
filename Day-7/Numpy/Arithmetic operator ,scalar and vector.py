--Arithmetic operator

import numpy as np
a = np.array([10,20,30,40,50])
b = np.array([1,2,3,4,5])
print(a+b)
print(a-b)
print(a*b)
print(a/b)

[11 22 33 44 55]
[ 9 18 27 36 45]
[ 10  40  90 160 250]
[10. 10. 10. 10. 10.]

--scalar operation

import numpy as np
a = np.array([10,20,30,40,50])
print(a +5)
print(a -4)
print(a *2)
print(a /5)

[15 25 35 45 55]
[ 6 16 26 36 46]
[ 20  40  60  80 100]
[ 2.  4.  6.  8. 10.]

--vector operations

import numpy as np
a = np.array([10,20,30,40,50])
b = np.array([12,13,14,15,16])
print(a+b)

[22 33 44 55 66]

--Element wise multiplication

import numpy as np
a = np.array([10,20,30,40,50])
b = np.array([12,13,14,15,16])
print(a*b)

[120 260 420 600 800]

--power operator 

import numpy as np
a = np.array([10,20,30,40,50])
b = np.array([12,13,14,15,16])
print(a**3)
print(b**2)

[  1000   8000  27000  64000 125000]
[144 169 196 225 256]

--floor division and modulus

import numpy as np
a = np.array([10,20,30,40,50])
b = np.array([12,13,14,15,16])
print(a//b)
print(a%b)


[0 1 2 2 3]
[10  7  2 10  2]

 
--universal function

import numpy as np
a = np.array([10,20,30,40,50])
b = np.array([12,13,14,15,16])
print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b))


[22 33 44 55 66]
[-2  7 16 25 34]
[120 260 420 600 800]


