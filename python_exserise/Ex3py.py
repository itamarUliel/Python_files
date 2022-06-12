import sys
sys.setrecursionlimit(2147483647)


def add(a, b):
    if a == 0 and b == 1:
        return 0
    else:
        if a != 0:
            result = add(a - 1, b)
            return result + 1
        if b != a and a == 0:
            result = add(a, b - 1)
            return result + 1


# print(add(8,5))
def mult(num, num_mul):
    if num_mul == 1:
        return num
    else:
        result = add(num, mult(num,num_mul-1))
        return result


# print(mult(5,4))
def atz(num):
    if num == 0:
        return 1
    else:
        return mult(num,atz(num - 1))


n2 = 7
print(atz(n2))

