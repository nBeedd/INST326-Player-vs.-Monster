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


def playerhealth(monster_attack = False, health = 100, health_jar = False):

    """ Manages the player's health based on monster attacks and found health jar.

    Arguments:
            monster_attack (bool): If true, reduces player's health by 10.
            health         (int): Players' health bar which is 100 at the start of the game.
            health_jar     (bool): If true, the player's health increases by random amount.
    
    Returns:
            int: The player's updated health bar.

    """
    health_loss = 10
    # The amount of health player lose if he gets attack by the monster.
    boost_health = random.choice([5,10,15,20]) if health_jar else 0
    #If the player finds the boost, it will increase his health.

    if monster_attack:
    # If the monster attacks the player, he will lose his health by 10.
        health -= health_loss
        print("Monster attacked! Player health decreased by 10.")
    elif health_jar:
    # If the player finds the health jar, it will increase his health.
        health += boost_health
        print(f"Player found a health jar! Gained {boost_health} health.")

    health = min(max(health, 0), 100)
    # This will ensure the player's health doesn't go below 0 nor above 100. 
    print(f"Current health: {health}")
    return health
