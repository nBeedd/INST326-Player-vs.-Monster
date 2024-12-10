import random
import re


invalidname = False
monsterturn = False
hasweapon = False
playerchoice = str()
foundroom = str()
player = None


class Player:
    """
    A class representing a player in a game.

    Attributes:
        name (str): The name of the player.
        health (int): The current health points of the player, set to 100.
        weapon (str or None): The weapon currently equipped by the player.
        current_room (str or None): The current room the player is in.     
    """

    def __init__(self, name):
        """
        Initialize a Player object.

        Args:
            name (str): The name of the player.

        Side-effects:
             Initializes instance attributes (self.health, self.weapon, self.current_room).

        Author: 
            Abhishek Subedi
        """
        self.name = name
        self.health = 100
        self.weapon = None
        self.current_room = None

    def take_damage(self, damage):
        """
        Reduce the player's health by the specified amount.

        Args:
            damage (int): The amount of damage to be taken.

        Returns:
            int: The remaining health after taking the damage.

        Author:
            Abhishek Subedi
        """
        self.health -= damage
        return self.health


    def boost_health(self):
        """
        Increase the player's health by a random amount between 5 to 20.

        Returns:
            int: The new health value after boosting.
        
        Author: 
            Abhishek Subedi

        Technique:
            Key Function
        """
        boost_health = random.choice([5, 10, 15, 20])
        self.health += boost_health
        print(f"{self.name} found a health boost! Gained {boost_health} HP.")
        self.health = min(max(self.health, 0), 100)
        return self.health  
    
    def status(self):
        """
        Check the current status of the player.

        Returns:
            str: "Alive" if the player's health is greater than 0, otherwise "Dead".

        Author:
            Abhishek Subedi     
        """
        if self.health > 0:
            return "Alive"
        else:
            return "Dead"

    def equip_weapon(self, weapon):
        """
        Equip the player with a specified weapon.

        Args:
            weapon (str): The weapon to be equipped.

        Author:
            Abhishek Subedi
        """
         
        self.weapon = weapon

    def choose_room(self, game_map):
        """
        Allow the player to choose a room from a provided game map.

        Args:
            game_map (list): A list of available rooms.

        Returns:
            str: The name of the chosen room.

        Author:
            Abhishek Subedi
        """
        print("Available Rooms:")
        for room in game_map:
              print(room)
        playerturn = True
        while playerturn:
            room_choice = input("Select a room and type the room exactly as shown: ")

            if room_choice in game_map:
                self.current_room = room_choice

                print(f"{self.name} moved to {self.current_room}.")
                playerturn = False
                return room_choice

            else:
                print("Invalid room choice. Please select a valid room.")

    def __str__(self):
        """
        Return a string representation of the player.

        Returns:
            str: A f string showing the player's name, health, and current room.

        Author: 
            Abhishek Subedi

        Technique:
            Magic method
        """
        return f"Player: {self.name}, Health: {self.health}, Current Room: {self.current_room}"
    
    
    
class Monster:
    
    def __init__(self, level, health=100, defense=5):
        """
        Initializes a new Monster instance with level, health, and defense.

        Args:
            level (int): The initial level of the monster.
            health (int): The initial health points of the monster.
            defense (int): The defense value of the monster.

        Side Effects:
            Sets the monster's attributes to the given or default values.
        Author: 
            Ahmed Babikir
        Technique:
            magic method
        """
    
        self.level = level
        self.health = health
        self.defense = defense

    def take_damage(self, damage):
        """
        Reduces the monster's health based on the incoming damage.

        Args:
            damage (int): The amount of damage inflicted on the monster.

        Side Effects:
            Updates the monster's health attribute, reducing it based on the damage.
        Returns:
            int: updated health attribute 
        Author: 
            Ahmed Babikir
        """
        
        self.health = self.health - damage
        self.health = self.health + self.defense
        return self.health
        
    def status(self):
    
        """
        Checks if the monster is still alive.

        Returns:
            bool: True if the monster's health is greater than 0, False otherwise.
        Author: 
            Ahmed Babikir
        """
        
        if self.health > 0:
            return "Alive"
        else:
            return "Dead"


    def __str__(self):
         """
        Provides a string representation of the monster's current stats.

        Returns:
            str: A formatted string showing the monster's health, attack, and defense.
        Author: 
            Ahmed Babikir
        Technique:
            Magic Method
            
        """
        return (f"\nMonster Health: {self.health} Defense: {self.defense}")
    
    
    
    
    
class Weapon:
    def __init__(self, name, mod_damage):
        """
        Initializes the weapon object.
        
        Args:
            name (str): Name of the weapon.
            mod_damage (float): The damage modifer of the weapon.
            
        Side Effects:
            Attributes name and mod_damage are created. 
        """
        self.name = name
        self.mod_damage = mod_damage


    def __str__(self):
        """
        An informal representation of the weapon description.
        
        Returns:
            str: String formatted with name of weapon and the damage modifer.
        """
        return f"{self.name} with damage modifer of {self.mod_damage}"

weapon_storage = [ Weapon("Sword", 1.7),
                  Weapon("Hammer", 2.5),
                  Weapon("Dagger", 0.7),
                  Weapon("Spear", 1.0)]


def validate_player_name(name):
    """
    Validates the name the player inputs when the game starts
    
    Args:
        name (str): name inputted by the player.
        
    Raises:
        ValueError: if the name doesn't start with a capital letter and has numbers.
    
    Returns:
        str: Validated players name.
        
    Author:
        Edras Tlapechco
        
    Technique Demonstrated:
        Regular expressions
    """
    if not re.match(r"^[A-Z][a-zA-Z]*$", name):
        raise ValueError("Player name must start with a capital letter and contain only letters.")
    return name



while True:
    try:
        player_name  = input("Enter your player name: ")
        validated_name = validate_player_name(player_name)
        player = Player(validated_name)
        print(f"Welcome, {player.name}!")
        break
    except ValueError as e:
        print(e)
        
        
        
        
def combat_sys(player, monster, weapon):

    """
    Executes a combat action where the player attacks a monster using a attack type.

    Args:
        player (object): The player initiating the attack.
        monster (object): The monster being attacked.
        weapon (object): The weapon being used for the attack.
        attack (str): The type of attack chosen by the player.

    Returns:
        float: Total damage of the attack.
        bool: False if the attack type was invalid.
        
    Author:
        Edras Tlapechco
        
    Technique Demonstrated:
        Conditional Expression

    """

    attack = input("Choose your attack (Heavy, Medium, Light): ").capitalize()

    attack_types = {"Heavy": 30, "Medium": 20, "Light": 10}
    base_damage = attack_types[attack] if attack in attack_types else None
    if base_damage is None:
        print("Invalid attack choice! Monster takes advantage and attacks!\n")
        return False
    total_damage = base_damage * weapon.mod_damage
    monster.take_damage(total_damage)
    print(f"{player.name} used his {weapon.name}! Monster took {total_damage} damage!")
    return total_damage
    
def jsonopener(path):
    """
    Opens and loads a JSON file into a Python dictionary.

    Args:
        path (str): The file path to the JSON file.

    Returns:
        dict: The maps from the JSON file as a Python dictionary.

    Side Effects:
        Opens and reads the file.
    Author:
        Ahmed Babikir
    """
    with open(path) as file:
        map = load(file)
        return map
rooms = [key for key in jsonopener(jsonfile)]

l3map = jsonopener(jsonfile).copy()

del l3map[random.choice(rooms)]
l3rooms = [key for key in l3map]
l3rooms.pop(l3rooms.index(random.choice(l3rooms)))
