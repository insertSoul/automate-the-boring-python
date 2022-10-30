def collatz(number):
    if number == 1:
        print( 'collatzs complete')
        restartCollatz()

    elif number % 2 == 0: # if even
        print (number // 2)
        collatz(number // 2)
    else:
        print (3 * number + 1) # if odd
        collatz(3* number +1)


def restartCollatz():
    print ( 'Do you want to choose another number?')
    print (' Y / N ')
    yesOrNo = str(input())
    if yesOrNo == 'Y':
        print('Type an interger in for Collatzs sequence')
        collatz(int(input()))
    else:
        print ( 'Thank you for using' )



print('Type an interger in for Collatzs sequence')

try:
    collatz(int(input()))
except ValueError:
    print( 'That wasnt an Interger was it?')
    print( 'Try again' )
    collatz(int(input()))
