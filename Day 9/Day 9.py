logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\
                   
'''

print(logo)
bidders = {}
bidding = True
highest_bid = 0
while bidding:
    print("\n" *50)
    Name = input("Please Write your beautiful Name : ")
    bid = input("Enter your Bid : $")
    bidders[Name] = int(bid)
    members =  input("Is there are other users who want to bid Yes : No ").lower()
    if members == "no":
        bidding = False
        for amount in bidders:
            if bidders[amount] > highest_bid:
                highest_bid = bidders[amount]                
                winner = amount
        print(f"The Winner is {winner} and his Bid is ${highest_bid}.")        