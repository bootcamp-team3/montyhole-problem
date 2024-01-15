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

def check_result(switched_choice, initial_choice, car_door):
    stay_win = 0
    switched_win = 0
    
    if(initial_choice == car_door):
        stay_win = 1
    elif(switched_choice == car_door):
        switched_win=1
        
    return stay_win, switched_win


if __name__=='__main__':
  stay, switch = 0, 0
  for _ in range(1000):
    car, first = picj_two_doors()
    first, car, second_choice = switch_choice(first, car)
    stay_win, switched_win = check_result(second_choice, first, car)
    
    stay += stay_win
    switch += switched_win
  
  print('바꿨을 때의 승률: {}'.format(switch/1000 * 100))
  print('안바궜을 떄의 승률: {}'.format(stay/1000 * 100))
