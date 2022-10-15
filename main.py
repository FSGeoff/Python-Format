# This is a sample Python script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import re
import string
from collections import Counter


# Prints out all items and number of occurrences
def AllItems():
    my_dict = {}
    file = open("groceries.txt", "r")
    lines = file.readlines()
    for item in lines:
        item = item.strip()
        if item in my_dict:
            my_dict[item] = my_dict[item] + 1
        else:
            my_dict[item] = 1
    for item in my_dict:
        print(item, " ", my_dict[item])


# Retrieves specific item and number of purchases
def SpecificItems(v):
    my_dict = {}
    file = open("groceries.txt", "r")
    lines = file.readlines()
    for item in lines:
        item = item.strip()
        if item in my_dict:
            my_dict[item] = my_dict[item] + 1
        else:
            my_dict[item] = 1
    # return my_dict
    if v in my_dict:
        print('{} appeared on the list {} times'.format(v, my_dict[v]))
    else:
        print("Item", v, "not found")

    return


# Retrieves grocery list with graphical representation of number of items
def Histogram():
    my_dict = {}
    file = open("groceries.txt", "r")
    lines = file.readlines()
    for item in lines:
        item = item.strip()
        if item in my_dict:
            my_dict[item] = my_dict[item] + 1
        else:
            my_dict[item] = 1
    for item in my_dict:
        num = my_dict[item]
        symbol = "*" * num
        print('{:20s} {:20s}'.format(item, symbol))

    return


AllItems()
Histogram()
SpecificItems("Yams")
