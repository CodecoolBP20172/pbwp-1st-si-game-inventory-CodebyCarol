# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification

import csv
import operator

# Displays the inventory.
def display_inventory(inventory):
    print("Inventory:")
    x=0
    for key in inventory:
        print (inventory[key], "", key)
        x=x+inventory[key]
        #SUM for cikluson belul
    print("Total number: ", x)

# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for key in added_items:
        if key in inventory:
            inventory[key]+=1
        else:
            inventory[key]=1
    return inventory

# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order

def print_table(inventory, order=None):
    max_length = len(max(inventory, key=len))
    fmt_str = '{:>7} {:>%s}' % (max_length+2)

    if order == None:
        sorted_inv = inventory.items()
    elif order == "count,desc":
        sorted_inv = sorted(inventory.items(), key = operator.itemgetter(1), reverse = True)
    elif order == "count,asc":
        sorted_inv = sorted(inventory.items(), key=operator.itemgetter(1))
    print("Inventory:")
    print(fmt_str.format("count", "item name"))
    print('-'*(7+max_length+3))

    for item in sorted_inv:
        print(fmt_str.format(item[1], item[0]))

    print('-'*(7+max_length+3))
    print("Total number: %s" % sum(inventory.values()))

# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            # using the already existing add_to_inventory def
            inventory = add_to_inventory(inventory, row)
    return inventory

# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    # transforming dict to list, where
    # {"A" => 2 "B" => 3}  A,A,B,B,B
    items = []
    for key in inventory:
        a = [key] * inventory[key]
        items.extend(a)
    # export to a csv file the transformed list
    with open(filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(items)
