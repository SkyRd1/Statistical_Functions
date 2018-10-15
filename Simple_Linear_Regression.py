#Author: Sepehr Roudini.
#Date: 04/11/2018.
#University of Iowa.
#Department of Chemical Engineering.
#Purpose: Simple linear regression(R squared)


#--------------------------------------------------------------------------------------------#
#Defining function and importing necessary libraries.
#--------------------------------------------------------------------------------------------#

##############################################################################################
#Libraries used in this function are: numpy.
##############################################################################################
#X: A 1d array of predictor data.
##############################################################################################
#Y: A 1d array for predictand data.
##############################################################################################
#Slope: The slope value to be tested.
##############################################################################################
#X0: The value for which prediction
#interval probabilty is desired.
##############################################################################################
#T: The interval value
##############################################################################################
#This functions returnes respectively
#a,b,Yhat,SSE,SSR,MSE,MSR,F,R2,Sigmaa,
#Sigmab,z(for slope test),p(for slope test)
#,z(for prediction interval), p(for prediction interval)
##############################################################################################
def Linear_Regression(X,Y,Slope,X0,T):
    #numpy is for data manipulationt
    import  numpy as np
    #Statsmodels is for regression calculations
    import statsmodels.api as sm
    #For probability
    from scipy import stats
    
   
    
#--------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------#
 
 
#--------------------------------------------------------------------------------------------#
#Retrieving ANOVA table
#--------------------------------------------------------------------------------------------#
    X = np.asanyarray(X)
    Y = np.asanyarray(Y)
    # we need to consider a constant as interecept
    # essenailly regression to two predictnat.
    #one is X, one is costant
    #x = sm.add_constant(X)
    results = sm.OLS(Y, sm.add_constant(X)).fit()
    print (results.summary())
    print ("results.mse_resid = ", results.mse_resid )
#--------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------#


#--------------------------------------------------------------------------------------------#
#Calculating regression parameters
#--------------------------------------------------------------------------------------------#
    #print (results.ess, results.fvalue, results.mse_model,
    #results.mse_resid, results.mse_total, results.params, results.rsquared, results.ssr )
    # linear regression equatin
    N = len(X)
    #Constant
    b= (N*np.sum(X*Y) - np.sum(X)*np.sum(Y))/(N*np.sum(X**2)\
    -np.sum(X)**2)
    #Slope
    a = np.mean(Y)-b*np.mean(X)
    #regression values
    Yhat = a + b*X
    #Sum of Squared errors
    SSE = np.sum((Y-Yhat)**2)
    #Regression sum of squares
    SSR = np.sum((Yhat - np.mean(Y))**2)
    #Sum of Squares total
    SST = np.sum((Y - np.mean(Y))**2)
    #Mean squared error(Se^2)
    MSE = SSE/(len(X)-2) 
    #Mean Square Regression
    MSR = SSR/1
    #F ratio
    F = MSR/MSE
    #R2
    R2 = SSR/SST
    #Slope standard deviation
    Sigmab = np.sqrt(MSE/np.sum((X-np.mean(X))**2))
    #Z value for a slope
    z = (b-Slope)/Sigmab
    #Probabilty for that z value
    p= stats.norm.cdf(z)
    #Constant standard deviation
    Sigmaa = np.sqrt(MSE)*(np.sqrt(np.sum((X**2) / (len(X) *\
    np.sum ( (X - np.mean(X))**2 )))))
    Sy2=MSE*(1.+(1./N) + ((X0-np.mean(X))**2)/np.sum((X-np.mean(X))**2))
    Sy = np.sqrt(Sy2)
    Z = -T/Sy
    P =1 - 2*(stats.norm.cdf(Z))
    return a,b,Yhat,SSE,SSR,MSE,MSR,F,R2,Sigmaa, Sigmab,z,p,Z,P
#--------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------#
