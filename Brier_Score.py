#Author: Sepehr Roudini.
#Date: 04/17/2018.
#University of Iowa.
#Department of Chemical Engineering.
#Purpose: Calculatig Brier and skill 
#scores for using verification data

#--------------------------------------------------------------------------------------------#
#Defining function and importing necessary libraries.
#--------------------------------------------------------------------------------------------#

##############################################################################################
#Libraries used in this function are: numpy.
##############################################################################################
#yi: A 1d array of forcast probability values.
##############################################################################################
#nf: number of times forcast
##############################################################################################
#no: number of occurences
##############################################################################################
#This functions returnes respectively
#a,b,c,d for contingency table.
##############################################################################################
def Calculate_Scores(yi,nf,no):
#numpy is for data manipulationt
    import  numpy as np
#--------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------#


#--------------------------------------------------------------------------------------------#
#Calculating Scores
#--------------------------------------------------------------------------------------------#
    on = no/nf
    meano = np.sum(no)/np.sum(nf)
    #Brier score due to climatology
    ClimatologyBrier = meano*(1-meano)
    #Brier Score
    Brierscore = (np.sum(nf*(yi-on)**2))/np.sum(nf) - \
    np.sum(nf*(on-meano)**2)/(np.sum(nf))+ClimatologyBrier
    #Skill of Forcast
    Skill = 1-(Brierscore)/ClimatologyBrier
    return ClimatologyBrier, Brierscore, Skill
#--------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------#
