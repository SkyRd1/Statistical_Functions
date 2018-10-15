#Author: Sepehr Roudini.
#Date: 04/17/2018.
#University of Iowa.
#Department of Chemical Engineering.
#Purpose: Converting probabilistic
#forcasts( with parameters P(O1|yi) and p(yi) and yi)
#to nonprobabilistic forecasts


#--------------------------------------------------------------------------------------------#
#Defining function and importing necessary libraries.
#--------------------------------------------------------------------------------------------#

##############################################################################################
#Libraries used in this function are: numpy.
##############################################################################################
#yi: A 1d array of forcast probability values
##############################################################################################
#PO1yi: A 1d array of conditional probabilty
#of relative frequency of events happening
#for n forcasts.
##############################################################################################
#pyi: marginal probabilty
##############################################################################################
#Thr: Threshold for probabilty
##############################################################################################
#n: Total number of data
##############################################################################################
#This functions returnes respectively
#a,b,c,d for contingency table.
##############################################################################################
def Convert_to_Contingency(yi,PO1yi,pyi,Thr,n):
#numpy is for data manipulationt
    import  numpy as np
#--------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------#


#--------------------------------------------------------------------------------------------#
#Calculating contingency table
#--------------------------------------------------------------------------------------------#
    idx = np.where(yi>Thr)
    POY = PO1yi[idx]
    PY = pyi[idx]
    idx2 = np.where(yi<=Thr)
    POY2 = PO1yi[idx2]
    PY2 = pyi[idx2]
    #a+b in contingency table
    ab = np.round(n*np.sum(PY))
    #probability of rain observ and forcast yes
    Prob = np.sum(POY*PY)
    a = np.round(n*Prob)
    b = ab-a
    #c+d in contingency table
    cd = np.round(n*np.sum(PY2))
    #probability of rain observ and forcast no
    Prob2 = np.sum(POY2*PY2)
    c = np.round(n*Prob2)
    d = cd-c
    return a,b,c,d
#--------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------#
