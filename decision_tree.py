
# -*- coding: utf-8 -*-
"""
Created on Sun 1:16 AM 02/11/2018

@author: SELVA GANESH
"""
#==========================================================#

#Import libraries

from __future__ import division

import pandas as pa
import math as ma
import sys as sy

#==========================================================#

#Declare global variables
data_dict = { }
class_set = { }
class_occur = []
info_gain = { }
entropy_dict = { }
kentropy_dict = { }
class_name = ''
class_entropy = 0.0

#==========================================================#
#List of Lambda functions


#==========================================================#



#==========================================================#
#Calculate Entropy value as per the (=-P(x)log(x) -P(y))log(y) & (K0 * K1 * Kn / (n *K)


def Entropy(feature):
	feature_data = data_dict[feature]
	feature_data_cnt = len(feature_data)	
	feature_set = set(feature_data)
	

	feature_set_occur = map(lambda x: data_dict[feature].count(x), feature_set)	

	entropy = 0.0
	k_entropy = 0.0
	
	#Calculate entropy
	for i in feature_set_occur:
		entropy = entropy + (-1 * float(i)/feature_data_cnt * ma.log((float(i)/feature_data_cnt),2))
	

	#Calculate k-entropy
	feature_mult = reduce(lambda x,y: x*y, feature_set_occur)
	k_entropy = float(feature_mult)/(len(feature_set) * feature_data_cnt)
	
	#Store entropy & k-entropy in the disctionary
	entropy_dict[feature] = entropy
	kentropy_dict[feature] = k_entropy



#==========================================================#
#        MAIN PROGRAM
#==========================================================#


#Process the csv file

input_parm = sy.argv

csv_name = input_parm[1]
csv_ptr = pa.read_csv(csv_name)

#Column Names
csv_col_name = csv_ptr.columns


#Total No of columns
csv_col = len(csv_col_name)



#Read CSV by Column Names
#x = (csv_ptr[csv_col_name[0]].to_csv(index=False).split())
#print x
	

#Storing the FEATURE & CLASS values in a DICTIONARY with Features as key values

for i in range(csv_col):
	data_dict[csv_col_name[i]] = csv_ptr[csv_col_name[i]].to_csv(index=False).split()
	#pass


#---------------------- Dictionary Loaded with Feature and Class values ------------------------------ #

#Calculate Entropy values & k-entropy values
map(Entropy, data_dict.keys())


print "Entropy dict: "
print entropy_dict.items()

print("---------")

print "K-Entropy dict: "
print kentropy_dict.items()


#Store the class attributes
class_name = csv_col_name[-1]
class_entropy = entropy_dict[csv_col_name[-1]]
class_kentropy = kentropy_dict[csv_col_name[-1]]
#print "class name: " + class_name
#print "class entropy: " + str(class_entropy)

#print(" *** --------- *** ")

#Delete the class entropy values
del entropy_dict[class_name]
del kentropy_dict[class_name]

min(entropy_dict.values())

#-------------




#-------------


print(" *** --- End --- *** ")


#==========================================================#

