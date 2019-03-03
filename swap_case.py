def swap_case(s):
    s_list = list(s)
    
    for i in range(0,len(s_list)):
        if s_list[i].isalpha:
            if s_list[i].islower():
                #print ('is lower')
                s_list[i] = s_list[i].upper()
                #print ('s:',s_list)
            else:
                #print ('not lower')
                s_list[i] = s_list[i].lower()
                #print ('s:',s_list)
    return "".join(s_list)