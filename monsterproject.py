import random
import re
invalidname = False
monsterturn = False
hasweapon = False
playerchoice = str()
foundroom = str()
player = None
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = None
        self.current_room = None

    def take_damage(self, damage):
        self.health -= damage
        return self.health


    def boost_health(self):
        boost_health = random.choice([5, 10, 15, 20])
        self.health += boost_health
        print(f"{self.name} found a health boost! Gained {boost_health} HP.")
        return self.health
    def status(self):
        if self.health > 0:
            return "Alive"
        else:
            return "Dead"

    def equip_weapon(self, weapon):
         self.weapon = weapon


    def choose_room(self, game_map):
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
          return f"Player: {self.name}, Health: {self.health}, Current Room: {self.current_room}"

class Monster:
    def __init__(self, level, health=100, defense=5):
        self.level = level
        self.health = health
        self.defense = defense

    def take_damage(self, damage):
        # Reduces the monster's health based on incoming damage.
        self.health = self.health - damage
        self.health = self.health + self.defense
        return self.health
    def status(self):
        if self.health > 0:
            return "Alive"
        else:
            return "Dead"


    def __str__(self):
        # returns a string representation of the monster
        return (f"\nMonster Health: {self.health} Defense: {self.defense}")


class Weapon:
    def __init__(self, name, mod_damage):
        self.name = name
        self.mod_damage = mod_damage


    def __str__(self):
        return f"{self.name} with damage modifer of {self.mod_damage}"

weapon_storage = [ Weapon("Sword", 1.7),
                  Weapon("Hammer", 2.5),
                  Weapon("Dagger", 0.7),
                  Weapon("Spear", 1.0)]
def validate_player_name(name):
    """
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

    Parameters:
        player (object): The player initiating the attack.
        monster (object): The monster being attacked.
        weapon (object): The weapon being used for the attack.
        attack (str): The type of attack chosen by the player.

    Returns:
        bool: True if the attack was successful, False if the attack type was invalid.

    """
    
    attack = input("Choose your attack (Heavy, Medium, Light): ").capitalize()

    attack_types = {"Heavy": 30, "Attack": 20, "Light": 10}
    base_damage = attack_types[attack] if attack in attack_types else None
    if base_damage is None:
        print("Invalid attack choice! Monster takes advantage and attacks!\n")
        return False

    total_damage = base_damage * weapon.mod_damage
    monster.take_damage(total_damage)
    print(f"{player.name} used his {weapon.name}! Monster took {total_damage} damage!")
    return total_damage
    


with open('gamemap.json', r) as file:
    map = json.load(file)

rooms = [key for key in map]

l3map = map.copy()

del l3map[random.choice(rooms)]
l3rooms = [key for key in l3map]
l3rooms.pop(l3rooms.index(random.choice(l3rooms)))




