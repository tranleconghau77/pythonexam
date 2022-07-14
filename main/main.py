
import re

from object import house

from list_cards import add_cards

from object import reward

from card_player import card_player

from compare_value import compare_value

from player import player


add_cards()

print("===================INFORMATION====================")
def main():
    login = False
    while(login == False):
        username = input("Type your username")
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

        if regex.search(username) == None and len(username)>5:
            print("String is accepted")
            user = player(username)
            login = True
        else:
            print("String is not accepted.")

    go = True
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

if __name__ == "__main__":
    main()



