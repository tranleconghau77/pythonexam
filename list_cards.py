from object import list_card_numbers
from object import list_card_joker
from object import list_cards
from object import list_type_card

def add_cards():
    for i in list_card_numbers:
        for j in list_type_card:
            list_cards.append(j + " " + str(i))

    for z in list_card_joker:
        list_cards.append(z)
