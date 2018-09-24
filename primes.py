#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###
# Name: Jack Savage
# Student ID: 2295072 
# Email: jsavage@chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2018 Assignment: CW03
###

'''Eratosthanes module
This module contains the eratosthanes function that generates
primes up to the value of positive integer input n'''

def eratosthanes(n):
    '''Erastosthanes function
    Args: n - positive integer
    Returns: list of all primes less than n'''
    
    # ensures positive integer entry value
    if n < 1:
        raise Exception('Please enter a value larger than 0')
        
    # generating list of integers between 1 and n excluding 1 and 0
    numbers = list(range(n))
    numbers.remove(0)
    numbers.remove(1)
    
    # obtaining divisor and removing even multiples of divisor
    for divisor in numbers:
        if divisor> math.sqrt(n):
        break
        for number in numbers:
            if (number%divisor == 0 and number>divisor):
                numbers.remove(number)
    
    return numbers

def gen_eratosthanes():
    while True:
        
