#def censor(text, word):
    #chop_string = text.split(" ")
    #new_list = []
    #for i in chop_string:
        #if i == word:
            #i.replace(i, "*" * len(i))
        #return chop_string
        #new_list.append(i)
        
    #return " ".join(new_list)
        
#print censor("this is test", "this")  

#print censor ('this is that', 'this')
                      
                      
#it is not replacing 'this' with asterisks
def censor(text, word):
    chop_string = text.split(" ")
    new_list = []
    for i in chop_string:
        if i == word:
            new_list.append("*"*len(i))
        else:
            new_list.append(i)
    return " ".join(new_list)

print censor ('this is that', 'this')