x = {'a': 'apple', 'b': "boy", 'c': 'cat'}
print x['a'] # output = apple
print x.get('a') # ouput = apple

#.has_key - checks whether the 'key' exists
print x.has_key('a')#output = True

print x.keys()#output= ['a', 'c', 'b']
print x.values()#output = ['apple', 'cat', 'boy']
print x.items()#output = [('a', 'apple'), ('c', 'cat'), ('b', 'boy')]
print x #output = {'a': 'apple', 'c': 'cat', 'b': 'boy'}

#create a dictionary from a list of tuples
c = [('a', 1), ('b', 2), ('c', 3)] #a list of tuples
c = dict(c)
print c #output = {'a': 1, 'c': 3, 'b': 2}