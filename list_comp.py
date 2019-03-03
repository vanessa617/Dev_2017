#builds a list of number of even numbers from 1 to 50 
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50

#This will create a new_list populated by the numbers one to five and doubled numbers that are evenly divisible by three.
doubles_by_3 = [x*2 for x in range(1,6) if x % 3 == 0]
print doubles_by_3

#include the squares of the even numbers between 1 to 11. 
even_squares = [x**2 for x in range(1,12) if x % 2 == 0]
print even_squares

#The comprehension should consist of the cubes of the numbers 1 through 10 only if the cube is evenly divisible by four.
cubes_by_four = [x**3 for x in range(1, 11) if x % 4 == 0]
print cubes_by_four