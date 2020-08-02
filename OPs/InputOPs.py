import sys, time


# get the city from the user
def get_source_city():
    root = input("Source city:  ")
    root = root.capitalize()
    return root

# get another input from user
def GetNewInput():
    answer = input("\nInvalid Entry. Please try again.\n:  ")
    return answer

# idk im liking function rn
def printErrMsg():
    print("\nInvalid Entry. Please try again.")

# check to see if it is a romanian city
def is_city(root, dictionary):
    state = False
    for key in dictionary.keys():
        if root == key:
            state = True
            print(f"\nLet us begin the trip from {root} to Bucharest!\n")
    return state

# just puts all of the about into one easy function
def verify_city_input(data):
    count = 0
    user_inp = get_source_city()
    state = is_city(user_inp, data)
    while state is False:
        printErrMsg()
        user_inp = get_source_city()
        state = is_city(user_inp, data)
    return user_inp

# prints main menu
def search_menu():
    options = [1, 2, 3, 4, 5]
    count = 0
    print("""
    What would you like to do?

    1. Breadth-First Search (BFS)
    2. Depth-First Search (DFS)
    3. Iterative-Deepening Search (IDS)
    4. Enter new source city
    5. Exit\n""")

    answer = input(':  ')
    answer = int(answer)
    while answer not in options:
        count += 1
        answer = input('\n:')
        answer = int(answer)
        if count % 3 == 0:
            search_menu()
    return answer

# user picks what to do
def validate_action(input):
    count = 0
    t = 0
    while input not in range(1,6):
        count += 1
        i += 1
        print(i)
        input = GetNewInput()
        input = int(input)
        if count % 3 == 0:
            printErrMsg()
            search_menu()
        return input


# see if user wants to continue with different search/city
def continuation():
    count = 0
    VI = ['y', 'n', 'Y', 'N']

    ans = input("\nWould you like to continue? (Y/n)\n:  ")
    ans = ans.lower()

    Kontinue = True
    while Kontinue:
        count += 1
        if ans not in VI:
            ans = GetNewInput()
            ans = ans.lower()
            print(ans)
            if count == 3:
                continuation()
        elif ans == 'y':
            break
            # ans = search_menu()
        elif ans == 'n':
            Kontinue = False
            ExitRomania()
    return Kontinue

 # when user quits prgram
def ExitRomania():
    print("Thank you for using this program!\n")
    time.sleep(1)
    print("You can find all results in the 'Results' directory\n")
    time.sleep(1)
    sys.exit("Exiting...")
