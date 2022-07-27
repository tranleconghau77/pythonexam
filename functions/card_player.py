
import random

from .list_cards import add_cards



def card_player():
    list_cards = add_cards()
    #House PC
    ##
    card_one = random.choice(list_cards)
    #Player
    card_two = random.choice(list_cards) 
    while card_two == card_one:
        card_two = random.choice(list_cards)
    
    return {"card_one" : card_one ,"card_two" : card_two}
