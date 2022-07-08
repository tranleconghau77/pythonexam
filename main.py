import random


player = {
    "name" : "",
    "value" : "",
    "guess" : ""
}
house = {
    "name" : "HAU server",
    "value" : ""
}
player_points = 60

list_cards = []

list_card_numbers = [2,3,4,5,6,7,8,9]

list_card_words = {
    "Jack" : 10,
    "Queen" : 11,
    "King" : 12,
    "Ace" : 13
}

list_card_joker = {
    "Black Joker" : 14,
    "Red Joker" : 15
}

list_type_card = ["Heart", "Diamond", "Club", "Spade"]


for i in list_card_numbers:
        for j in list_type_card:
            list_cards.append(str(i) + " " + j)

for k in list_card_words:
    for j in list_type_card:
            list_cards.append(k + " " + j)

for z in list_card_joker:
    list_cards.append(z)

for z in list_cards:
    print(z)

#House PC
house["value"] = random.choice(list_cards)
print(house["name"] + " card value " + house["value"])

#Player
player["name"] = input("Your name:")
player["value"] = random.choice(list_cards)
print(player["name"] + " card value " + player["value"])

player["guess"] = input("Your guess:")
print("Your guess",player["guess"])



