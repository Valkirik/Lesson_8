# A function CamleCase

def came_case(strng: str) -> str:

    l = list(strng)
    new_l = [i if i != "_" and i != "-" and i != "." and i != "," else " " for i in l]

    new_str = str("".join(new_l))
    new_list = new_str.split()

    cap_every_word = list(map(lambda word: word.capitalize(), new_list))
    join_list = "".join(cap_every_word)

    return join_list

print(came_case("Hello, world"))