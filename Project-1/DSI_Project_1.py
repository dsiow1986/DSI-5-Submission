# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 11:31:44 2018

@author: dsiow
"""

import os
from pprint import pprint

os.chdir('C:\\Users\\dsiow\\OneDrive\\GA - Data Science Immersive\\project-1')

pokedex_file = 'pokedex_basic.csv'
with open(pokedex_file, 'r') as f:
    raw_pd = f.read()
    
clean1 = raw_pd.splitlines()
clean1 = clean1[:4]

# Splitting the words/numbers in each string inside clean1 by the commas
# The resulting list (clean1_split) is a list of lists, with each element in the internal list is a word/number in string format
clean1_split = [row.split(",") for row in clean1]

# Removing all the double-quotes for each word/number in the internal list
clean1_replace = [[item.replace('"', '') for item in row] for row in clean1_split]

# Converting numerical column values to floats
clean1_float = []

for row in clean1_replace:
    temp_list = []
    for item in row:
        try:
            float(item)
        except:
            temp_list.append(item)
        else:
            temp_list.append(float(item))
            
    clean1_float.append(temp_list)
    
print(clean1_float)


clean1_patch_missing = []

for row in clean1_float:
    temp_list = []
    for item in row:
        if item == '':
            item = -1
            temp_list.append(item)
        else:
            temp_list.append(item)
    
    clean1_patch_missing.append(temp_list)


clean1_patch_missing = [[-1 if item == '' else item for item in row] for row in clean1_float]

print(clean1_patch_missing)


# Removing the 'Total' attribute from clean1_patch_missing, as it is not required in the pokedex

#for each_list in clean1_patch_missing:
#    del each_list[3]
pokedex_list = []

for each_list in clean1_patch_missing:
        pokedex_list.append([each_list[0],each_list[1],each_list[2],each_list[4],each_list[5],each_list[6],each_list[7],each_list[8],each_list[9]]) 
        
header = clean1_patch_missing[0]
data = clean1_patch_missing[1:]


pokedex = {}

for i in range(len(data)):
    
    pokedex[data[i][0]] = dict(zip(header[1:], data[i][1:]))

pprint(pokedex)

import numpy as np

total_list = []

# looping through each pokemon's total score - pokedex_function(clean1_patch_missing)[i]['total'] is the total score for each pokemon
for i in range(1,len(pokedex)+1):
    total_list.append(pokedex[i]['Total'])

total_array = np.array(total_list)

population_mean = total_array.mean()
population_std = np.std(total_array)

print('The population mean of the total attribute is {}'.format(population_mean))
print('The population standard deviation of the total attribute is {}'.format(population_std))


# Return the name and total power of pokemon whose total power is greater than 0.5 standard deviations from population mean

overpowered_pokemon = {}

for i in range(1,len(pokedex)+1):
    if pokedex[i]['Total'] > (population_mean + 0.5*population_std):
        overpowered_pokemon[pokedex[i]['Name']] = pokedex[i]['Total']

print(overpowered_pokemon)