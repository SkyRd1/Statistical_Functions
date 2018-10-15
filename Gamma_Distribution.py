#Author: Sepehr Roudini.
#Date: 03/07/2018.
#University of Iowa.
#Department of Chemical Engineering.
#Purpose: Calculating Gamma distribution
#for a set of data and overlay it on the
#histogram of data.



#--------------------------------------------------------------------------------------------#
#Defining function and importing necessary libraries.
#--------------------------------------------------------------------------------------------#

##############################################################################################
#Libraries used in this function are: numpy and
#matplotlib and Quantile_Calculation (local) and scipy.
##############################################################################################
#xdata: A 1d array of data.
##############################################################################################
#This functions returnes Gamma values and plots it.
##############################################################################################
def Calculate_Gamma_Dist(xdata):
#numpy is for data manipulationt
 import  numpy as np
#matplotlib is for plotting data.
 import matplotlib.pyplot as plt
#Quantile_Calculation is for quartile calculation
 import Quantile_Calculation as QC
#Using help to see library distribution
 #help(QC)
#scipy is for statistical calculations
 from scipy import special as sci
#--------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------#


#--------------------------------------------------------------------------------------------#
#Preparing data and calculate Gaussian dist
#--------------------------------------------------------------------------------------------#
#Calculating mean and std
 data = np.sort(xdata)
 num = len(data)
 mean = np.sum(data)/len(data)
#Calculating bin width
 upper_q = QC.Calculate_Quantile(data,0.75)
 lower_q = QC.Calculate_Quantile(data,0.25)
 IQR = upper_q - lower_q
 c = 2.
 bin_w = c*IQR/(num**(1/3))
 start = min(data)
 end = max(data) + bin_w
 bin_t = np.arange(start,end,bin_w)
#Gamma distribution
 d = np.log(mean) - 1.0/num * np.sum(np.log(data))
 alpha = (1+np.sqrt(1+4.0*d/3.0))/(4.0*d)
 beta = mean / alpha
 fx = np.power(data/beta,(alpha-1))*np.exp(-1.*data/beta)/(beta * sci.gamma(alpha))
 #--------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------#


#--------------------------------------------------------------------------------------------#
#Plotting the data
#--------------------------------------------------------------------------------------------#
 n,bins,patches=plt.hist(data, bins=bin_t,label='Histogram', edgecolor='black',normed = 0, linewidth=1.2)
 plt.setp(patches, 'facecolor', 'g', 'alpha', 0.75)
 plt.plot(data,fx*num,'k')
 plt.title('Data fitted to Gamma distribution')
 plt.xlabel('X')
 plt.ylabel('f(x)')
 plt.show()
 return fx
#--------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------#