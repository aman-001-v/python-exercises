# import antigravity
from decorators import timer
@timer
def func(num):
    num = list(num)
    num.append(69)
    return num

n = (5,4,3,2,1)
func(n)
# print(func(n))
# print(n)