#Author: Sepehr Roudini.
#Date: 02/05/2018.
#University of Iowa.
#Department of Chemical Engineering.
#Purpose: Calculating mean and Std


#--------------------------------------------------------------------------------------------#
#Defining function and importing necessary libraries.
#--------------------------------------------------------------------------------------------#

##############################################################################################
#Libraries used in this function are: numpy and math.
##############################################################################################
#Data: A 1d array of data.
##############################################################################################
#This functions returnes mean and standard
#deviation of data.
##############################################################################################
def Calculate_Mean_Std(Data):
#numpy is for data manipulationt
 import  numpy as np
#--------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------#


#--------------------------------------------------------------------------------------------#
#Preparing data and quantile calculation
#--------------------------------------------------------------------------------------------#
#Calculating mean
 mean = np.sum(Data)/len(Data)
#Calculating standard deviation
 std = np.sqrt(np.sum(((Data-mean)**2))/(len(Data)-1))
 return mean, std
#--------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------#