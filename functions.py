import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = None
        self.stamina = 100
        self.current_room = None

    def take_damage(self, damage):
         self.health -= damage
         if self.health <= 0:
              print(f"{self.name} is dead!") 
    
    def use_stamina(self, stamina):
        self.stamina -= stamina
        if self.stamina <= 0:
            print(f"{self.name} is out of stamina, needs to recharge!")
            
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
            self.health = min(max(self.health, 0), 100)
            print(f"Current health: {self.health}")
            return self.health

    def choose_room(self, game_map):
        print("Available Rooms:")
        for room in game_map:
              print(room)

        while True:
            room_choice = input("Select a room and type the room exactly as shown: ")
            if room_choice in game_map:
                self.current_room = room_choice
                print(f"{self.name} moved to {self.current_room}.")
                break
            else:
                print("Invalid room choice. Please select a valid room.")

    def __str__(self):
          return f"Player {self.name}: Health={self.health}, Stamina={self.stamina}, Current Room={self.current_room}"


class Monster:
    def __init__(self, level, health=100, attack=10, defense=5):
        self.level = level
        self.health = health
        self.attack = attack
        self.defense = defense
    
    def take_damage(self, damage):
        # Reduces the monster's health based on incoming damage.
        damage_after_defense = max(0, damage - self.defense)
        self.health = max(0, self.health - damage_after_defense)
    
    def level_up(self):
        # Levels up the monster 1 level and strengthens the monster.
        self.level += 1
        self.attack += random.randint(2, 10)
        self.defense += random.randint(1,5)
        self.health += random.randint(10,30)
        print(f"Monster has leveled up to {self.level}")
    
    def is_monster_alive(self):
        # Checks to see if monster is stil alive
        return self.health > 0
    def __str__(self):
        # returns a string representation of the monster
        return (f"Monster\n"
                 f"Health: {self.health}\n"
                 f"Attack: {self.attack}\n"
                 f"Defense: {self.defense}")


class Weapon:
    def __init__(self, name, mod_damage, mod_stamina_cost):
        self.name = name
        self.mod_damage = mod_damage
        self.mod_stamina_cost = mod_stamina_cost
        
    def __str__(self):
        return f"{self.name} with damage modifer of {self.mod_damage} and stamina modifer of {self.mod_stamina_cost}"
    
weapon_storage = [ Weapon("Sword", 1.7, 1.7),
                  Weapon("Hammer", 2.5, 2.5),
                  Weapon("Dagger", 0.7, 0.7),
                  Weapon("Spear", 1.0, 1.0)]    
        
        
def combat_sys(player, monster, weapon, attack):
    
    """
    """
    
    if attack == "Heavy":
        base_damage = 30
        base_stamina = 30
    elif attack == "Attack":
        base_damage = 20
        base_stamina = 20
    elif attack == "Light":
        base_damage = 10
        base_stamina = 10
    else:
        print("Invalid attack choice!")
        return False
    
    if player.stamina < base_stamina + weapon.stamina_cost:
        print(f"{player.name} does not have enough stamina to use {weapon.name} with ")
        
    total_damage = base_damage * weapon.mod_damage
    total_stamina = base_stamina * weapon.mod_stamina_cost
    
    player.use_stamina(total_stamina)
    monster.take_damage(total_damage)

    
turns = 0
monsterdead = False
mondone = False
playerturn = False
monsterturn = False
monsterdead = False
monsterattack = False


def levels(level):
    
    """
    Creates a condition for the game according to the game's level. The higher the level the more options the monster has.
    Args:
        level (int): An integer used to set the level
    Returns:
        finalchoice (str): Represents the monsters choice
    """
    map = {
        "Kitchen": {
            "Floor": 1,
            "Placement": "Left of Dining Room"
            
        },
        "Dining Room":{
            "Floor": 1,
            "Placement": "Right of the Kitchen"
        },
        "Living Room":{
            "Floor": 1,
            "Placement": "Left of Kitchen"
        },

        "Bedroom": {
            "Floor": 2,
            "Placement": "Right of Bathroom"
        
        },
        "Bathroom": {
            "Floor": 2,
            "Placement": "Left of Bedroom"
        },
        "Guest Room": {
            "Floor": 2,
            "Placement": "Left of Bathroom"
        }
    }
    
    limit = 6
    
    weapons = ["Sword", "Hammer", "Dagger", "Spear"]
    if level <= 3:
        
        if level == 3:
            #Determines whether the player will get a weapon or not
            weaponchance = ["yes","no","no","no"]
            monster = create_monster(3)
            rooms = [key for key in map]
            playerturn = True
            for room in rooms:
                   print(room)
            if playerturn == True:
            
                playerchoice = input("Select a room and type the room exactly as it is shown: ")
                weapon = random.choice(weaponchance)
                if weapon == "yes":
                       pass
                       #use the weapon function
                else:
                        print(f"You selected {playerchoice}" if playerchoice in rooms else "not in the rooms")
                        
            playerturn = False
            monsterturn = True
            while monsterturn == True:  
                    
                    if map[playerchoice]["Floor"] == map[playerchoice]["Floor"]:
                            monsterchoices = [room for room in rooms if map[room]["Floor"] == 1]
                            if "Left" in map[playerchoice]["Placement"]:
                                 narrowchoice = [room for room in monsterchoices if "Right" in map[playerchoice]]
                                 stuff = [narrowchoice]
                                 for i in monsterchoices:
                                        stuff.append(i)
                                 finalchoice = random.choice(stuff)
                                 return f"Monster chose {finalchoice}"
        
                            elif "Right" in map[playerchoice]["Placement"]:
                                 narrowchoice = [room for room in monsterchoices if "Left" in map[playerchoice]]
                                 stuff = [narrowchoice]
                                 for i in monsterchoices:
                                        stuff.append(i)
                                
                                 finalchoice = random.choice(stuff)
                                 return f"Monster chose {finalchoice}"
                    
                    elif playerchoice in rooms:
                         finalchoice = random.choice(rooms)
                         return f"Monster chose {finalchoice}"
                    if finalchoice == playerchoice:
                           #monster attacks player
                           monsterattack = True
                           turn -= 1
                    else:
                           turn -= 1
                    if turn == 0:
                        limit -= 1
                        playerturn = True
                    if limit == 0:
                            print("Game over! Your score was {score}")
                                               
    if level == 2:
        limit = 5
        if map[playerchoice]["Floor"] == map[monsterchoice]["Floor"] and limit > 0:
            
                            monsterchoices = [room for room in rooms if map[room]["Floor"] == map[playerchoice]["Floor"]]
                            choices = [""]
                            for i in monsterchoices:
                                   choices.append(i)
                            finalchoice = random.choice(choices)
                            return f"Monster chose {finalchoice}"
        if finalchoice == playerchoice:
                           monsterattack = True
                           turn -= 1
        else:
                           turn -= 1
        if turn == 0:
                    limit -= 1
                    playerturn = True
        if limit == 0:
                    level(level + 1)
         
    if level == 1:
         limit = 3
         turns = 1
         if playerchoice in rooms and  limit > 0:
              monsterchoice = random.choice(rooms)
              return f"Monster chose {monsterchoice}"
         if playerchoice == finalchoice:
            monsterattack == True
            turns = 0
            playerturn = True
              
         turns -= 1
         limit -= 1

         if limit == 0:
                 level(level + 1)   
