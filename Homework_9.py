# A function CamleCase

"""def came_case(strng: str) -> str:

    l = list(strng)
    new_l = [i if i != "_" and i != "-" and i != "." and i != "," else " " for i in l]

    new_str = str("".join(new_l))
    new_list = new_str.split()

    cap_every_word = list(map(lambda word: word.capitalize(), new_list))
    join_list = "".join(cap_every_word)

    return join_list

print(came_case("Hello, world"))"""


from curses.ascii import isdigit

#"is2 Thi1s T4est 3a"  ->  "Thi1s is2 3a T4est"


a = "is2 Thi1s T4est 3a is6 Thi5s T7est 8a"
f = list(a)
l = []
for i in f:
    if isdigit(i):
        l.append(i)
print(l)
s = a.split()
print(s)
l.sort()
print(l)
print(l[0])
new = []


while len(new) < len(s)-1:
    for i in s:
        if str(l[0]) in i:
            l.remove(l[0])
            new.append(i)


for i in s:
    if i not in new:
        new.append(i)

print(new)
