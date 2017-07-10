def Find_Longest_Word(sent):
    new_sent = sent.split(" ")
    return max(new_sent, key=len)
    

print Find_Longest_Word ("You have to be kidding me")
