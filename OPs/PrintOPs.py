import sys


# the total cost of the search algorithm
# the amount of nodes transversed
def print_total_cost(cost):
    print("\nTrip cost: ", cost)


# prints the shortest path taken
def print_shortest(path):
    print("\nShortest Path:\n")
    print(path, '\n')


# print all of the other paths that were taken
# these will not always include destination
def print_other_routes(lists):
    if not lists:
        print("There was only one path to the destination.\n")
    else:
        print("Other Routes:\n    ")
        print(lists)


# display all of the results found
def display_results(root, result, search):
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"      {search} Statistics: {root} to Bucharest ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print_total_cost(result[2])
    print_shortest(result[0])
    print_other_routes(result[1])
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# store to file
def store_results(root, result, search):
    OG_stdout = sys.stdout
    with open(f"{root}_{search}.txt", 'w') as f:
        sys.stdout = f
        display_results(root, result, search)
        sys.stdout = OG_stdout
