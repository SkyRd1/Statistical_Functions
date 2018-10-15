#Author: Sepehr Roudini.
#Date: 02/05/2018.
#University of Iowa.
#Department of Chemical Engineering.
#Purpose: Calculating Spearman correlation
#Coefficient for two sets of data.


#--------------------------------------------------------------------------------------------#
#Defining function and importing necessary libraries.
#--------------------------------------------------------------------------------------------#

##############################################################################################
#Libraries used in this function are: numpy and math.
##############################################################################################
#xdata: A 1d array of data.
##############################################################################################
#ydata: A 1d array of data.
##############################################################################################
#This functions returnes r (between -1 and 1).
##############################################################################################
def Calculate_Spearman_Coefficient(xdata, ydata):
#numpy is for data manipulationt
 import  numpy as np
#--------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------#


#--------------------------------------------------------------------------------------------#
#Preparing data and calculate correlation
#--------------------------------------------------------------------------------------------#
 xsorted = np.sort(xdata)
 ysorted = np.sort(ydata)
 xranks = np.zeros(len(xdata))
 yranks = np.zeros(len(ydata))
 for i in range(0,len(xdata)):
#If the the values are equal gives
#the average rank of them to each of them
  if len(np.where(xsorted == xsorted[i])[0]) >1:
   xrank = np.asanyarray((np.sum(np.where(xsorted == xsorted[i])[0]+1))/np.asanyarray(len(np.where(xsorted == xsorted[i])[0])))
  else:
   xrank = np.asanyarray(np.where(xsorted == xsorted[i])[0][0]+1)
  xranks[np.where(xdata == xsorted[i])] = xrank
#If the the values are equal gives
#the average rank of them to each of them
  if len(np.where(ysorted == ysorted[i])[0]) >1:
   yrank = np.asanyarray((np.sum(np.where(ysorted == ysorted[i])[0]+1)) /np.asanyarray(len(np.where(ysorted == ysorted[i])[0])))
  else:
   yrank = np.asanyarray(np.where(ysorted == ysorted[i])[0][0]+1)
  yranks[np.where(ydata == ysorted[i])] = yrank
 Di = xranks - yranks
 r = 1 - (6*(np.sum(Di**2))/((len(xdata))*((len(xdata)**2)-1)))
 return r
#--------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------#
