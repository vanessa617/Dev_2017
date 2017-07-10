ran_list = [1, 2, 3, 4, 5, 6, 7]
#print ran_list

def purify(num_list):
    new_list = []
    #print new_list
    for n in num_list:
        if n%2 == 0:
            new_list.append(n)
    return new_list
            
print purify(ran_list)
