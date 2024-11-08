# This is where we are putting our functions for the project check in
import random

def create_monster(level):
    """
    Creates a monster with attributes that power scales based on the given level.
    
    Parameters:
    level (int): The level of the monster, which affects its health, attack, and defense power.
    
    Returns:
    dict: A dictionary with the monster's attributes.
    """
    monster = {"Health": random.randint(75,100) + (level * 5), 
              "Attack": random.randint(10,15) + (level * 2),
              "Defense Power": (5 + level * 2),
              "Name": "Monster Level " + str(level)}
    return monster
