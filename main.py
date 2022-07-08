from ast import arguments
import random

##Initialize variables

player_points = 60

player = {
    "name" : "PLAYER",
    "value" : "",
    "guess" : ""
}
house = {
    "name" : "HAU SERVER:",
    "value" : ""
}
player_points = 60

list_cards = []

list_card_numbers = {
    "Two" : 2,
    "Three" : 3,
    "Four" : 4,
    "Five" : 5,
    "Six" : 6,
    "Seven" : 7,
    "Eight" : 8,
    "Nine" : 9,
    "Ten" : 10,
    "Jack" : 11,
    "Queen" : 12,
    "King" : 13,
    "Ace" : 14
}


list_card_joker = {
    "Black Joker" : 15,
    "Red Joker" : 16
}

# list_type_card = ["Heart", "Diamond", "Club", "Spade"]
list_type_card = {
    "Heart" : 4,
    "Diamond" : 3,
    "Club" : 2,
    "Spade" : 1
}


def add_cards():
    for i in list_card_numbers:
        for j in list_type_card:
            list_cards.append(j + " " + str(i))

    for z in list_card_joker:
        list_cards.append(z)

add_cards()

#House PC
##
house["value"] = random.choice(list_cards)
print(house["name"] + " " + house["value"])

#Player
# player["name"] = input("Your name:").upper()
player_random_value = random.choice(list_cards) 
while player_random_value == house["value"]:
    player_random_value = random.choice(list_cards) 
    
player["value"] = player_random_value
    
print(player["name"] + ": " + player["value"])


def compare_value(player_name_card,house_name_card):
    print("compare value", player_name_card, house_name_card)
    if house_name_card in list_card_joker:
        house_value = list_card_joker[house_name_card]
    else:
        temp_house_value =house_name_card.split(" ")
        house_value = list_card_numbers[temp_house_value[1]]
    
    if player_name_card in list_card_joker:
        player_value = list_card_joker[player_name_card]
    else:
        temp_player_value =player_name_card.split(" ")
        player_value = list_card_numbers[temp_player_value[1]]

    if player_value > house_value:
        return "high"
    elif player_value == house_value:
        
        house_value = list_type_card[temp_house_value[0]]

        player_value = list_type_card[temp_player_value[0]]

        if player_value > house_value:
            return "high"
    return "low"


result = compare_value(player["value"], house["value"])
print("Result",result)

play_guess = input("Your guess")

if play_guess == result:
    switch arguments:
        case "stop":
            return player_points; 

