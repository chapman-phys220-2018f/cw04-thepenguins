#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###
# Name: Enea Dodi
# Student ID: 2296306
# Email: dodi@chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2018 Assignment: CW03
###

'''Eratosthanes module
This module contains the eratosthanes function that generates
primes up to the value of positive integer input n'''
import math
def eratosthanes(n):
    '''Erastosthanes function
    Args: n - positive integer representing ceiling number
    Returns: list of all primes less than n'''
    
    #check if integer passed in is positive
    if n < 1:
        raise Exception("Please enter an integer > 0")
    
    #generates all integers up to n > 2
    nums = list(range(n))
    nums = nums[2:]
    
    #removes all even numbers
    nums = [a for a in nums if a % 2 != 0]
    for i in nums:
        if i > math.sqrt(n):
            break
        for a in nums:
            if (a%i == 0 and a>i):
                nums.remove(a)
    return nums

def gen_eratosthanes