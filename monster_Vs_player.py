import random
import re

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
    Technique:
        Json.dump()
    """
    with open(path) as file:
        map = load(file)
        return map
rooms = [key for key in jsonopener(jsonfile)]

l3map = jsonopener(jsonfile).copy()

del l3map[random.choice(rooms)]
l3rooms = [key for key in l3map]
l3rooms.pop(l3rooms.index(random.choice(l3rooms)))

ef levels(level, turns):
    """
    Determines the conditions of the game. The higher the level the stronger the monster and less damage tolerance for the player

    Args:
        level (int): Sets the level of the game. Ranges from 1-3
        turns (int): Decides how many turns in the level


    Side Effects:
        Prints the monster attacking the player and the HP the player loses
        Prints the monster being attacked and losing HP
        Prints the Monster being in the same room as the player
        Prints the weapons the players finds and the weapons damage based on the Weapon class and methods
        Prints the matching level and turns
        Prints the monster or player being dead
    Technique:
        F strings with expression
    Author:
        Eli Jean

    """
    if level <= 3:
        if level == 3:
            prev_health = None

            monster = Monster(3,100,3)
            weaponchance = ["yes","no","no","no"]
            gameplay = True
            hasweapon = False
            while gameplay:
                print(f"LEVEL 3\tTurns: {turns}\n")
                print(str(player) + "\n")
                print(str(monster)+ "\n")
                playerchoice = player.choose_room(l3rooms)
                weapon = random.choice(weaponchance)
                if weapon == "yes":
                    yourweapon = player.equip_weapon(random.choice(weapon_storage))
                    hasweapon = True
                    print(f"{player.name} got {str(yourweapon)}\n")
                    weaponchance = ["no", "no"]
                monsterturn = True
                while monsterturn:
                    foundroom = room_finder(playerchoice, jsonopener(jsonfile)[playerchoice]["Floor"], level)
                    monsterturn = False
                    if playerchoice == foundroom:
                        print(f"MONSTER IS IN THE SAME ROOM AS {player.name}\n")
                        if hasweapon:
                            combat_sys(player, monster, yourweapon)
                            prev_health = player.health
                            pdmg = player.take_damage(random.randint(45,70))
                            if player.health < 50 and player.status() != "Dead":
                                    player.boost_health()
                            print(f"MONSTER hits {player.name} and {player.name} took {prev_health - pdmg} HP\n")
                            turns -= 1
                        elif hasweapon == False:
                            prev_health = player.health
                            pdmg = player.take_damage(random.randint(45,70))
                            if player.health < 50 and player.status() != "Dead":
                                    player.boost_health()
                            print(f"MONSTER hits {player.name} and {player.name} lost {prev_health - pdmg} HP\n")
                            turns -= 1
                    elif playerchoice != foundroom:
                        turns -= 1
                if player.status() == "Dead":
                      print(f"{player.name} is dead and the monster rips {player.name}'s heart out and makes a sandwich with it!")
                      gameplay = False
                elif monster.status() == "Dead":
                     print(f"Monster is dead and {player.name} wins")
                     gameplay = False
                if turns == 0:
                      gameplay = False
                      print(f"Level {level} is done and the {player.name} survived!")

    if level == 2:
        prev_health = None
        monster = Monster(2,50,1.5)
        weaponchance = ["yes","yes","no","no"]
        gameplay = True
        hasweapon = False
        while gameplay:
            print(f"LEVEL 2\tTurns: {turns}\n")
            print(str(player) + "\n")
            print(str(monster))
            playerchoice = player.choose_room(jsonopener(jsonfile))
            weapon = random.choice(weaponchance)
            if weapon == "yes":
                yourweapon = player.equip_weapon(random.choice(weapon_storage))
                hasweapon = True
                print(f"{player.name} got {str(yourweapon)}\n")
                weapon = ["no", "no"]
            monsterturn = True
            while monsterturn:
                foundroom = room_finder(playerchoice, jsonopener(jsonfile)[playerchoice]["Floor"], level)
                monsterturn = False
                if playerchoice == foundroom:
                    print(f"MONSTER IS IN THE SAME ROOM AS {player.name}!\n")
                    if hasweapon:
                        combat_sys(player, monster, yourweapon)
                        prev_health = player.health
                        pdmg = player.take_damage(random.randint(20,35))
                        print(f"MONSTER hits {player.name} and {player.name} lost {prev_health - pdmg} HP!\n")
                        turns -= 1
                    elif hasweapon == False:
                        prev_health = player.health
                        pdmg = player.take_damage(random.randint(20,35))
                        print(f"MONSTER hits {player.name} and player lost {prev_health -  pdmg} HP!\n")
                        turns -= 1
                elif playerchoice != foundroom:
                    turns -= 1
            if player.status() == "Dead":
                print(f"{player.name} is dead and the monster eats {player.name}'s flesh!")
                gameplay = False
            elif monster.status() == "Dead":
                    print(f"The monster is defeated! Onto the next level!\n")
                    gameplay = False
                    player.health = 100
                    levels(level + 1)
            if turns == 0:
                gameplay = False
                print(f"Level {level} is done! Moving to Level {level + 1}\n")
                player.health = 100
                levels(level + 1)
    if level == 1:
          prev_health = None
          monster = Monster(1,50,0.5)
          weaponchance = ["yes","yes","yes","no"]
          gameplay = True
          hasweapon = False
          while gameplay:
                print(f"LEVEL 1\tTurns: {turns}\n")
                print(str(player) + "\n")
                print(str(monster))
                playerchoice = player.choose_room(jsonopener(jsonfile))
                weapon = random.choice(weaponchance)
                if weapon == "yes":
                    yourweapon = player.equip_weapon(random.choice(weapon_storage))
                    hasweapon = True
                    print(f"{player.name} got {str(yourweapon)}\n")
                    weaponchance = ["no", "no"]
                monsterturn = True
                while monsterturn:
                    monsterchoices = [place for place in rooms]
                    foundroom = random.choice(monsterchoices)
                    print(f"Monster chose {foundroom}\n")
                    monsterturn = False
                    if playerchoice == foundroom:
                        print(f"MONSTER IS IN THE SAME ROOM AS {player.name}\n")
                        if hasweapon:
                            combat_sys(player, monster, yourweapon)
                            prev_health = player.health
                            pdmg = player.take_damage(5)
                            print(f"MONSTER hits {player.name} and {player.name} lost {prev_health - pdmg} HP\n")
                            turns -= 1
                        elif hasweapon == False:
                            prev_health = player.health
                            pdmg = player.take_damage(5)
                            print(f"MONSTER hits {player.name} and {player.name} lost {prev_health - pdmg} HP\n")
                            turns -= 1
                    elif playerchoice != foundroom:
                        turns -= 1
                if player.status() == "Dead":
                    print(f"{player.name} is dead and the monster eats {player.name}'s flesh!")
                    gameplay = False
                if monster.status() == "Dead":
                    print(f"Monster is defeated! Onto the next level!\n")
                    gameplay = False
                    levels(level + 1)
                if turns == 0:
                    gameplay = False
                    print(f"Level {level} is done! Moving to Level {level + 1}\n")
                    player.health = 100
                    levels(level + 1)

def room_finder(room, number, level):
    """
    Assists the monster in finding rooms by using the room's floor number


    Returns:
        Returns the room the monster selected
    Side Effects:
        Prints what the monster selected
        Changes the monsterchoices list
    Technique:
        Comprehensions
    Author:
        Eli Jean
    """
    if level == 3:
        if number == 1:
            monsterchoices = [place for place in l3rooms if jsonopener(jsonfile)[place]["Floor"] == 1]
            monsterchoices.append(room)
            finalchoice = random.choice(monsterchoices)
            print(f"Monster chose {finalchoice}\n")
            return finalchoice
        elif number == 2:
            monsterchoices = [place for place in l3rooms if jsonopener(jsonfile)[place]["Floor"] == 2]
            monsterchoices.append(room)
            finalchoice = random.choice(monsterchoices)
            print(f"Monster chose {finalchoice}\n")
            return finalchoice

    if level == 2:
        if number == 1:
            monsterchoices = [place for place in rooms if jsonopener(jsonfile)[place]["Floor"] == 1]
            monsterchoices.append(room)
            finalchoice = random.choice(monsterchoices)
            print(f"Monster chose {finalchoice}\n")
            return finalchoice
        elif number == 2:
            monsterchoices = [place for place in rooms if jsonopener(jsonfile)[place]["Floor"] == 2]
            monsterchoices.append(room)
            finalchoice = random.choice(monsterchoices)
            print(f"Monster chose {finalchoice}\n")
            return finalchoice

def main():
    levels(1, 5)
if __name__ == "__main__":
    main()
