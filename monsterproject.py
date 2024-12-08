import random
playerturn = False
monsterturn = False
monsterdead = False
monsterattack = False
hasweapon = False
playerchoice = str()
turn = 0

foundroom = str()
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = None
        self.stamina = 100
        self.current_room = None

    def take_damage(self, damage):
        self.health -= damage
        return self.health


    def boost_health(self):
        boost_health = random.choice([5, 10, 15, 20])
        self.health += boost_health
        print(f"{self.name} found a health boost! Gained {boost_health} health.")
        self.health = min(max(self.health, 0), 100)
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
        return (f"Monster\n"
                 f"Health: {self.health}\n"
                 f"Defense: {self.defense}")

player = Player("Bob")

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
rooms = [key for key in map]

def levels(level):

    """
    Creates a condition for the game according to the game's level. The higher the level the more options the monster has.
    Args:
        level (int): An integer used to set the level
    """
    if level <= 3:

        if level == 3:
            prev_health = None
            monster = Monster(3,100,30)
            weaponchance = ["yes","no","no","no"]
            gameplay = True
            hasweapon = False
            limit = 8
            while gameplay:
                room_to_be_taken = random.choice(rooms)
                print("LEVEL 3")
                print(str(player))
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
                      print(f"Monster chose {foundroom}")
                      monsterturn = False
                      if playerchoice == foundroom:
                            print(f"MONSTER IS IN THE SAME ROOM AS {player.name}\n")
                            if hasweapon:
                                dmg = monster.take_damage(20 * yourweapon.mod_damage)
                                print(f"MONSTER has been damaged by {player.name}'s {yourweapon.name} and lost {dmg} HP!\n\n")
                                prev_health = player.health
                                pdmg = player.take_damage(random.randint(45,70))
                                print(f"MONSTER hits {player.name} and {player.name} took {prev_health - pdmg} HP\n")
                                limit -= 1
                                playerturn = True
                            elif hasweapon == False:
                                        prev_health = player.health
                                        pdmg = player.take_damage(random.randint(45,70))
                                        print(f"MONSTER hits {player.name} and {player.name} lost {prev_health - pdmg} HP\n")
                                        limit -= 1
                                        playerturn = True
                      elif playerchoice != foundroom:
                            limit -= 1
                            playerturn = True
                if player.status() == "Dead":
                      print(f"{player.name} is dead and the monster cooks {player.name}'s brains with some scrambled eggs!")
                      gameplay = False
                if monster.status() == "Dead":
                     print(f"Monster is dead and {player.name} wins")
                     gameplay = False
                if limit == 0:
                      playerturn = False
                      gameplay = False
                      print(f"Level {level} is done! Moving to Level {level + 1}")
                      player.health = 100
                      levels(level + 1)
    if level == 2:
            prev_health = None
            monster = Monster(2,50,5)
            weaponchance = ["yes","yes","no","no"]
            gameplay = True
            hasweapon = False
            limit = 3
            while gameplay:
                print("LEVEL 2")
                print(str(player) + "\n")
                playerchoice = player.choose_room(map)
                weapon = random.choice(weaponchance)
                if weapon == "yes":
                       yourweapon = random.choice(weapon_storage)
                       hasweapon = True
                       print(f"{player.name} got {str(yourweapon)}\n")
                       weapon = ["no", "no"]
                monsterturn = True
                while monsterturn :
                     foundroom = room_finder(playerchoice, map[playerchoice]["Floor"], level)
                     monsterturn = False
                     if playerchoice == foundroom:
                            print(f"MONSTER IS IN THE SAME ROOM AS {player.name}!")
                            if hasweapon:
                                dmg = monster.take_damage(random.randint(10,29) * yourweapon.mod_damage)
                                print(f"MONSTER has been damaged by {player.name}'s {yourweapon.name} and lost {dmg} HP!\n\n")
                                prev_health = player.health
                                pdmg = player.take_damage(random.randint(30,55))
                                print(f"MONSTER hits {player.name} and {player.name} took {prev_health - pdmg} HP\n")
                                limit -= 1
                                playerturn = True
                            elif hasweapon == False:
                                        prev_health = player.health
                                        pdmg = player.take_damage(random.randint(30,55))
                                        player.take_damage(random.randint(30,50))
                                        print(f"MONSTER hits player! and player took {prev_health -  pdmg} HP\n")
                                        limit -= 1
                                        playerturn = True


                     elif playerchoice != foundroom:
                        limit -= 1
                        playerturn = True
                if player.status() == "Dead":
                    print(f"{player.name} is dead and the monster eats {player.name}'s flesh!")
                    gameplay = False
                elif monster.status() == "Dead":
                     print(f"The monster is defeated")
                     gameplay = False
                if limit == 0:
                    playerturn = False
                    gameplay = False
                    print(f"Level {level} is done! Moving to Level {level + 1}")
                    player.health = 100
                    levels(level + 1)
    if level == 1:
          prev_health = None
          monster = Monster(1,40,5,5)
          weaponchance = ["yes","yes","yes","no"]
          gameplay = True
          hasweapon = False
          limit = 3
          while gameplay:
                print("LEVEL 1")
                print(str(player) + "\n")
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
                      print(f"Monster chose {foundroom}")
                      monsterturn = False
                      if playerchoice == foundroom:
                            print(f"MONSTER IS IN THE SAME ROOM AS {player.name}\n")
                            if hasweapon:
                                dmg = monster.take_damage(50 * yourweapon.mod_damage)
                                print(f"MONSTER has been damaged by {player.name}'s {yourweapon.name} and lost {dmg} HP!\n\n")
                                prev_health = player.health
                                pdmg = player.take_damage(5)
                                print(f"MONSTER hits {player.name} and {player.name} took {prev_health - pdmg} HP\n")
                                limit -= 1
                                playerturn = True
                            elif hasweapon == False:
                                        player.take_damage(5)
                                        print(f"MONSTER hits {player.name} and {player.name} lost {prev_health - pdmg} HP\n")
                                        limit -= 1
                                        playerturn = True
                      elif playerchoice != foundroom:
                            limit -= 1
                            playerturn = True
                if player.status() == "Dead":
                      print(f"{player.name} is dead and the monster eats {player.name}'s flesh!")
                      gameplay = False

                if limit == 0:
                      playerturn = False
                      gameplay = False
                      print(f"Level {level} is done! Moving to Level {level + 1}")
                      player.health = 100
                      levels(level + 1)

