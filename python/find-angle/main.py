from math import atan


def angle(y, x):
    return round(atan(y / x) * 57.296)


y = int(input())
x = int(input())

print('{}\u00b0'.format(angle(y, x)))
