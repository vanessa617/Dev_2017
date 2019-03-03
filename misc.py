letters = ['x', 'y', 'z']
letters.insert(1,'w') #add w @ index 1
print letters #output = ['x', 'w', 'y', 'z']
print (letters[2]) #output = y

x = 5
y = x + 3
y = int(str(y) + '2')
print(y)#output = 82

spam = '7'
spam = spam + '0'
eggs = int(spam) + 3
print(float(eggs))

b = 'cde'

def number_needed(b):
    dict_temp_b = dict()
    
    for i in b:
        dict_temp_b[i] = dict_temp_b.get(i,0) + 1
    return dict_temp_b
        
print number_needed(b)

dict_temp_b1 = {'c': 1, 'd': 1, 'e': 1}

print abs(dict_temp_b1['c'])
