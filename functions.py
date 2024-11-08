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
monsterhp = 10
resilience = 0
power = 2
turns = 0
monsterdead = False
mondone = False
def levels(level):
    """
    Creates a condition for the game according to the game's level. The higher the level the more options the monster has.
    Args:
        level (int): An integer used to set the level
    """
    map = {
        "Kitchen": {
            "Floor": 1,
            "Placement": ["Left of Dining Room", "Stairs to Bedroom"]
            
        },
        "Dining Room":{
            "Floor": 1,
            "Placement": "Right of the Kitchen"
        },
        "Bedroom": {
            "Floor": 2,
            "Placement": "Right of Bathroom"
        
        },
        "Bathroom": {
            "Floor": 2,
            "Placement": "Left of Bedroom"
        }
    }
    

    if level <= 3:
        if level == 3:
            rooms = [key for key in map]
            turns = 2
            while monsterdead == False:
                if playercounter >= 1:
                    
                    if playerchoice == key:
                            monsterchoice = random.choice(playerchoice, "")
                    elif map[playerchoice]["Floor"] == map[monsterchoice]["Floor"]:
                            monsterchoices = [room for room in rooms if map[room]["Floor"] == map[playerchoice]["Floor"]]
                            monsterchoice = random.choice(monsterchoices)
                            turns -= 1
                            if "Left" in map[playerchoice]["Placement"]:
                                 monsterchoices = [room for room in rooms if "Right" in map[playerchoice]]
                                 monsterchoice = random.choice(monsterchoice)
                                 turns -= 1  
        
                            elif "Right" in map[playerchoice]["Placement"]:
                                 monsterchoices = [room for room in rooms if "Left" in map[playerchoice]]
                                 monsterchoice = random.choice(monsterchoice)
                                 turns -= 1
                    
                    if playerchoice in rooms:
                         monsterchoice = random.choice(rooms)
                    if turns == 0:
                            mondone = True
                    
    if level == 2:
        if map[playerchoice]["Floor"] == map[monsterchoice]["Floor"]:
            
                            monsterchoices = [room for room in rooms if map[room]["Floor"] == map[playerchoice]["Floor"]]
                            monsterchoice = random.choice(monsterchoices, "", "")
                            turns -= 1
        if turns == 0:
                            mondone = True
         
    if level == 1:
         turns = 1
         if playerchoice in rooms:
              monsterchoice = random.choice(rooms)
         if turns == 0:
                mondone = True

    health = min(max(health, 0), 100)
    # This will ensure the player's health doesn't go below 0 nor above 100. 
    print(f"Current health: {health}")
    return health
