#normal method 
arr = [ 1,2,3,4,5,6]
odd =[]

for i in arr:
    if i%2 == 0:
      odd.append(i)
print(odd)   

#list comperhension

odd = [i for i in arr if i%2 == 0]
print(odd)

'''[2, 4, 6]
[2, 4, 6]

=== Code Execution Successful ==='''
