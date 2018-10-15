#Author: Sepehr Roudini.
#Date: 05/02/2018.
#University of Iowa.
#Department of Chemical Engineering.
#Purpose: Calculating harmonic 
#functions(monthly and daily)


#--------------------------------------------------------------------------------------------#
#Defining function and importing necessary libraries.
#--------------------------------------------------------------------------------------------#

##############################################################################################
#Libraries used in this function are: numpy.
##############################################################################################
#data: 1 d array of data.
##############################################################################################
#Harmonicnum:Number of harmonics desired for the data
##############################################################################################
#This functions returnes respectively Timestep,
#A,B,C,phi, monthly harmonic values each one
#as an array( each row is a harmonic in harmonic
#values array), daily harmonic values,n first monthly 
#harmonics and N first dialy harmonics.
#(All the harmonics are without adding the
# mean of data. AS a result, the mean should be
#added to each of them)
##############################################################################################
def Retrieve_Harmonics(data,Harmonicnum):
#numpy is for data manipulationt
    import  numpy as np
#--------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------#


#--------------------------------------------------------------------------------------------#
#Computing harmonics
#--------------------------------------------------------------------------------------------#
    #Time step(should be 12 in length)
    step=np.arange(1,len(data)+1)
    #empty arrays for storing harmonic
    #parameters
    phi=np.zeros(Harmonicnum)
    A=np.zeros(Harmonicnum)
    B=np.zeros(Harmonicnum)
    #Retrieving A and 
    for i in range(Harmonicnum):
        A[i]=(2/len(data))*np.sum(data*np.cos\
        ((2*np.pi*(i+1)*step)/len(data)))    
        B[i]=(2/len(data))*np.sum(data*np.sin\
        ((2*np.pi*(i+1)*step)/len(data)))
    #Retrieving amplitude   
    C=np.sqrt(A**2 + B**2)
    #Retrieving phase angle
    for i in range(len(A)):    
        if A[i]>0:
            phi[i]=np.degrees(np.arctan(B[i]/A[i]))
        elif A[i]==0:
            phi[i]=90
        elif np.arctan(B[i]/A[i]) >0:
            phi[i]=np.degrees(np.arctan(B[i]/A[i])) + 180
        else:
            phi[i]=np.degrees(np.arctan(B[i]/A[i]))-180
    #Creating array for storing
    #harmonic values
    Harmonics = np.zeros((Harmonicnum,len(data)))
    #Calculating values
    for i in range(Harmonicnum):
        Harmonics[i,:] = C[i]*np.cos((2*np.pi*(i+1)*step)/len\
        (data) - phi[i]*np.pi/180)
    Nfirstharmonics = np.sum(Harmonics, axis=0)
    #Daily harmonics
    Day=np.arange(1,366)
    Harmonicsday = np.zeros((Harmonicnum,len(Day)))
    #Calculating values
    for i in range(Harmonicnum):
        Harmonicsday[i,:] = (C[i]*np.cos((2*np.pi*(i+1)*Day)/365\
        - (phi[i]*np.pi/180 -30*np.pi/365)))
    Nfirstharmonicsday = np.sum(Harmonicsday, axis=0)
    return step,A,B,C,phi,Harmonics,Harmonicsday,Nfirstharmonics,Nfirstharmonicsday
#--------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------#
