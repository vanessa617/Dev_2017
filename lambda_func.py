#lambda is an annoymous function that allows you to pass a function as variable.
#syntax example - lambda x: x % 3 == 0
#filter is used in conjunction with lambda to determine what to filter.
my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list) # returns only numbers divisible by 3.

languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x == languages[2], languages)#returns index # 2.

cubes = [x**3 for x in range(1,11)] #cubes numbers between 1 -10
print filter(lambda  x: x % 3 == 0, cubes)#returns cubes divisible by 3

#a list of squares of numbers 1 - 10
squares = [x**2 for x in range (1,11)]
#print only squares #s 30 - 70
print filter(lambda x: x>=30 and x<=70, squares)