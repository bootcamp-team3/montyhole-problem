import random
from random import randint


def pick_two_doors():
    no1 = randint(1,4)
    no2 = randint(1,4)

    return no1, no2
  
def switch_choice(first,car, switch=True):
    remain =[d for d in [1,2,3] if d not in [first,car]]
    open_door = random.choice(remain)
    
    if switch:
        can_choice = [d for d in [1,2,3] if d not in [first,open_door]]
        second_choice = can_choice[0]
    else:
        second_choice = first

    return first, car, second_choice

def check_result(choice, car_door):
    win = 0
    
    if(choice == car_door):
        win=1
        
    return win


if __name__=='__main__':
  stay, switch = 0, 0
  num = 1000000  
  for _ in range(num):
    car, first = pick_two_doors()
    first, car, second_choice = switch_choice(first, car, True)
    win = check_result(second_choice, car)
    
    switch += win
  
  print('바꿨을 때의 승리: {}, 패배: {}, 승률: {}'.format(switch, num - switch, switch/num * 100 ))
  
  for _ in range(num): 
    car, first = pick_two_doors()
    first, car, second_choice = switch_choice(first, car, False)
    win = check_result(second_choice, car)
    
    stay += win
  print('안바궜을 때의 승리: {}, 패배: {},  승률: {}'.format(stay, num - stay, stay/num * 100))
