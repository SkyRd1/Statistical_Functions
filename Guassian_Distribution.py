#Author: Sepehr Roudini.
#Date: 03/07/2018.
#University of Iowa.
#Department of Chemical Engineering.
#Purpose: Calculating Gausian distribution
#for a set of data and overlay it on the
#histogram of data.



#--------------------------------------------------------------------------------------------#
#Defining function and importing necessary libraries.
#--------------------------------------------------------------------------------------------#

##############################################################################################
#Libraries used in this function are: numpy and
#matplotlib and Quantile_Calculation (local).
##############################################################################################
#xdata: A 1d array of data.
##############################################################################################
#This functions returnes Gaussian values and plots it.
##############################################################################################
def Calculate_Gaussian_Dist(xdata):
#numpy is for data manipulationt
 import  numpy as np
#matplotlib is for plotting data.
 import matplotlib.pyplot as plt
#Quantile_Calculation is for quartile calculation
 import Quantile_Calculation as QC
#Using help to see library distribution
 #help(QC)
#--------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------#


#--------------------------------------------------------------------------------------------#
#Preparing data and calculate Gaussian dist
#--------------------------------------------------------------------------------------------#
#Calculating mean and std
 data = np.sort(xdata)
 num = len(data)
 mean = np.sum(data)/len(data)
 std = np.sqrt(np.sum(((data-mean)**2))/(len(data)-1))
#Calculating bin width
 upper_q = QC.Calculate_Quantile(data,0.75)
 lower_q = QC.Calculate_Quantile(data,0.25)
 IQR = upper_q - lower_q
 c = 2.4
 bin_w = c*IQR/(num**(1/3))
 start = min(data)
 end = max(data) + bin_w
 bin_t = np.arange(start,end,bin_w)
#Guassian distribution
 G = (1/(std*np.sqrt(2*np.pi)))*np.exp(-((data-mean)**2)/(2*std**2))
#--------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------#


#--------------------------------------------------------------------------------------------#
#Plotting the data
#--------------------------------------------------------------------------------------------#
 n,bins,patches=plt.hist(data, bins=bin_t,label='Histogram', edgecolor='black',normed = 0, linewidth=1.2)
 plt.setp(patches, 'facecolor', 'g', 'alpha', 0.75)
 plt.plot(data,G*num,'k')
 plt.title('Data fitted to Guassian distribution')
 plt.xlabel('X')
 plt.ylabel('f(x)')
 plt.show()
 return G
#--------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------#