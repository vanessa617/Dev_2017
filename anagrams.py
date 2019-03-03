a = 'cde'
b = 'abc'

def number_needed(a,b):
    dict_temp_a = dict()
    
    for i in a:
        dict_temp_a[i] = dict_temp_a.get(i,0) + 1 #adds the value of 1
    
    dict_temp_b = dict()
    
    for i in b:
        dict_temp_b[i] = dict_temp_b.get(i,0) + 1 #adds the value of 1
    
    count = 0
    for k,v in dict_temp_a.items():
        if k in dict_temp_b:
            count += abs(v-dict_temp_b[k])#???
        else:
            count += v #adds 1 to the total count
    for k,v in dict_temp_b.items():
        if k not in dict_temp_a:
            count += v
            
    return count



print(number_needed(a, b))

