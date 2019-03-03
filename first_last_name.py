def print_full_name(a, b):
    if len(str(a)) <= 10:
        a = str(a)
    if len(str(b)) <= 10:
        b = str(b)
    print("Hello %s %s! You just delved into python" % (a, b))
    
print print_full_name("Apple", "Dot")   
