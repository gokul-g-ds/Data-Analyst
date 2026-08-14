#Dictionary
Students = {"name":'Gokul',
            "age" : 20,
            "standard" : 12 }
numbers = {1:'one',2:'two',3:'three',4:'four',5:'five'}
print("# Single key")
print(numbers[1])
print("# All keys")
print(numbers)
print(Students)

#methods
print("# Get methods")
print(Students.get('age'))
print(numbers.get(2))

#for keys
print("# key methods")
print(Students.keys())
print(type(Students))
print(numbers.keys())

#for vlaue
print("# value method")
print(Students.values())
print(numbers.values())

#pop
print("# pop ")
print(Students.pop('age'))
print(numbers.popitem())

'''# Single key
one
# All keys
{1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
{'name': 'Gokul', 'age': 20, 'standard': 12}
# Get methods
20
two
# key methods
dict_keys(['name', 'age', 'standard'])
<class 'dict'>
dict_keys([1, 2, 3, 4, 5])
# value method
dict_values(['Gokul', 20, 12])
dict_values(['one', 'two', 'three', 'four', 'five'])
# pop 
20
(5, 'five')

=== Code Execution Successful ==='''
