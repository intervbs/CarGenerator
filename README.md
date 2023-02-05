# CarGenerator
Generates a list of cars that can be used in Assignments for DTE-2511

This file can be used to auto generate vehicles into a dictionary, that is dumped into a file that can be used for the mandatory assignment.

To read the file use this line:

import pickle
with open('car_list.txt', 'rb') as fp:
    car_dict = pickle.load(fp)