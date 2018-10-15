#Author: Sepehr Roudini.
#Date: 05/02/2018.
#University of Iowa.
#Department of Chemical Engineering.
#Purpose: PCA analysis


#--------------------------------------------------------------------------------------------#
#Defining function and importing necessary libraries.
#--------------------------------------------------------------------------------------------#

##############################################################################################
#Libraries used in this function are: numpy.
##############################################################################################
#Variables: An array of data each row is
#for a variable.
##############################################################################################
#NumofComp: Number of PCA components to
#transform data(should be equal or less
#than number of variables).
##############################################################################################
#Cov: If True PCA uses covariance matrix. 
#If Fasle it uses correlation matrix.
##############################################################################################
#This functions returnes respectively
#Eigenvalues,Information percentage in
#used eigenvalues, sorted Eigenvectors(all),
#transformed data and 
#Reconstructed data as an array(with its rows 
#for each variable)
##############################################################################################
def PCA_Analysis(Variables,NumofComp,Cov='True'):
#numpy is for data manipulationt
 import  numpy as np
#--------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------#
 
 
#--------------------------------------------------------------------------------------------#
#Preparing data
#--------------------------------------------------------------------------------------------#
 Variables = np.asanyarray(Variables)
 if Cov == 'True':
     mean = np.mean(Variables,axis=1)
     for i in range(0,len(mean)):
         Variables[i,:] = Variables[i,:]-mean[i]
 else:
     mean = np.mean(Variables,axis=1)
     stdd = np.std(Variables, axis = 1, ddof=1)
     Varr = np.zeros((np.shape(Variables)[0],np.shape(Variables)[1]),dtype=np.float)
     for i in range(0,len(mean)):
         Varr[i,:] = (Variables[i,:]-mean[i])/stdd[i]
#--------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------#

 
#--------------------------------------------------------------------------------------------#
#Calculating cov matrix, sorted eigenvalues and vectors
#--------------------------------------------------------------------------------------------#
 #Covariance matrix
 if Cov == 'True':
     Covmatr = np.cov(Variables,rowvar='True', ddof = 1)
 else:
     Covmatr = np.corrcoef(Variables,rowvar='True', ddof = 1)
 #Eigenvalues and vectors
 evalues, evectors = np.linalg.eig(Covmatr)
 #Sorting from large to small
 Sortedidx = evalues.argsort()[::-1]   
 evalues = evalues[Sortedidx]
 Info = (np.sum(evalues[0:NumofComp])/np.sum(evalues))
 evectors = evectors[:, Sortedidx]
 evectorsused = evectors[:, 0:NumofComp]
#--------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------#


#--------------------------------------------------------------------------------------------#
#Rerieving resuts
#--------------------------------------------------------------------------------------------#
 #Transforming data
 if Cov == 'True':
     Transformed = np.dot(Variables.T, evectorsused)
 else:
     Transformed = np.dot(Varr.T, evectorsused)
 old = np.zeros((np.shape(Variables)[1],np.shape(Variables)[0]),dtype=np.float)
 old[:,:NumofComp] = Transformed[:,:]
 Reconstructed = np.dot(old,evectors.T).T
 if Cov == 'True':
     for i in range(0,len(mean)):
             Reconstructed[i,:] = Reconstructed[i,:]+mean[i]
 else:
     for i in range(0,len(mean)):
         Reconstructed[i,:] = (stdd[i]*Reconstructed[i,:])+mean[i]
 Reconstructed[np.abs(Reconstructed) < 10**-13] = 0
 Transformed = Transformed.T
 #Reconstructing old data
 return evalues,Info,evectors, Transformed,Reconstructed
#--------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------#