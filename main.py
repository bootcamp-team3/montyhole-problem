import random

def switch_choice(first,car):
    remain =[d for d in [1,2,3] if d not in [first,car]]
    open_door = random.choice(remain)

    can_choice = [d for d in [1,2,3] if d not in [first,open_door]]
    second_choice = can_choice[0]

    return first, car, second_choice
