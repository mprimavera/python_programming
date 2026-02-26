from ascii_art import secret_auction_logo

# Welcome the user
print(secret_auction_logo)
print("Welcome to the secret auction program.")

# empty dictionary for adding bidders and their amount
bidders = {}

# variable for while loop termination
bidders_bidding = 'yes'
# add bidders
while bidders_bidding == 'yes':
    # get the next bidder's name
    name = input("What is your name?\n")
    # get the next bidder's bid
    bid = round(float(input("What's your bid?\n$")), 2)
    # add bidder and their name to the list
    bidders[name] = bid
    # ask whether there are more bidders
    bidders[name] = bid
    bidders_bidding = input("Are there any more bidders?\n").lower()
    # clear screen if there are more bidders
    if bidders_bidding == 'yes':
        # clear the screen with 100 blank lines
        print("\n" * 100)

# find the max bidder and max bid
max_bid = 0
for key in bidders:
    if bidders[key] > max_bid:
        max_bidder = key
        max_bid = bidders[key]

# check for multiple max bidders
max_keys = []
for bidder in bidders:
    if bidders[bidder] == max_bid:
        max_keys.append(bidder)

# print max bidders when there is a tie
if len(max_keys) > 1:
    # concatenate names from the list for printing
    max_bidders = max_keys[0]
    count = 1
    while count < len(max_keys):
        max_bidders += " and " + max_keys[count]
        count += 1
    # print the single max bidder and their bid to the screen
    print(f"{max_bidders} are the max bidders at ${max_bid}")
else:
    # print the single max bidder and their bid to the screen
    print(f"{max_bidder} has the highest bid of ${max_bid}.")
