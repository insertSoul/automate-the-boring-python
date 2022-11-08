from collections import Counter

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0 # item counter
    for k, v in inventory.items():   # loop trough inventory
        print(str(v) + ' ' + k )     # print the value a space and the item
        item_total += 1 * v          # add the items to the total
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addItems):
    #itemsDict = Counter(addItems) # turn items into dictionary (not needed)
    for i in addItems: # run through addItems (the loot obtained)
        inventory.setdefault(i, 0) #if an unkown item add to the inventory
        inventory[i] += 1 # add the item to the inventory
    return(inventory)

inv = {'gold coin': 42, 'rope': 1}
print("Starting inventory is :\n")
displayInventory(inv)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
print("\nFinal inventory is :\n")
displayInventory(inv)

#### MORE TESTING ##########

#inv2 = {'gold coin' : 12 , 'Axe' : 1 , 'helmet' : 2  , 'sword': 3 , 'magic frog' : 69}
#treasureChest = {'gold coin' , 'gold coin' ,'gold coin' ,'gold coin' ,'gold coin' ,'cape of destruction'}
#treasureChest2 = {  (('gold coin') )*10 ,'cape of destruction'}

#inv2 = addToInventory(inv2, treasureChest2)
#displayInventory(inv2)