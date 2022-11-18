from card import card
from user import user
import utils as utils

def initial_game(user_number):
    card_ = card()
    card_.initial_card()
    user_ = user(user_number)
    user_.initial_user()
    return card_, user_

def find_dice_queal_card(cards_ontop, dice):
    cards = []
    for index, card_ontop in enumerate(cards_ontop):
        if card_ontop[0] == dice:
            # choose to draw card or throw card
            cards.append([index]+card_ontop)
    return cards

def get_cin():
    return input()

def put_cout(msg):
    print(msg)

def check_winner(user_data):
    winner, point, num = "", 0, 0
    for key in user_data:
        if user_data[key][0] > point:
            winner, point, num = key, user_data[key][0], user_data[key][2]
        elif user_data[key][0] == point:
            if user_data[key][2] > num:
                winner, num = key, user_data[key][2]
            elif  user_data[key][2] == num:
                winner += " " + key
    return winner

def run_game(card_, user_): 
    n = 0
    while(len(user_.user_names) > 1 and len(card_.card_ontop) > 0):
        for user_name in user_.user_names:
            if (len(user_.user_names) <= 1 and len(card_.card_ontop) <= 0):
                break
            dice = utils.row_number(1, 6)
            cards = find_dice_queal_card(card_.card_ontop, dice)
            # show ontop_card==dice
            if cards:
                put_cout(str(user_name) + " turn")
                index_list, index = {}, 0
                for i, key, _ in cards:
                    index_list[i+1] = index
                    put_cout(str(i+1) + ": " + str(key))
                    index += 1

                # cin >> choose
                choose = int(get_cin())
                if -choose in index_list:
                    n = index_list[-choose]
                elif choose in index_list and cards[index_list[choose]][2] == 1:
                    n = index_list[choose]
                    user_.user[user_name][1] += 1
                    if user_.user[user_name][1] >= 3:
                        user_.user_names.remove(user_name)
                else:
                    n = index_list[choose]
                    user_.user[user_name][0] += cards[index_list[choose]][1]
                    user_.user[user_name][2] += 1
                card_.card_ontop.pop(n)
                card_.draw_card(1)
            put_cout(n)
            put_cout(user_.user)
            
    if len(user_.user_names) > 1:
        check_winner(user_.user)
    put_cout("winner is: " + str(user_.user_names[0]))

def run(user_number):
    card_, user_ = initial_game(user_number)
    run_game(card_, user_ )

if __name__ == "__main__":
    # select user number
    user_number = 5
    run(user_number)