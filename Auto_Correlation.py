#Author: Sepehr Roudini.
#Date: 02/05/2018.
#University of Iowa.
#Department of Chemical Engineering.
#Purpose: Calculating auto temporal
#correlation coefficient for two sets of data.


#--------------------------------------------------------------------------------------------#
#Defining function and importing necessary libraries.
#--------------------------------------------------------------------------------------------#

##############################################################################################
#Libraries used in this function are: numpy and math.
##############################################################################################
#xdata: A 1d array of data.
##############################################################################################
#lagday: number of lag days for auto correlation.
##############################################################################################
#This functions returnes r (between -1 and 1).
##############################################################################################
def Calculate_auto_Coefficient(xdata,lagday):
#numpy is for data manipulationt
 import  numpy as np
#--------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------#


#--------------------------------------------------------------------------------------------#
#Preparing data and calculate correlation
#--------------------------------------------------------------------------------------------#
 ydata = xdata[:len(xdata)-lagday]
 xdata = xdata[lagday:]
 meanx = np.sum(xdata)/len(xdata)
 stdx = np.sqrt(np.sum(((xdata-meanx)**2))/(len(xdata)-1))
 meany = np.sum(ydata)/len(ydata)
 stdy = np.sqrt(np.sum(((ydata-meany)**2))/(len(ydata)-1))
 r = (np.sum((xdata-meanx)*(ydata-meany))*(1/(len(xdata)-1)))/(stdx*stdy)
 return r
#--------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------#
