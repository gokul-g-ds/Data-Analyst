a = 10
b = 20
print(a,b)
a = a+b
b = a-b
a = a-b
print(a,b)

# with temp  varaible 

a = 10
b = 20
print(a,b)
temp = a
a = b
b = temp
print(a,b)

#10 20
#20 10


#in single line 

a = 10
b = 20
a,b = b,a
print(b,a)

#10 20

