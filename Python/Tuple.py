#creating tuple

lst = (111,222,333,444)
tup = (1,2,3,4)
print(type(tup))
print(tup)
print("Tuple is created")

#max and min 
print("max value is")
print(max(tup))
print("min value is")
print(min(tup))

#count 
print("counts in tup")
print(tup.count(3))

#index
print("index of 2")
print(tup.index(4))

#converting

'''print("tuple converted into list"))
lst = list(tup)
print(type(lst))
print(lst)'''

print("list converted into tuple")
tup = tuple(lst)
print(type(tup))
print(tup)

#output

'''<class 'tuple'>
(1, 2, 3, 4)
Tuple is created
max value is
4
min value is
1
counts in tup
1
index of 2
3
list converted into tuple
<class 'tuple'>
(111, 222, 333, 444)

=== Code Execution Successful ==='''
