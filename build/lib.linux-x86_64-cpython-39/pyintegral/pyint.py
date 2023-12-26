#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 12:07:21 2021

RESUME : Numerical integration using Fortran legacy routines
    
Version: v01

@author: Jean Gomes Copyright (c)

@email: antineutrinomuon@gmail.com

Written: Jean Michel Gomes © Copyright
"""

# Import libraries
import matplotlib.pyplot as plt
import numpy as np

# My library
from pyintegral import flib

# Class PyIntegral
# pyintegral.py:22:0: C0103: Class name "PyIntegral_class" doesn't \
#                            conform to PascalCase naming style (invalid-name)
# pyintegral.py:26:0: R0205: Class 'PyIntegralClass' inherits from \
# object, can be safely removed from bases in python3 (useless-object-inheritance)

# class PyIntegral_class( object ):
class PyIntegralClass():
    ''''Created on 
Last version on Wed Sep 23 14:33:51 2020

@author: Jean Gomes Copyright (c)
'''

    def perform_integration(self):
        '''Perform integration'''
        #options = self.options or {}
        lambda_i = self.options.get('lambda_i', np.nan)
        lambda_f = self.options.get('lambda_f', np.nan)
        int_type = self.options.get('int_type', 2)
        integralall,iskeepon = flib.integralall(
            self.x_array,self.y_array,lambda_i,lambda_f,
            int_type=int_type,verbosity=self.verbosity
            )
        return integralall,iskeepon

# pyintegral.py:34:24: C0103: Argument name "x" doesn't conform to \
# snake_case naming style (invalid-name)
# pyintegral.py:37:0: C0301: Line too long (102/100) (line-too-long)
# pyintegral.py:38:4: R0913: Too many arguments (7/5) \
# (too-many-arguments)

    # def __init__(self,x_array,y_array,lambda_i=np.nan,
                 # lambda_f=np.nan,int_type=2,verbosity=0):
    def __init__(self,x_array,y_array,options=None,verbosity=0):
        # Set default values for optional parameters
        self.options = options or {}
        lambda_i = self.options.get('lambda_i', np.nan)
        lambda_f = self.options.get('lambda_f', np.nan)
        int_type = self.options.get('int_type', 2)

        self.int_type = int_type

        if np.isnan(lambda_i) or np.isnan(lambda_f):
            lambda_i = x_array[0]
            lambda_f = x_array[-1]

            # Store new values of lambda_i and lambda_f
            options['lambda_i'] = lambda_i
            options['lambda_f'] = lambda_f
        else:

            if lambda_i > lambda_f:
# pyintegral.py:58:22: C0209: Formatting a regular string which could \
# be a f-string (consider-using-f-string)
                result = f"... lambda_i > lambda_f: \
                        lambda_i={lambda_i:10.5f} > \
                        lambda_f={lambda_f:10.5f}"
                print(result)
                # print("... lambda_i > lambda_f: lambda_i={} > \
                      # lambda_f={}".format(lambda_i,lambda_f))

            # lambda_i = lambda_i
            # lambda_f = lambda_f

        if verbosity:
            result = f"... Integration from lambda_i: {lambda_i:10.5f} \
                     to lambda_f: {lambda_f:10.5f}"
            print(result)
            # print("... Integration from lambda_i: {} to \
                  # lambda_f: {} ".format(self.lambda_i,self.lambda_f))

        # self.integralall,self.iskeepon = flib.integralall(
        #     x_array,y_array,self.lambda_i,self.lambda_f,
        #     int_type=self.int_type,verbosity=verbosity
        #     )

        self.x_array=x_array
        self.y_array=y_array
        self.verbosity=verbosity

        self.integralall,iskeepon = self.perform_integration()
        if iskeepon:
            print("Problem!!!")

    def simpletest(self):
        '''Simple test for sine integration'''
        # This is a drill
        x_array = np.arange(0,2*np.pi,0.01)
        y_array = np.sin(x_array)

        lambda_i=-10
        lambda_f=32
        int_type=3
        options = {'lambda_i': lambda_i, 'lambda_f': lambda_f, 'int_type': int_type}

        integralall,iskeepon = flib.integralall(
            x_array,y_array,lambda_i,lambda_f,int_type=int_type,
            verbosity=0 )

        if iskeepon:
            print("Problem!!!!")

        area = np.trapz(y_array,x=x_array)

        print(area,integralall)

        plt.plot( x_array,y_array )
        plt.plot( x_array,y_array*0 )

        plt.step( x_array,y_array )

        print(x_array[0])
        i_object=PyIntegralClass( x_array,y_array,options )

        print( i_object.integralall )

def main():
    '''Main function of script'''
    print("")
