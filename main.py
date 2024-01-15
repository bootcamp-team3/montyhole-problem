from random import randint

def pick_two_doors():
    doors = range(1, 4)
    no1 = randint(doors)
    no2 = randint(doors)

    return no1, no2