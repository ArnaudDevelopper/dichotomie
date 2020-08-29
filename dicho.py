# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 18:19:01 2020

@author: Arnaud
"""

import numpy as np

def dichotomie(f, a, b, precision, iteration = 500, value = 0, details = True):
    
    if np.sign(a) != np.sign(b):
        difference = b-a
        i = 0
        
        while difference > precision and i < iteration:
            
            m = (a+b)/2
            
            if f(m) > value:
                b = m
            else:
                a = m
                
            difference = b-a
            
            i += 1
            
        if i < iteration:
            if details:
                return "With a precision of "+str(precision)+", the solution is "+str(m)+" after "+str(i)+" iterations."
            else:
                return m
        else:
            return "Error : Max iteratin has been reach."
        
        
        
    else:
        return "Error : Your values are not correct or the function is strictly positive/negative."