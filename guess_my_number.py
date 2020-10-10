#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 11:15:48 2020

@author: juliettesalles
"""


import random
 
MIN = 0
MAX = 1000
 
if __name__ == '__main__':
    number_to_guess = random.randint(MIN, MAX)
    print('HEY ! Try to guess a number betwenn %d and %d'% (MIN, MAX))
     
    while True:
        user_input = input('Your guess?')
        try:
            user_attempt = int(user_input)
            if user_attempt == number_to_guess:
                print('Fantastic, you could find the number I had in mind')
                break 
            elif user_attempt < number_to_guess:
                 print('too low')
            else:
                print('too high')
        except ValueError:
            print('you joker...that was not an integer')