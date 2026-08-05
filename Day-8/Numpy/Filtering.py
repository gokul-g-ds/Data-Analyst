--Filtering 

import numpy as np
a =np.array([10,20,30,40,50])
print(a > 25)

[False False  True  True  True]

--Boolean mask 

import numpy as np
a =np.array([10,20,30,40,50])
mask = a > 23
print(a[mask])

[30 40 50]

--np.where 

import numpy as np
a =np.array([10,20,30,40,50])
print(np.where(a > 20))

(array([2, 3, 4]),)

import numpy as np
a =np.array([10,20,30,40,50])
print(np.where(a > 20,1,0))

[0 0 1 1 1]

import numpy as np
a =np.array([10,20,30,40,50])
print(np.where(a > 20,"pass","fail"))

['fail' 'fail' 'pass' 'pass' 'pass']

--multiple condition (using and And or)

import numpy as np
a =np.array([10,20,30,40,50])
print(a[(a > 20) & (a < 50)])
print(a[(a>10)|(a < 40)])

[30 40]
[10 20 30 40 50]

--nonzero

import numpy as np
a =np.array([10,0,20,0,30,0,40,0,50])
print(np.nonzero(a))

(array([0, 2, 4, 6, 8]),)

