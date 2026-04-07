def Welcome():
    print("""
╔══════════════════════════════════════════════════╗
║                                                  ║
║        W E L C O M E   G E N I U S               ║
║                                                  ║
╚══════════════════════════════════════════════════╝
""")

def Statements():
    print("""
╔═══════════════════════════════════════╗
║   1. You Choose Exact Number. (0_0)   ║
║   2. Number Is Greater than....       ║
║   3. Number Is Less than....          ║
╚═══════════════════════════════════════╝
""")

def Greet():
    print("""
╔═══════════════════════════════╗
║   Yeas , I'm A Genius. (0_0)  ║
║   Game_Over !                 ║
╚═══════════════════════════════╝
""")


Welcome()

print("\n╔════════════════════════════════════════════════════════════════════════╗\n")

print('\tChoose A Number Between 1 To 25 , & I Want TO Try Guess That.....')

print("\n╚════════════════════════════════════════════════════════════════════════╝\n")

start = 1
end = 25

while start <= end:

    mid = (start + end) // 2

    print('\nYeah, I think You Choose Number - ', mid,'\n')

    Statements()

    print("\n╔══════════════════════════════════════════╗")
    C = input('     Enter your choice... ').strip()
    print("╚══════════════════════════════════════════╝\n")

    if C == '1':
        Greet()
        break

    elif C == '2':
        start = mid + 1

    elif C == '3':
        end = mid - 1

    else:
        print("Invalid Input , please try again...")

else:
    print("╔════════════════════════════════╗")
    print("     You Cheated ....(0_0)")
    print("╚════════════════════════════════╝")

print("\n╚═══════════════════════════════x═══════════════════════════════╝\n")
