#creating a tuple
t1 = ('a','b','c')
print type(t1)

#create an empty tuple
t2 = ()
print t2
print type(t2)

#you have to use a comma even if the tuple has one element
t2 = (1,)
print t2

#getting the first element
print t1[0] #output = a

#getting the last element
print t1[-1] #output = c

#getting elements using slicing
print t1[1:3] #output = ('b', 'c') - returns the second and third elements

a = (1,2,3,4,5)
print type(a)

#replace the first element with (10, ), and reassign result to a new tuple
b = (10,) + a[1:]
print b