# Sam Lyons
# CIS-294
# 2/23/19
# Assignment 5

"""A program that returns values pertaining to a grocery store's stocks and prices
in order to calculate a bill."""

shopping_list = ["banana", "orange", "banana", "pear", "orange", "banana"]

stock = {  # dictionary containing the stock of the grocery items.

    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {  # dictionary containing the prices of the grocery items.

    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


# function that computes the bills of the total items in the shopping list.
def compute_bill(food):

    total = 0
    for item in food:
        if stock[item] > 0:
            total += prices[item]
            stock[item] -= 1
    return total


def main():  # main function with outputs.

    total = str(compute_bill(shopping_list))

    print("%s %s" % ("Grocery List: $", total))


main()
