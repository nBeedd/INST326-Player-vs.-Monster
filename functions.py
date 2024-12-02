import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = None

    def take_damage(self, damage):
         self.health -= damage
         if self.health <= 0:
              print(f"{self.name} is dead!") 

    def equip_weapon(self, weapon):
         self.weapon = weapon 
        
    def playerhealth(self, monster_attack = False, health_jar = False):
        
        """ Manages the player's health based on monster attacks and found health jar.

    Arguments:
            monster_attack (bool): If true, reduces player's health by 10.
            health         (int): Players' health bar which is 100 at the start of the game.
            health_jar     (bool): If true, the player's health increases by random amount.
    
    Returns:
            int: The player's updated health bar.
        """
        
        health_loss = 10
        boost_health = random.choice([5,10,15,20]) if health_jar else 0
        if monster_attack:
            self.health -= health_loss
            print("Monster attacked! {self.name}. Player health decreased by 10.")
        elif health_jar:
            self.health += boost_health
            print(f"{self.name} found a health jar! Gained {boost_health} health. Current health: {self.health}")
            self.health = min(max(health, 0), 100)
            print(f"Current health: {self.health}")
            return self.health




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

def combat_sys(player_stamina, weapon_choice, attack_choice):
    
    """
    Used to make a turn based combat system

    Args:
        player_stamina (float): The current stamina of the player.
        weapon_choice (str): The weapon chosen by the player
        attack_choice (str): The type of attack chosen by the player 
    
    returns:
        float: The players stamina at the end of the turn

    """
    weapons = {
        'Sword': {'damage_modify': 1.7, 'stamina_modify': 1.7},
        'Hammer': {'damage_modify': 2.5, 'stamina_modify': 2.5},
        'Dagger': {'damage_modify': 0.7, 'stamina_modify': 0.7},
        'Spear': {'damage_modify': 1.0, 'stamina_modify': 1.0}
    }
    
    if weapon_choice in weapons:
        weapon_modifier = weapons[weapon_choice]['damage_modify']
        stamina_modifier = weapons[weapon_choice]['stamina_modify']
        print(f"You chose the {weapon_choice} with a damage modifier of {weapon_modifier}.")
        
        if attack_choice == "A":
            base_damage = 30
            base_stamina = 30
        elif attack_choice == "B":
            base_damage = 20
            base_stamina = 20
        elif attack_choice == "C":
            base_damage = 10
            base_stamina = 10
        else:
            print("Invalid attack")
            return player_stamina

        if player_stamina >= base_stamina * stamina_modifier:
            player_stamina -= base_stamina * stamina_modifier
            damage_monster = base_damage * weapon_modifier
            print(f"Damage dealt to monster: {damage_monster}")
            print(f"Remaining stamina: {player_stamina}")
        else:
            print("Not enough stamina for this attack.")
    else:
        print("Chosen weapon is not an option.")
    
    return player_stamina

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
