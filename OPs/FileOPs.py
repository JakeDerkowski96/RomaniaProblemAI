import os
import shutil


# create and move into this dir??
def create_output_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    os.chdir(directory)


# delete directory ~~ for testing purposes
def delete_dir(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)
        print(os.getcwd())
    else:
        print("nudin\n")


# go back to output directory
def CD_results():
    os.chdir('..')

# folder where each search will be store separately
def create_city_dir(root):
    if not os.path.exists(root):
        os.makedirs(root)
    os.chdir(root)


# get data and store into local dictionary
def read_in_dict(filename):
    dict_graph = {}
    with open(filename, 'r') as f:
        for words in f:
            city_a, city_b, p_cost = words.split()
            if city_a not in dict_graph:
                dict_graph[city_a] = {}
            dict_graph[city_a][city_b] = int(p_cost)
            if city_b not in dict_graph:
                dict_graph[city_b] = {}
            dict_graph[city_b][city_a] = int(p_cost)
    return dict_graph


# print map representation, and write to file
def print_dictionary(dictionary):
    for key in dictionary.keys():
        print(key, '->', dictionary[key])
    print('\n')


# ask to print
def display_dict(dictionary):
    user_input = input("Display adjacent list represented by a dictionary(Y/n)?\n:  ")
    user_input = user_input.lower()
    while user_input != 'n' or 'y':
        if user_input == 'y' or user_input == 'Y':
            print('\n')
            print_dictionary(dictionary)
            break
        elif user_input == 'n' or user_input == 'N':
            break
        else:
            user_input = input("Please enter (y/n):\n:   ")


# export dictionary to file
def export_dictionary(dictionary):
    file = open("map_data.txt", "w")
    for key in dictionary.keys():
        line = f'{key} -> {dictionary[key]}\n'
        file.write(line)
    file.close()
    print("\nSaved in the 'Results' directory\n")
