#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 11:15:48 2020

@author: juliettesalles
"""


import random
 
MIN = 0
MAX = 1000

class GuessMachine():
    '''
    I have a number in mind
    you have to guess it!
    '''
    def __init__(self):
    
        self.number_to_guess = random.randint(MIN, MAX)
        self.number_of_attempt = 0
      
    def guess(self, num):
        '''
        attempt to find he right number
        it returns 'too high', 'too low', 'found'
        '''
        self.number_of_attempt += 1
       if num < self.number_to_guess:
           return 'too low'
       elif num > self.number_to_guess:
           return 'too high'
       else:
           return 'found'
    
  
if __name__ == '__main__':
    guess_nachine = GuessMachine()
    print('HEY ! Try to guess a number betwenn %d and %d'% (MIN, MAX))
     
    while True:
        user_input = input('Your guess?')
        try:
            user_attempt = int(user_input)
            result = guess_nachine.guess(user_attempt)
            if result == 'found':
                print('Fantastic'
                      'you could find the number I had in mind'
                      'in %d attempts!' % guess_nachine.number_of_attempt)
                break 
            else: 
                print(result)
        except ValueError:
            print('you joker...that was not an integer')
