--csv file

from google.colab import files
uploaded = files.upload()

import pandas as pd
df = pd.read_csv("customers-100.csv")
print(df)
print(df.to_string)
print(df.head)
print(df.tail)

 
Untitled2.ipynb_
[37]
11s
[42]
0s

    Index      Customer Id First Name Last Name  \
0       1  DD37Cf93aecA6Dc     Sheryl    Baxter   
1       2  1Ef7b82A4CAAD10    Preston    Lozano   
2       3  6F94879bDAfE5a6        Roy     Berry   
3       4  5Cef8BFA16c5e3c      Linda     Olsen   
4       5  053d585Ab6b3159     Joanna    Bender   
..    ...              ...        ...       ...   
95     96  cb8E23e48d22Eae       Karl     Greer   
96     97  CeD220bdAaCfaDf       Lynn  Atkinson   
97     98  28CDbC0dFe4b1Db       Fred    Guerra   
98     99  c23d1D9EE8DEB0A     Yvonne    Farmer   
99    100  2354a0E336A91A1   Clarence    Haynes   

                            Company               City  \
0                   Rasmussen Group       East Leonard   
1                       Vega-Gentry  East Jimmychester   
2                     Murillo-Perry      Isabelborough   
3   Dominguez, Mcmillan and Donovan         Bensonview   
4          Martin, Lang and Andrade     West Priscilla   
..                              ...                ...   
95                        Carey LLC       East Richard   
96            Ware, Burns and Oneal       New Bradview   
97                    Schmitt-Jones         Ortegaland   
98               Fitzgerald-Harrell    Lake Elijahview   
99               Le, Nash and Cross          Judymouth   

                       Country                 Phone 1  \
0                        Chile            229.077.5154   
1                     Djibouti              5153435776   
2          Antigua and Barbuda         +1-539-402-0259   
3           Dominican Republic  001-808-617-6467x12895   
4   Slovakia (Slovak Republic)  001-234-203-0635x76146   
..                         ...                     ...   
95                      Guyana     (188)169-1674x58692   
96                   Sri Lanka         +1-846-706-2218   
97             Solomon Islands    +1-753-067-8419x7170   
98                       Aruba           (530)311-9786   
99                    Honduras           (753)813-6941   

                   Phone 2                           Email Subscription Date  \
0         397.884.0519x718        zunigavanessa@smith.info        2020-08-24   
1         686-620-1820x944                 vmata@colon.com        2021-04-23   
2      (496)978-3969x58947             beckycarr@hogan.com        2020-03-25   
3          +1-813-324-8756     stanleyblackwell@benson.org        2020-06-02   
4    001-199-446-3860x3486         colinalvarado@miles.net        2021-04-17   
..                     ...                             ...               ...   
95    001-841-293-3519x614                hhart@jensen.com        2022-01-30   
96            605.413.3198               vkemp@ferrell.com        2021-07-10   
97   +1-632-666-7507x92121                swagner@kane.org        2021-09-18   
98  001-869-452-0943x12424  mccarthystephen@horn-green.biz        2021-08-11   
99            783.639.1472          colleen91@faulkner.biz        2020-03-11   

                              Website  
0          http://www.stephenson.com/  
1               http://www.hobbs.com/  
2            http://www.lawrence.com/  
3          http://www.good-lyons.com/  
4         https://goodwin-ingram.com/  
..                                ...  
95            http://hayes-perez.com/  
96         https://novak-allison.com/  
97              https://www.ross.com/  
98               http://watkins.info/  
99  http://www.hatfield-saunders.net/  

[100 rows x 12 columns]


--JSON files

from google.colab import files
uploaded = files.upload()

import pandas as pd
df = pd.read_csv("customers-100.JSON")
print(df)
print(df.to_string)
print(df.head)
print(df.tail)


