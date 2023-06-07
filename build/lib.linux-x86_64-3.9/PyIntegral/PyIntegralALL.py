#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 12:07:21 2021

RESUME : Numerical integration using Fortran legacy routines
    
Version: v01 beta

@author: Jean Gomes Copyright (c)

@email: antineutrinomuon@gmail.com

Written: Jean Michel Gomes © Copyright
"""

from pyintegralall import flib
import numpy as np
import matplotlib.pyplot as plt

# Class PyIntegralALL
class PyIntegralALL_class( object ):
    ''''Created on 
Last version on Wed Sep 23 14:33:51 2020

@author: Jean Gomes Copyright (c)
'''
    def __init__( self, x, y, lambda_i=np.nan, lambda_f=np.nan, int_type=2, verbosity=0 ):
        
        self.int_type = int_type
        
        if np.isnan(lambda_i) or np.isnan(lambda_f): 
            self.lambda_i = x[0]
            self.lambda_f = x[-1]
        else:
            
            if lambda_i >  lambda_f:
                print("... lambda_i > lambda_f: lambda_i={} > lambda_f={}".format(lambda_i,lambda_f) )
            
            self.lambda_i = lambda_i
            self.lambda_f = lambda_f
        
        if verbosity:
            print("... Integration from lambda_i: {} to lambda_f: {} ".format(self.lambda_i,self.lambda_f))
            
        self.integralall,self.iskeepon = flib.integralall( x,y,self.lambda_i,self.lambda_f,int_type=self.int_type,verbosity=verbosity )
        
# x = np.arange(0,2*np.pi,0.01)
# y = np.sin(x)

# lambda_i=-10 ; lambda_f=32 ; int_type=3

# integralall,iskeepon = integral.integralall( x,y,lambda_i,lambda_f,int_type=int_type,verbosity=0 )

# A = np.trapz(y,x=x)

# print(A,integralall)

# plt.plot( x,y )
# plt.plot( x,y*0 )

# plt.step(x, y)
 
# print(x[0])
# i_object=PyIntegralALL_class( x,y,lambda_i=-10,lambda_f=-32 )

# print( i_object.integralall )

def main():
    print("")


