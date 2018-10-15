#Author: Sepehr Roudini.
#Date: 02/05/2018.
#University of Iowa.
#Department of Chemical Engineering.
#Purpose: Calculating a specified quantile of an array of data


#--------------------------------------------------------------------------------------------#
#Defining function and importing necessary libraries.
#--------------------------------------------------------------------------------------------#

##############################################################################################
#Libraries used in this function are: numpy and math.
##############################################################################################
#Data: A 1d array of data.
##############################################################################################
#Percentile: The fraction of data that the qauntile exceeds.
##############################################################################################
#This functions returnes quantile (between 0 and 1).
##############################################################################################
def Calculate_Quantile(Data, Percentile):
#numpy is for data manipulationt
 import  numpy as np
#math is for mathematical operations
 import math
#--------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------#


#--------------------------------------------------------------------------------------------#
#Preparing data and quantile calculation
#--------------------------------------------------------------------------------------------#
#Preparing and sorting data
 Percentile = float(Percentile)
 data = np.asanyarray(Data)
 data = sorted(data)
 q = ((len(data)-1)*Percentile)+1
 #Number of data is even
 num = int(q)
 if num==q:
     Quantile = data[num-1]
 #Number of data odd
 else:
     x1 = math.floor(q)
     y1 = data[x1-1]
     x2 = math.ceil(q)
     y2 = data[x2-1]
     slope = (y2-y1)/(x2-x1)
     Quantile = ((q-x1)*slope)+y1
 return Quantile
#--------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------#
