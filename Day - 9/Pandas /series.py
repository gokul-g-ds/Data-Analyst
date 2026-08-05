--series
--using list 

import pandas as pd
a = pd.Series([10,20,30])
print(a)

0    10
1    20
2    30
dtype: int64

--using tuple 

import pandas as pd
a = pd.Series((10,20,30))
print(a)

0    10
1    20
2    30
dtype: int64

--using Dictionary

import pandas as pd
a = pd.Series({
    "maths" : 85,
    "science" : 91,
    "tamil" : 99
})
print(a)

maths      85
science    91
tamil      99
dtype: int64

--custom index

import pandas as pd
a = pd.Series([100,200,300,400,500],
              index =  ["a","b","c","d","e"])
print(a)

a    100
b    200
c    300
d    400
e    500
dtype: int64

--Accessing values

import pandas as pd
a = pd.Series([100,200,300,400,500])
              
print(a[3])

400

--mathematical operation 

import pandas as pd
a = pd.Series([100,200,300,400,500])           
print(a + 3)
print(a * 2)
print(a / 3)

0    103
1    203
2    303
3    403
4    503
dtype: int64
0     200
1     400
2     600
3     800
4    1000
dtype: int64
0     33.333333
1     66.666667
2    100.000000
3    133.333333
4    166.666667
dtype: float64



