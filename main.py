def check_result(switched_choice, initial_choice, car_door):
    stay_win = 0
    switched_win = 0
    if(initial_choice == car_door):
        stay_win = 1
    elif(switched_choice == car_door):
        switched_win=1
    return stay_win, switched_win
