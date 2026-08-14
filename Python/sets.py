#sets

set1 = {1,2,3,4}
print(set1)
print(type(set1))

print("# add methods")
set1.add("hi")
print(set1)

print("# remove methods")
set1.remove(2)
print(set1)

print("# Clearing the set")
set1.clear()
print(set1)

print("# list converted into set")
lst = [3.12,3.24,3.36,3.48]
set2 = set(lst)
print(set2)

print("# union")
print(set1.union(set2))
print("# intersection")
print(set1.intersection(set2))

'''{1, 2, 3, 4}
<class 'set'>
# add methods
{1, 2, 3, 4, 'hi'}
# remove methods
{1, 3, 4, 'hi'}
# Clearing the set
set()
# list converted into set
{3.24, 3.36, 3.12, 3.48}
# union
{3.24, 3.36, 3.12, 3.48}
# intersection
set()

=== Code Execution Successful ==='''

