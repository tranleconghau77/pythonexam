
import random
from object import house
from object import list_cards


def card_player(user):
    #House PC
    ##
    house["value"] = random.choice(list_cards)
    print(house["name"] + " " + house["value"])

    #Player
    player_random_value = random.choice(list_cards) 
    while player_random_value == house["value"]:
        player_random_value = random.choice(list_cards) 

    user.set_value(player_random_value)
    print("PLAYER NAME"+ ": " + str(user.get_name()))