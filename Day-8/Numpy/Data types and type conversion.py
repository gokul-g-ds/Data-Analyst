import numpy as np
array = np.array([128,456,789,234,678],dtype = np.int8)
print(array)
print(array.dtype)
print(array.nbytes)

---------------------------------------------------------------------------

OverflowError                             Traceback (most recent call last)

/tmp/ipykernel_1782/116107066.py in <cell line: 0>()
      1 import numpy as np
----> 2 array = np.array([128,456,789,234,678],dtype = np.int8)
      3 print(array)
      4 print(array.dtype)
      5 print(array.nbytes)

OverflowError: Python integer 128 out of bounds for int8

import numpy as np
array = np.array([128,456,789,234,678],dtype = np.int16)
print(array)
print(array.dtype)
print(array.nbytes)

[128 456 789 234 678]
int16
10

--float 

import numpy as np
array = np.array([1.2,3.4,5.6,7.8,9.1],dtype = np.float16)
print(array)
print(array.dtype)
print(array.nbytes)

[1.2 3.4 5.6 7.8 9.1]
float16
10


--str(without using "" and using dtype)

import numpy as np
array = np.array([1.2,3.4,5.6,7.8,9.1],dtype = np.str_)
print(array)
print(array.dtype)
print(array.nbytes)

['1.2' '3.4' '5.6' '7.8' '9.1']
<U3
60 #


--str (using "" and without using dtype)

import numpy as np
array = np.array(["goku","is","learning","numpy"])
print(array)
print(array.dtype)
print(array.nbytes)

['goku' 'is' 'learning' 'numpy']
<U8
128

--str using <u(n)

import numpy as np
array = np.array(["goku","is","learning","numpy"],dtype = "<U3")
print(array)
print(array.dtype)
print(array.nbytes)

['gok' 'is' 'lea' 'num']
<U3
48

--type coversion

import numpy as np
array = np.array([1,2,3,4,5,6,7],dtype = np.int8)
print(array)
print(array.dtype)
print(array.nbytes)
array = array.astype(np.str_)
print(array)
print(array.dtype)
print(array.nbytes)

[1 2 3 4 5 6 7]
int8
7
['1' '2' '3' '4' '5' '6' '7']
<U4
112

--converting into boolean 

import numpy as np
array = np.array([1,2,3,4,5,6,7],dtype = np.int8)
print(array)
print(array.dtype)
print(array.nbytes)
array = array.astype(np.bool_)
print(array)
print(array.dtype)
print(array.nbytes)

[1 2 3 4 5 6 7]
int8
7
[ True  True  True  True  True  True  True]
bool
7

--astype()

import numpy as np
arr = np.array([10,20,30,40,50])
arr = arr.astype(np.str_)
print(arr)
print(arr.dtype)
print(arr.nbytes)

['10' '20' '30' '40' '50']
<U21
420
