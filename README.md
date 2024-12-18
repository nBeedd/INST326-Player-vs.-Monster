# Monster Vs. Player Game
* In our game, players will face a monster as they move through different rooms. There are three levels, each with a stronger monster. Players can find weapons by chance and use them. There are also health jars that appear randomly to help players regenerate their health.
* **MAKE SURE TO TYPE EVERYTHING EXACTLY AS IT IS PROMPTED TO YOU WHEN ASKED FOR INPUT OR ELSE MONSTER WILL TAKE ADVANTAGE.**

## Purpose of Each File
* monstervsplayer.py: This file contains the main game logic, including classes for Player, Monster, and Weapon, as well as functions for combat and gameplay levels.
* gamemap.json: This file stores the map layout for the game, detailing rooms and their respective floors.

## How to Run Our Program
Assuming you have already downloaded the monstervsplayer.py and gamemap.json on your computer, follow these steps:
1. Open the monstervsplayer.py file on VS Code.
2. In the main function set the levels function with the level(1 - 3) and turns to your liking.
3. Open the Terminal.
4. Run the command **python3 monstervsplayer.py** if you are a Mac user or **python monstervsplayer.py** for a Windows user to start the game.

## How to Use Our Program
* **Input**: The program will prompt you to enter your player name and choose rooms during gameplay. Follow the prompts and enter choices as instructed.
* **Output**: The game will display the player's name, the player's status (his health level), and the current room he/she is in. It will also display how many turns the player has left and move onto different levels until the player or the monster is dead.

 ## Each Member's contribution
 | Method/Function | Primary Author | Techniques Demonstrated
| --- | --- | --- |
| boost_health | Abhishek Subedi | Key Function | 
| str | Abhishek Subedi | Magic Method | 
| validate_player_name | Edras Tlapechco | Regular Expression | 
| combat_sys | Edras Tlapechco | Conditional Expression |
| jsonopener | Ahmed Babikir | Json.dump() |
| init | Ahmed Babikir | Optional Parameters |
| levels | Eli Jean | F-strings Containing Expressions |
| room_finder | Eli Jean | Comprehensions |

