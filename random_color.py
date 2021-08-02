from random import choice

def random_color():
    nbr_lettre = ['a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6']
    a = "".join(choice(nbr_lettre)for x in range(6))
    color = "#" + a
    return color