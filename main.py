import random
from random import randint


def pick_two_doors():
    doors = range(1, 4)
    no1 = randint(doors)
    no2 = randint(doors)

    return no1, no2
  
def switch_choice(first,car):
    remain =[d for d in [1,2,3] if d not in [first,car]]
    open_door = random.choice(remain)

    can_choice = [d for d in [1,2,3] if d not in [first,open_door]]
    second_choice = can_choice[0]

    return first, car, second_choice



