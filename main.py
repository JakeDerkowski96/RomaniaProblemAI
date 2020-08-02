#!/bin/bash/python3

from OPs import *
from SearchRomania import *


def main():
    in_file = "misc/data.txt"
    res_dir = "Results"
    goal = 'Bucharest'

    # get map information and store it into dictionary
    city_map = read_in_dict(in_file)

    # create dir to save results in
    create_output_dir(res_dir)

    # ask to print dict to screen
    display_dict(city_map)

    # export map data to file
    export_dictionary(city_map)

    # get user input that is valid
    root = verify_city_input(city_map)

    # create directory for city
    create_city_dir(root)

    Status = True
    while Status:
        decision = search_menu()  # print menu

        if decision == 1:
            # for displaying data
            search = 'Breadth-First_Search'
            # search is performed
            res = BFSearch(city_map, root, goal)
            #results printed to screen
            display_results(root, res, search)
            # results saved in their individual file/city folder
            store_results(root, res, search)
            # contine on with more/different searches?
            Status = continuation()

        elif decision == 2:
            search = 'Depth-First_Search'
            res = DFSearch(city_map, root, goal)
            display_results(root, res, search)
            store_results(root, res, search)
            Status = continuation()

        elif decision == 3:
            search = 'Iterative-Deepening_Search'
            res = IDSearch(city_map, root, goal)
            display_results(root, res, search)
            store_results(root, res, search)
            Status = continuation()

        elif decision == 4:  # new city
            CD_results()
            root = verify_city_input(city_map)
            create_city_dir(root)
            continue

        elif decision == 5:
            ExitRomania()
            Status = False

        else:
            printErrMsg()
            print('\n')
            sleep(1)
            decision = search_menu()

if __name__ == '__main__':
    main()
