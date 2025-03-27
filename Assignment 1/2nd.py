'''
Explain how Python handles type conversion between different data 
types, such as between integers and floats or between strings and 
lists. 
'''
# Python handles type conversion between different data types
# using built-in functions. Here are some examples:
a=1
print(a, type(a))
b=float(a)
print(b, type(b))

c=1.6
print(c, type(c))
d=int(c)
print(d, type(d))

e="RAHUL"
print(e, type(e))
f=list(e)
print(f, type(f))

g=[1,2,3,"Rahul"]
print(g, type(g))
h=str(g)
print(h, type(h))