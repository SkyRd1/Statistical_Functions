#Author: Sepehr Roudini.
#Date: 05/02/2018.
#University of Iowa.
#Department of Chemical Engineering.
#Purpose: Fitting First-Order Two-State
#Markov Chain to precipitation data


#--------------------------------------------------------------------------------------------#
#Defining function and importing necessary libraries.
#--------------------------------------------------------------------------------------------#

##############################################################################################
#Libraries used in this function are: numpy.
##############################################################################################
#Variables: A 1d array of precipitation data.
##############################################################################################
#Lag: Number of lags.
##############################################################################################
#This functions returnes respectively
#n01,n10,n00,n11,n0o,no0,n1o,no1,p01,p10,
#p00,p11,pi, Fre, Lags,e01,e10,e00,e11, X2
##############################################################################################
def Fit_Markov_First_Order(Variables,Lag):
#numpy is for data manipulationt
    import  numpy as np
#--------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------#


#--------------------------------------------------------------------------------------------#
#Retrieving parameters
#--------------------------------------------------------------------------------------------#
#Findind n values
    n01=0
    n10=0
    n00=0
    n11=0
    for i in range(len(Variables)-1):
        if Variables[i]>0:
            if Variables[i+1]>0:
                n11=n11+1
            else:
                n10=n10+1
        elif Variables[i+1]>0:
            n01=n01+1
        else:
            n00=n00+1
    no1=n01+n11
    n1o=n10+n11               
    n0o=n00+n01
    no0=n00+n10
    #Transition Probabilities
    p01 = (n01)/(n00+n01)
    p10 = (n10)/(n11+n10)
    p00 = (n00)/(n00+n01)
    p11 = (n11)/(n11+n10)
    #Stationary probabilty
    pi = (p01)/(1+p01-p11)
    #relative frequency of precipitation
    Fre = no1/(len(Variables)-1)
    #Autocorrelation
    lag1 = p11-p01
    Lags = np.zeros(Lag+1)
    Lags[0] = 1
    Lags[1] = lag1
    if Lag>1:
        for i in range(2,Lag+1):
            Lags[i] = (lag1**i)
    #Test for indipendence
    e01=(n0o*no1)/(len(Variables)-1)
    e10=(n1o*no0)/(len(Variables)-1)
    e00=(n0o*no0)/(len(Variables)-1)
    e11=(n1o*no1)/(len(Variables)-1)
    #Independence
    X2 = (((n01-e01)**2)/e01)+(((n10-e10)**2)/e10)\
    +(((n00-e00)**2)/e00) + (((n11-e11)**2)/e11)
    return n01,n10,n00,n11,n0o,no0,n1o,no1,p01,p10,p00,p11,pi, Fre, Lags,e01,e10,e00,e11, X2
#--------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------#
