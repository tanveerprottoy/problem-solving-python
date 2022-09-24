# Python Program to find the L.C.M. of two input number
# The Least Common Multiple
def compute_lcm(x, y):
    # choose the greater number
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1
    return lcm


# print(compute_lcm(3, 2))
