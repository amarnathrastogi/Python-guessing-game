def Welcome():
    print("""
    __       __   _                                  
    \ \      / /__| | ___ ___  _ __ ___   ___   
     \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \          
      \ V  V /  __/ | (_| (_) | | | | | |  __/   ---->
       \_/\_/ \___|_|\___\___/|_| |_| |_|\___|
    """)

def Statements():
    print('1. You Choose Exact Number. (0_0)')
    print('2. Number Is Greater than....')
    print('3. Number Is Less than....')

def Greet():
    print("Yaas , I'm A Genius. (0_0)")
    print('Game_Over!')


Welcome()

print("\n------------------------------\n")

print('Choose A Number Between 1 To 25 , & I Want TO Try Guess That....')

start = 1
end = 25

while start <= end:

    mid = (start + end) // 2

    print('\nYeah, I think You Choose Number', mid)

    Statements()

    C = input('Enter your choice...').strip()

    if C == '1':
        Greet()
        break

    elif C == '2':
        start = mid + 1  

    elif C == '3':
        end = mid - 1

    else:
        print("Invalid Input")

else:
    print("You Cheated ....(0_0)")

print("\n-------------x---------------\n")