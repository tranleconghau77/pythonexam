
import re
from object import house

from list_cards import add_cards

from object import reward

from card_player import card_player

from compare_value import compare_value

from player import player

add_cards()

print("===================INFORMATION====================")
def play():
    
    
    txt = "The rain in Spain1@"
    x = re.match("[^a-z]", txt)
    if x:
        print("YES! We have a match!")
    else:
        print("No match")

    go = True
    name_player = input("Type your name")

    user = player(name_player)
    user.set_points(user.get_points() - 25)

    while(go):
        
        card_player(user)
        print("player value",user.get_value())
        result = compare_value(user.get_value(), house ["value"])


        #Input your guess
        play_guess = input("Your guess")

        if (result == play_guess):
            print("CORRECT")
            print("YOUR POINT",user.get_points())

            option = input("Type to continue or stop ")
            global reward
            if option == 'c':
                reward*=2
                print("reward",reward)
            elif option == 's':
                reward*=2
                user.add_point(reward)
                print("YOUR POINT",user.get_points())
                return

        elif result != play_guess:
            print("INCORRECT")
            print("YOUR POINT",user.get_points())
            go = False

play()



