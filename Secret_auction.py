# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
dictionary ={}
def my_function():
    name = input("What is your name?: \n")
    bid = int(input("What is your bid?:\n$"))
    dictionary[name] = bid
    print(dictionary)

print(logo)

next_available = True
while next_available ==True:
    my_function()
    is_next_there = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if is_next_there == "no":
        next_available= False
        highest_bid = 0
        winner =""
        for name,bid in dictionary.items():   #for key in dictionary: → only gives keys
            if bid>highest_bid:               #for key, value in dictionary.items(): → gives both key and value
                highest_bid=bid
                winner = name

        print(f"The winner is:{winner}, with a bid of ${highest_bid}")
    else:
        print("\n" * 20)














