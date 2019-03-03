str1 = 'This'

#for i=0, j=len(s) - 1:

#Alt way 2: needs fixing
def reverse(text):
    text_list = list(text)
    str_len = len(text)
    j = str_len - 1
    for i in range(str_len/2):
        temp = text_list[i]
        text_list[i] = text_list[j]
        text_list[j] = temp
        j -= 1
    return "".join(text_list)
print reverse('This')

 