# Cricket-Mud-Games

######################################################################
Using this document we understand the game configurations and each file descriptions.

data_files : Folder in root directory contains all the file to store and load the game data.
bowlData.txt > This file contains the various types of bowl and shot played against them. We can configure 
               the new bowls to the game and shots with score mapping.
bowlerFile.txt > This file contains the various bowler in different teams in the game.Data consists 
                 bowler id,name,team code and bowler type.
teamFile.txt > This file contains the various team data with team code and name.

PlayerData.txt > This file contains the register player details to game.Data contains game id , name , age , gender
session.txt > This file contains the previous session of every player with finished or unfinised game.Data contains game id , team code,over
              ball, runs , bowler id , game status (F for finished/UN for unfinised) , trophy.                  

######################################################################
Game configurations before start :
In constants.py file MAX_OVER value can change the game from 2 to 3 overs.

To start the game :
1. Run the main.py file in python terminal.
