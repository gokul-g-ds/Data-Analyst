#list methods 

lst_0 = [1,2,3,4,5,6]
lst_1 = [11,22,33,44,55,66]
lst_2 = [111,222,333,444,555,666]
lst_3 = ["hi","today","day",3]

#len of list
print("The length of list")
print(len(lst_0))
print(len(lst_3))

#Append
print("The element added at end of the list")
lst_0.append(7)
print(lst_0)

#Insert
print("The element inserting in between ")
lst_1.insert(3,"hi")
print(lst_1)

#extend
print("Entend the lst_2")
lst_2.extend(lst_3)
print(lst_2)

#count
print("Counting the element present in lst")
print(lst_2.count(222))

#max and min
#print(max(lst_1))
#print(min(lst_2))

#remove
lst_0.remove(3)
print(lst_0)

'''The length of list
6
4
The element added at end of the list
[1, 2, 3, 4, 5, 6, 7]
The element inserting in between 
[11, 22, 33, 'hi', 44, 55, 66]
Entend the lst_2
[111, 222, 333, 444, 555, 666, 'hi', 'today', 'day', 3]
Counting the element present in lst
1
[1, 2, 4, 5, 6, 7]

=== Code Execution Successful ==='''
