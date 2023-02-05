# CarGenerator
Generates a list of cars that can be used in Assignments for DTE-2511

This file can be used to auto generate vehicles into a dictionary, that is dumped into a file that can be used for the mandatory assignment.

To read the file use this line:

import pickle
with open('car_list.txt', 'rb') as fp:
    car_dict = pickle.load(fp)

Keywords: 
first key is the number for the next nested dictionary
brand   = get the brand and model name
year    = what year was it made
km      = milage on the car
price   = price
special = This is the special variabel for car, truck or SUV
type    = is it a Car, Truck or SUV