--DataFrame 

import pandas as pd

data = {
    'name': ['gokul', 'unknown1', 'unknown2'],
    'age': [24, 24, 24],
    'city': ['erode', 'salem', 'tirupur']
}

df = pd.DataFrame(data)

print(df)

       name  age     city
0     gokul   24    erode
1  unknown1   24    salem
2  unknown2   24  tirupur

--create dataframe list by list

import pandas as pd

data = [['gokul', 24],
        ['unknown' , 24]
]
df = pd.DataFrame(data,columns = ("name","age"))
print(df)

      name  age
0    gokul   24
1  unknown   24

-- All attributes

import pandas as pd

data = [['gokul', 24],
        ['unknown' , 24]
]
df = pd.DataFrame(data,columns = ("name","age"))
print(df)
print(df.shape)
print(df.dtypes)
print(df.size)
print(df.ndim)

      name  age
0    gokul   24
1  unknown   24
(2, 2)
name    object
age      int64
dtype: object
4
2