def levels(level):

    """
    Creates a condition for the game according to the game's level. The higher the level the more options the monster has.
    Args:
        level (int): An integer used to set the level
    """
    if level <= 3:

        if level == 3:
            prev_health = None

            monster = Monster(3,100,3)
            weaponchance = ["yes","no","no","no"]
            gameplay = True
            hasweapon = False
            limit = 7
            while gameplay:
                print(f"LEVEL 3\tTurns: {limit}\n")
                print(str(player) + "\n")
                print(str(monster)+ "\n")
                playerchoice = player.choose_room(l3rooms)
                weapon = random.choice(weaponchance)
                if weapon == "yes":
                    yourweapon = random.choice(weapon_storage)
                    hasweapon = True
                    print(f"{player.name} got {str(yourweapon)}\n")
                    weaponchance = ["no", "no"]
                monsterturn = True
                while monsterturn:
                    foundroom = room_finder(playerchoice, map[playerchoice]["Floor"], level)
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
                            limit -= 1
                        elif hasweapon == False:
                            prev_health = player.health
                            pdmg = player.take_damage(random.randint(45,70))
                            if player.health < 50 and player.status() != "Dead":
                                    player.boost_health()
                            print(f"MONSTER hits {player.name} and {player.name} lost {prev_health - pdmg} HP\n")
                            limit -= 1
                    elif playerchoice != foundroom:
                        limit -= 1
                if player.status() == "Dead":
                      print(f"{player.name} is dead and the monster rips {player.name}'s heart out and makes a sandwich with it!")
                      gameplay = False
                if monster.status() == "Dead":
                     print(f"Monster is dead and {player.name} wins")
                     gameplay = False
                if limit == 0:
                      gameplay = False
                      print(f"Level {level} is done and the {player.name} survived!")

    if level == 2:
        prev_health = None
        monster = Monster(2,50,1.5)
        weaponchance = ["yes","yes","no","no"]
        gameplay = True
        hasweapon = False
        limit = 4
        while gameplay:
            print(f"LEVEL 2\tTurns: {limit}\n")
            print(str(player) + "\n")
            print(str(monster))
            playerchoice = player.choose_room(map)
            weapon = random.choice(weaponchance)
            if weapon == "yes":
                yourweapon = random.choice(weapon_storage)
                hasweapon = True
                print(f"{player.name} got {str(yourweapon)}\n")
                weapon = ["no", "no"]
            monsterturn = True
            while monsterturn:
                foundroom = room_finder(playerchoice, map[playerchoice]["Floor"], level)
                monsterturn = False
                if playerchoice == foundroom:
                    print(f"MONSTER IS IN THE SAME ROOM AS {player.name}!\n")
                    if hasweapon:
                        combat_sys(player, monster, yourweapon)
                        prev_health = player.health
                        pdmg = player.take_damage(random.randint(20,35))
                        print(f"MONSTER hits {player.name} and {player.name} lost {prev_health - pdmg} HP!\n")
                        limit -= 1
                    elif hasweapon == False:
                        prev_health = player.health
                        pdmg = player.take_damage(random.randint(20,35))
                        print(f"MONSTER hits {player.name} and player lost {prev_health -  pdmg} HP!\n")
                        limit -= 1
                elif playerchoice != foundroom:
                    limit -= 1
            if player.status() == "Dead":
                print(f"{player.name} is dead and the monster eats {player.name}'s flesh!")
                gameplay = False
            elif monster.status() == "Dead":
                    print(f"The monster is defeated! Onto the next level!\n")
                    gameplay = False
                    levels(level + 1)
            if limit == 0:
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
          limit = 3
          while gameplay:
                print(f"LEVEL 1\tTurns: {limit}\n")
                print(str(player) + "\n")
                print(str(monster))
                playerchoice = player.choose_room(map)
                weapon = random.choice(weaponchance)
                if weapon == "yes":
                    yourweapon = random.choice(weapon_storage)
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
                            limit -= 1
                        elif hasweapon == False:
                            prev_health = player.health
                            pdmg = player.take_damage(5)
                            print(f"MONSTER hits {player.name} and {player.name} lost {prev_health - pdmg} HP\n")
                            limit -= 1
                    elif playerchoice != foundroom:
                        limit -= 1
                if player.status() == "Dead":
                    print(f"{player.name} is dead and the monster eats {player.name}'s flesh!")
                    gameplay = False
                if monster.status() == "Dead":
                    print(f"Monster is defeated! Onto the next level!\n")
                    gameplay = False
                    levels(level + 1)
                if limit == 0:
                    gameplay = False
                    print(f"Level {level} is done! Moving to Level {level + 1}\n")
                    player.health = 100
                    levels(level + 1)

def room_finder(room, number, level):
    if level == 3:
        if number == 1:
            monsterchoices = [place for place in l3rooms if map[place]["Floor"] == 1]
            monsterchoices.append(room)
            finalchoice = random.choice(monsterchoices)
            print(f"Monster chose {finalchoice}\n")
            return finalchoice
        elif number == 2:
            monsterchoices = [place for place in l3rooms if map[place]["Floor"] == 2]
            monsterchoices.append(room)
            finalchoice = random.choice(monsterchoices)
            print(f"Monster chose {finalchoice}\n")
            return finalchoice

    if level == 2:
        if number == 1:
            monsterchoices = [place for place in rooms if map[place]["Floor"] == 1]
            monsterchoices.append(room)
            finalchoice = random.choice(monsterchoices)
            print(f"Monster chose {finalchoice}\n")
            return finalchoice
        elif number == 2:
            monsterchoices = [place for place in rooms if map[place]["Floor"] == 2]
            monsterchoices.append(room)
            finalchoice = random.choice(monsterchoices)
            print(f"Monster chose {finalchoice}\n")
            return finalchoice

def main():
    levels(1)
main()
