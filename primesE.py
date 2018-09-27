#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###
# Name: Enea Dodi
# Student ID: 2296306
# Email: dodi@chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2018 Assignment: CW03
###

'''Eratosthenes module
This module contains the eratosthenes function that generates
primes up to the value of positive integer input n'''
import math
def eratosthenes(n):
    '''Erastosthenes function
    Args: n - positive integer representing ceiling number
    Returns: list of all primes less than n'''
    
    #check if integer passed in is positive
    if n < 1:
        raise Exception("Please enter an integer > 0")
    
    #generates all integers up to n > 2
    nums = list(range(n))
    nums = nums[2:]
    
    #removes all even numbers
    nums = [a for a in nums if ((a % 2 != 0) or (a==2))]
    
    #removes everything that isnt a prime number
    for i in nums:
        if i > math.sqrt(n):
            break
        else:
            for counter in nums:
                if(counter!=i and counter%i==0):
                    nums.remove(counter)
            
    return nums

def gen_eratosthenes():
    n = 10000
    nums = list(range(n))
    nums = nums[2:]
    nums = [a for a in nums if ((a % 2 != 0) or (a==2))]
    i = -1
    b = 0
    while True:
        i = i+1
        #nums.extend(list(range(nums[-1],(nums[-1]+int(math.sqrt(nums[-1])),2))))
        b = nums[i]
        yield b
        for num in nums:
            if(num != b and num%b == 0):
                nums.remove(num)