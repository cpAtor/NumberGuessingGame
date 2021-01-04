# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 17:01:08 2021

@author: Chaitanya
"""

# 1. write a function that returns a random number between 1 and 100
# Python code to generate 
# random numbers and 
# append them to a list 
import random 
  
# Function to generate 
# and append them  
# start = starting range, 
# end = ending range 
# num = number of  
# elements needs to be appended 
start= input("enter your start value: ")
end= input("enter your end value: ")
start=int(start)
end=int(end)
def Rand(start, end, ): 
   
    num=random.randint(start, end) 
  
    return num
  
print(Rand(start, end))