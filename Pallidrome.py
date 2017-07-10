def pallidrome (sent_1, sent_2):
    new_sent1 = sent_1.lower()
    new_sent2 = sent_2.lower()
    list_sent1 = list(new_sent1)
    list_sent2 = list(new_sent2)
    if list_sent1 == list_sent2:
        return True
    else:
        return False
print pallidrome("Race car", "racE Car")