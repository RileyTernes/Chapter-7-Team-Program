#Chapter 7 Team Program

def main():
    #accepts no arguments
    #calls all functions to play the number of games specified
    
    
def output_dice(dice):
    #Accepts dice
    #Outputs each die in the list
    
    
def roll_die():
    #Accepts no arguments
    #Returns a random integer from 1 to 6


def first_roll():
    #Accepts no arguments
    #Uses roll_die to generate a list of 12 integers
    #Returns a list of 12 random integers
    
    
def count_frequency(dice, number):
    #Accepts a list of 12 random integers and a target value
    #Returns how often that target value occurs in the list


def find_mode(dice):
    #Accepts a list of dice.
    #Uses count_frequency(dice, number) to determine how often each number occurs.
    #Returns the mode


def list_unmatched_dice(dice):
    #Accepts a list of dice
    #Determines which dice need rerolled
    #Returns a list of indexes to reroll


def reroll_one(dice, index):
    #Accepts a list of dice and an index.
    #Uses roll_die to reroll that index
    #Returns a new list with that index rerolled


def reroll_many(dice):
    #Accepts a list of dice
    #Calls find_mode(), list_unmatched_dice(), and reroll_one() to reroll each die != the mode.
    #Returns a list of rerolled dice.
