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

def in_a_row(strng: str) -> str:
    lst = list(a)
    l = [i for i in lst if isdigit(i)]

    lst_with_words = strng.split()
    l.sort()

    final_list = []
    while len(final_list) < len(lst_with_words) - 1:
        if str(l[0]) in i:
            l.remove(l[0])
            final_list.append(i)

    for i in lst_with_words:
        if i not in final_list:
            final_list.append(i)

    return final_list

print("is2 Thi1s T4est 3a is6 Thi5s T7est")





