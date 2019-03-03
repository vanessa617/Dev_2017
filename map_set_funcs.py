#map(function, iterable, ...) - returns an iterator that applies function to every item of iterable, yeilding results  function - map() passes each item of the iterable to this function. iterable - iterable which is to be mapped. **you can pass more than one iterable to the map() function.

#set() - return a new set object. set is a built-in class

#The return value from map() (map object) then can be passed to functions like list() (to create a list), set() (to create a set) and so on.

#Example 1: How map() works?
def calculateSquare(n):
    return n*n

numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(result)

#converting map object to set
numbersSquare = set(result)
print(numbersSquare)

#Example 2: How to use lambda function with map()?
result = map(lambda x: x*x, numbers)
print(result)

#converting map object to set
numbersSquare = set(result)
print(numbersSquare)

#Example 3: Passing Multiple iterators to map() using lambda
num1 = [4,5,6]
num2 = [5,6,7]

result = map(lambda n1, n2: n1+n2, num1, num2)
print(list(result))