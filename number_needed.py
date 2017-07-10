#def number_needed(a,b):
#    a = list(a)
#    b = list(b)
#    count = 0
#    for i in a:
#        if i not in b:
#            count += 1
#    for i in b:
#        if i not in a:
#            count += 1
#    return count
    
a = "cdec"
b =  "abc"

def number_needed(a,b):
    dict_temp_a = dict()
    for i in a:
        dict_temp_a[i] = dict_temp_a.get(i,0) + 1
    
    dict_temp_b = dict()
    for i in b:
        dict_temp_b[i] = dict_temp_b.get(i,0) + 1
    
    count = 0
    for k,v in dict_temp_a.items():
        if k in dict_temp_b:
            count += abs(v-dict_temp_b[k])
        else:
            count += v
    for k,v in dict_temp_b.items():
        if k not in dict_temp_a:
            count += v
            
    return count

print number_needed(a, b)
    
        
    