#[start:end:stride] Where start describes where the slice starts (inclusive), end is where it ends (exclusive), and stride describes the space between items in the sliced list. For example, a stride of 2 would select every other item from the original list to place in the sliced list.

l = [i**2 for i in range (1, 11)]
print l

print l[2:9:2] #every other number between index 2 and index 9 

my_list = range(1,11)
print my_list[::2] #prints every other number in list.

#reversing a list
backwards = my_list[::-1]
print backwards

#traversing the list. A positive stride traverses from left to right. A negative stride traverses a list from right to  left.
to_one_hundred = range(101)
backwards_by_ten = to_one_hundred[::-10] #this returns the list reversed by 10's
print backwards_by_ten 

to_21 = range(1, 22) #creates a list from 1 - 21
print to_21
odds = to_21[::2] #returns only odd numbers
print odds
middle_third = to_21[7:14] #returns 8-14
print middle_third
