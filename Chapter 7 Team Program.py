<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
#Chapter 7 Team Program
=======
#Chapter 7 Team Program

import random

def main():
    #accepts no arguments
    #calls all functions to play the number of games specified
    
    pass
def output_dice(roll_die):
    #Accepts dice
    #Outputs each die in the list
    roll_die()
    return roll_die
def roll_die():
    #Accepts no arguments
    #Returns a random integer from 1 to 6
    number = random.randint(1, 6)
    return number

def first_roll():
    #Accepts no arguments
    #Uses roll_die to generate a list of 12 integers
    #Returns a list of 12 random integers
    num_rolls = 12
    dice = []
    for num in range(num_rolls):
        number = roll_die()
        dice.append(number)
    return dice
  
def count_frequency(dice, number):
    #Accepts a list of 12 random integers and a target value
    #Returns how often that target value occurs in the list
    pass


def find_mode(first_roll):
    #Accepts a list of dice.
    #Uses count_frequency(dice, number) to determine how often each number occurs.
    #Returns the mode
    first_roll()
    count_frequency(dice, number)


    pass
def list_unmatched_dice(dice, mode):
    #Accepts a list of dice
    #Determines which dice need rerolled
    #Returns a list of indexes to reroll
    index_list = []
    for num in dice:
        if num != mode:
            index = dice.index(num)
            index_list.append(index)
        else:
            pass


def list_unmatched_dice(dice):
    #Accepts a list of dice
    #Determines which dice need rerolled
    #Returns a list of indexes to reroll
    pass


def reroll_one(dice, index):
    #Accepts a list of dice and an index.
    #Uses roll_die to reroll that index
    #Returns a new list with that index rerolled
    find_mode()
    roll_die()



def reroll_many(dice):
    #Accepts a list of dice
    #Calls find_mode(), list_unmatched_dice(), and reroll_one() to reroll each die != the mode.
    #Returns a list of rerolled dice.

    
    pass

>>>>>>> Stashed changes
=======
#Chapter 7 Team Program

import random

def main():
    #accepts no arguments
    #calls all functions to play the number of games specified
    
    pass
def output_dice(roll_die):
    #Accepts dice
    #Outputs each die in the list
    roll_die()
    return roll_die
def roll_die():
    #Accepts no arguments
    #Returns a random integer from 1 to 6
    number = random.randint(1, 6)
    return number

def first_roll():
    #Accepts no arguments
    #Uses roll_die to generate a list of 12 integers
    #Returns a list of 12 random integers
    num_rolls = 12
    dice = []
    for num in range(num_rolls):
        number = roll_die()
        dice.append(number)
    return dice
  
def count_frequency(dice, number):
    #Accepts a list of 12 random integers and a target value
    #Returns how often that target value occurs in the list
    pass


def find_mode(first_roll):
    #Accepts a list of dice.
    #Uses count_frequency(dice, number) to determine how often each number occurs.
    #Returns the mode
    first_roll()
    count_frequency(dice, number)


    pass
def list_unmatched_dice(dice, mode):
    #Accepts a list of dice
    #Determines which dice need rerolled
    #Returns a list of indexes to reroll
    index_list = []
    for num in dice:
        if num != mode:
            index = dice.index(num)
            index_list.append(index)
        else:
            pass


def list_unmatched_dice(dice):
    #Accepts a list of dice
    #Determines which dice need rerolled
    #Returns a list of indexes to reroll
    pass


def reroll_one(dice, index):
    #Accepts a list of dice and an index.
    #Uses roll_die to reroll that index
    #Returns a new list with that index rerolled
    find_mode()
    roll_die()



def reroll_many(dice):
    #Accepts a list of dice
    #Calls find_mode(), list_unmatched_dice(), and reroll_one() to reroll each die != the mode.
    #Returns a list of rerolled dice.

    
    pass

>>>>>>> Stashed changes
=======
#Chapter 7 Team Program

import random

def main():
    #accepts no arguments
    #calls all functions to play the number of games specified
    
    pass
def output_dice(roll_die):
    #Accepts dice
    #Outputs each die in the list
    roll_die()
    return roll_die
def roll_die():
    #Accepts no arguments
    #Returns a random integer from 1 to 6
    number = random.randint(1, 6)
    return number

def first_roll():
    #Accepts no arguments
    #Uses roll_die to generate a list of 12 integers
    #Returns a list of 12 random integers
    num_rolls = 12
    dice = []
    for num in range(num_rolls):
        number = roll_die()
        dice.append(number)
    return dice
  
def count_frequency(dice, number):
    #Accepts a list of 12 random integers and a target value
    #Returns how often that target value occurs in the list
    pass


def find_mode(first_roll):
    #Accepts a list of dice.
    #Uses count_frequency(dice, number) to determine how often each number occurs.
    #Returns the mode
    first_roll()
    count_frequency(dice, number)


    pass
def list_unmatched_dice(dice, mode):
    #Accepts a list of dice
    #Determines which dice need rerolled
    #Returns a list of indexes to reroll
    index_list = []
    for num in dice:
        if num != mode:
            index = dice.index(num)
            index_list.append(index)
        else:
            pass


def list_unmatched_dice(dice):
    #Accepts a list of dice
    #Determines which dice need rerolled
    #Returns a list of indexes to reroll
    pass


def reroll_one(dice, index):
    #Accepts a list of dice and an index.
    #Uses roll_die to reroll that index
    #Returns a new list with that index rerolled
    find_mode()
    roll_die()



def reroll_many(dice):
    #Accepts a list of dice
    #Calls find_mode(), list_unmatched_dice(), and reroll_one() to reroll each die != the mode.
    #Returns a list of rerolled dice.

    
    pass

>>>>>>> Stashed changes
=======
#Chapter 7 Team Program

import random

def main():
    #accepts no arguments
    #calls all functions to play the number of games specified
    
    pass
def output_dice(roll_die):
    #Accepts dice
    #Outputs each die in the list
    roll_die()
    return roll_die
def roll_die():
    #Accepts no arguments
    #Returns a random integer from 1 to 6
    number = random.randint(1, 6)
    return number

def first_roll():
    #Accepts no arguments
    #Uses roll_die to generate a list of 12 integers
    #Returns a list of 12 random integers
    num_rolls = 12
    dice = []
    for num in range(num_rolls):
        number = roll_die()
        dice.append(number)
    return dice
  
def count_frequency(dice, number):
    #Accepts a list of 12 random integers and a target value
    #Returns how often that target value occurs in the list
    pass


def find_mode(first_roll):
    #Accepts a list of dice.
    #Uses count_frequency(dice, number) to determine how often each number occurs.
    #Returns the mode
    first_roll()
    count_frequency(dice, number)


    pass
def list_unmatched_dice(dice, mode):
    #Accepts a list of dice
    #Determines which dice need rerolled
    #Returns a list of indexes to reroll
    index_list = []
    for num in dice:
        if num != mode:
            index = dice.index(num)
            index_list.append(index)
        else:
            pass


def list_unmatched_dice(dice):
    #Accepts a list of dice
    #Determines which dice need rerolled
    #Returns a list of indexes to reroll
    pass


def reroll_one(dice, index):
    #Accepts a list of dice and an index.
    #Uses roll_die to reroll that index
    #Returns a new list with that index rerolled
    find_mode()
    roll_die()



def reroll_many(dice):
    #Accepts a list of dice
    #Calls find_mode(), list_unmatched_dice(), and reroll_one() to reroll each die != the mode.
    #Returns a list of rerolled dice.

    
    pass

>>>>>>> Stashed changes
