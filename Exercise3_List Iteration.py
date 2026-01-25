
def print_factor2(x):
    print(f"\n{x}all factors：")
    for i in range(2, x):
        if x % i == 0:
            print(i)

l = [52633, 8137, 1024, 999]
for num in l:
    print_factor2(num)