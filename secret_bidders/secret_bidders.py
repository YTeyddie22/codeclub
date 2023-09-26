bidder = {};
continue_bidding = True


def find_highest(record):
    highest_bid = 0
    winner = ""
    for bidder in record:
        amount = record[bidder]
        if amount > highest_bid:
            highest_bid = amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${amount}")    
    
while continue_bidding:
    bidder_name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidder[bidder_name] = bid
    ask_to_continue = input("Is there another bidder? Yes or No?")

    if ask_to_continue == "No".lower():
        continue_bidding = False
        find_highest(bidder)
        
        
