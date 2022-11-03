 #(2) loop through the code 10,000 times
    # generate a list of random coin tosses (heads of tails, H/T) 100
    # check through the list for streaks
    #find streaks that are over 6 and return
    # add number to counter
    #return the counter

#############   CODE THAT DID NOT WORK ##############

# import random
# numberOfStreaks = 0
# aStreak = 'HHHHHH'   or 'TTTTTT'
# searchList = ''
# flipList = []


# for experimentNumber in range(10000): # loop 10000 times
#     for flipListNumber in range(100): # create list of 100 flips
#         if random.randint(0, 1) ==1: # if 1 H
#             flipList.append('H')
#         else:
#             flipList.append('T') # is 0 T
# for i in range(len(flipList)): # make list search-abel
#     searchList += str(flipList[i])
# if aStreak in searchList:
#     numberOfStreaks += 1
# else:
#     numberOfStreaks += 0



# print(numberOfStreaks)
# print(numberOfStreaks / 10000 *100)
# print('Chance of streak: %s%%' % (numberOfStreaks / 100))

    # Code that checks if there is a streak of 6 heads or tails in a row.
#print('Chance of streak: %s%%' % (numberOfStreaks / 100))

 ######### CODE THAT DOES WORK!!!!!! #############

import random
numberOfStreaks = 0
searchList = ''
aStreak = 'TTTTTT' or 'HHHHHH' # has some issue so doesnt work (fixed thurther down)
flipList = []


for experimentNumber in range(10000): # loop 10000 times
    for flipListNumber in range(100): # create list of 100 flips
        if random.randint(0, 1) ==1: # if 1 add H
            flipList.append('H')
        else:
            flipList.append('T') # is 0  add T
    for i in range(len(flipList)): 
        searchList += str(flipList[i]) # make list search-abel by making single string
    if 'TTTTTT' in searchList: # if there is a Streak
        numberOfStreaks += 1
    elif 'HHHHHH' in searchList:
        numberOfStreaks += 1
    else:
        numberOfStreaks += 0
    searchList = '' #reset lists
    flipList = []


print(numberOfStreaks)
print(numberOfStreaks / 10000 *100)
print('Chance of streak: %s%%' % (numberOfStreaks / 100))


print(flipList)
print(searchList)
print(numberOfStreaks)

