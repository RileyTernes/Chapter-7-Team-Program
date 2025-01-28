
#Chapter 7 Team Program

import random

def main():
    #accepts no arguments
    #calls all functions to play the number of games specified
    
    pass

def output_dice(dice):
    #Accepts dice
    #Outputs each die in the list
    #output dice accepts dice
    #it prints the dice
    #Max-1st merge

    print("Current Dice Roll:")
    for die in dice:
        print(die, end=" ")
    print()
    
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
    occurence = 0
    for die in dice:
        if die == number:
            occurence += 1
    return occurence


def find_mode(dice):
    #Accepts a list of dice.
    #Uses count_frequency(dice, number) to determine how often each number occurs.
    #Returns the mode
    roll = 1
    frequency = 0
    number = 1
    for die in [1,2,3,4,5,6]:
        if frequency > roll:
            mode = number
        frequency = count_frequency(dice, number)
        roll = roll + 1
        number = number + 1
       
    mode = mode - 1
    return mode
    



def list_unmatched_dice(dice, mode):
    #Accepts a list of dice
    #Determines which dice need rerolled
    #Returns a list of indexes to reroll
    index_list = []
    for num in dice:
        if num != mode:
            index = dice.index(num)
            index_list.append(index)
            
    return index_list





def reroll_one(dice, index):
    #Accepts a list of dice and an index.
    #Uses roll_die to reroll that index
    #Returns a new list with that index rerolled
    #Max-2nd merge

    dice[index] = roll_die()
    return dice



def reroll_many(dice):
    #Accepts a list of dice
    #Calls find_mode(), list_unmatched_dice(), and reroll_one() to reroll each die != the mode.
    #Returns a list of rerolled dice.
    pass
    
    #obtaining a mode by running find_mode
    mode = find_mode(dice)
    #obtaining index list by running list_unmatched_dice
    unmatched = list_unmatched_dice(dice)
    #rerolling dice
    for index in unmatched:
        dice[index] = reroll_die()
    
    
    return dice