def room_finder(room, number, level):
    if level == 3:
        if number == 1:
                monsterchoices = [place for place in rooms if map[place]["Floor"] == 1]
                if "Left" in map[room]["Placement"]:
                    narrowchoice = [room for room in monsterchoices if "Right" in map[room]["Placement"]]
                    narrowchoice.append(room)
                    finalchoice = random.choice(narrowchoice)
                    print(f"Monster chose {finalchoice}")
                    return finalchoice
                elif "Right" in map[room]["Placement"]:
                    narrowchoice = [room for room in monsterchoices if "Left" in map[room]["Placement"]]
                    narrowchoice.append(room)
                    finalchoice = random.choice(narrowchoice)
                    print(f"Monster chose {finalchoice}")
                    return finalchoice
        elif number == 2:
            monsterchoices = [place for place in rooms if map[place]["Floor"] == 2]
            if "Left" in map[room]["Placement"]:
                narrowchoice = [place for place in monsterchoices if "Right" in map[place]["Placement"]]
                narrowchoice.append(room)
                finalchoice = random.choice(narrowchoice)
                print(f"Monster chose {finalchoice}")
                return finalchoice
            elif "Right" in map[room]["Placement"]:
                narrowchoice = [room for room in monsterchoices if "Left" in map[room]["Placement"]]
                narrowchoice.append(room)
                finalchoice = random.choice(narrowchoice)
                print(f"Monster chose {finalchoice}")
                return finalchoice
    elif level == 2:
            if number == 1:
                monsterchoices = [place for place in rooms if map[place]["Floor"] == 1]
                finalchoice = random.choice(monsterchoices)
                print(f"Monster chose {finalchoice}")
                return finalchoice
            if number == 2:
                monsterchoices = [place for place in rooms if map[place]["Floor"] == 2]
                finalchoice = random.choice(monsterchoices)
                print(f"Monster chose {finalchoice}")
                return finalchoice


def main():
      levels(1)

main()
