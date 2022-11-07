stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0 # item countter
    for k, v in inventory.items():   # loop trough inventory
        print(str(v) + ' ' + k )     # print the value a space and the item
        item_total += 1 * v          # add the items to the total
    print("Total number of items: " + str(item_total))

displayInventory(stuff)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
#Loot comes in a list, needs turning into dict. to add it in

