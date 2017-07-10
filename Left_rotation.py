test_list = [1,2,3,4,5]
def left_rotation(n,d):
    d = d % len(n)
    return n[d:] + n[:d]

print left_rotation(test_list, -1)