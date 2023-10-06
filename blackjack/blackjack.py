############### Blackjack Project #####################
import random;
#Get random cards
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# Calculate the score of cards 
def cal_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def compare(user,comp):
    if user == comp:
        return "Draw";
    elif comp == 0:
        return "Lose, Opponent has Blackjack"
    elif user == 0:
        return "Won with a Blackjack"
    elif user > 21:
        return "Lose, You went over"
    elif comp > 21:
        return "Won, Opponent went over"
    elif user > comp:
        return "You win"
    else:
        return "You lose"

## Append two random numbers to both the user and computer
def play_game():
    user_cards = []
    comp_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())

    # Continue deal if user decides the game to continue
    while not is_game_over:
        user_score = cal_score(user_cards)
        comp_score = cal_score(comp_cards)

        print(f"Your Cards are: {user_cards } and the score is {user_score}")   
        print(f"The Computer's card is {comp_cards[0]}") 
        
        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_continue_deal =  input("Type 'y' to pick another card, type n to end the game: ")
            if user_continue_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    # Check the comp score is < 17
    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_card())
        comp_score = cal_score(comp_cards)
        
    print(f"The computer cards are {comp_cards}")
    print(compare(user_score, comp_score))  


    

while input("Do you want to play a game of Blackjack? 'y' or 'n ") == 'y':
    play_game()