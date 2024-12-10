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
