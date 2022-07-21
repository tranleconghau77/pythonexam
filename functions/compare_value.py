from .object import list_card_joker
from .object import list_card_numbers
from .object import list_type_card

#check proprerties exist in dict. Can use dict.get(property) Watch part 6 of the video here: https://www.youtube.com/watch?v=8OKTAedgFYg
def compare_value(player_name_card,house_name_card):
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