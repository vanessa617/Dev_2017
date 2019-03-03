def gen_odd_number(count):
    for i in range(count):
        if i %2 != 0:
            yield i


for i in gen_odd_number(5):
    print 'x:',i**2
            