

"""def unic_thing(lst_1: list, lst_2: list) -> list:
    c = [i for i in lst_1 if i not in lst_2]
    return f"{c}: the numbers that there are no in the second list"

print(unic_thing([1, 2, 3], [1, 2]))"""
from functools import reduce
from itertools import count

"""strng = "Hello world my name is Valery"

a = strng.split(" ")
print(a)
new_str = []

for i in a:
    if len(i) > 5:
        new_str.append(i[::-1])
    else:
        new_str.append(i)"""




"""def rev(strng: str) -> str:
    lst = strng.split(" ")
    new_lst = [i[::-1].capitalize() if len(i) > 5 else i for i in lst]

    j = " ".join(new_lst)
    return j


print(rev("Hello Valery how are you"))"""

"""def numb(lst: list) -> str:
    n = 0
    c = lst
    for i in lst:
        if count(i)  c:
            n += 1
    return n

print([1, 1, 2])
v = [1, 2, 2, 3]
print(v.count(2))
"""


"""a = 123432
c = list(str(a))
c.sort()
c.reverse()
n = int("".join(c))

print(n)"""

"""def the_biggest(num: int) -> int:
    lst_num = list(str(num))
    lst_num.sort()
    lst_num.reverse()
    final = int("".join(lst_num))
    return final

print(the_biggest(123))"""





"""def zero(lst: list) -> list:
    without_zero = list(filter(lambda x: x != 0, lst))
    z = lst.count(0)
    print(z)
    while z != 0:
        without_zero.append(0)
        z -= 1
    return without_zero



print(zero([1, 0, 4, 5, 7, 9, 3, 0, 3, 0, 0, 0, 0, 0, 2]))"""

def one_num(num: int) -> int:
    n = num
    while n > 9:
        lst = list(str(n))
        s = reduce(lambda x, y: int(x) + int(y), lst)
        n = s
    return n

print(one_num(942))












