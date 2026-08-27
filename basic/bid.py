def find_winner_and_price(bid_info):
    winner = {"winner": "winner", "max_price": 0}
    for k,v in bid_info.items():
        if v > winner["max_price"]:
            winner["winner"] = k
            winner["max_price"] = v
    print(f'The winner is {winner["winner"]}. Price is ${winner["max_price"]}')

def main():
    print("Welcome to tender. Please sumbit your bid.")
    more_bidder = True
    bid = {}
    while more_bidder:
        name = input("Please enter your name. ")
        price = int(input("Please submit your bid. $"))
        bid[name] = price
        should_continue = input('Are there any other bidder? Please enter "Yes" or "No" ').lower()
        if should_continue == "yes":
            print("\n"*100)
        else:
            find_winner_and_price(bid)
            more_bidder = False

if __name__ == '__main__':
    main()