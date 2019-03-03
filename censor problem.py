def censor(text, word):
    list = text.split()
    for i in list:
        if i == word:
            i.replace(word, ("*" * len(word))
            return " ".join(list)
        
print censor("this is test", "this")
                      
                      
                      
