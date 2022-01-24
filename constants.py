# Normal Introduction Message
WelcomeMessage = """
█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█   █▀▀ █▀█ █ █▀▀ █▄▀ █▀▀ ▀█▀   █▀▄▀█ █░█ █▀▄   █▀▀ ▄▀█ █▀▄▀█ █▀▀
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█   █▄▄ █▀▄ █ █▄▄ █░█ ██▄ ░█░   █░▀░█ █▄█ █▄▀   █▄█ █▀█ █░▀░█ ██▄ \n"""
SelectOption = "Please Select the option from the Menu"
RegisterOption = "You Are Successfully Register To Game, Please Select the option from the Menu to Start Game"
ExitMessage = "Bye Bye !! Thanks For Playing the Game.\n Do you want to play again? (y or n)\n"
Register_Message = "Welcome to New User Register Menu"
Enter_Name = "Provide Your Full Name\n >"
Enter_Age = "Provide Your Age in Digits\n >"
Enter_Gender = "Provide Your Gender M for Male & F for Female\n >"
Enter_Custom_Game_Id = "Provide Your Customer Game Id\n >"
Game_Menu_Game_Id = "Provide Your Register Game Id to Start the Game\n >"
Exit_Game_Err = "Your Select Wrong Input!! Restart the Game \n"
### Err Message ###
Input_Err_Message = "Provide Valid Input In Range\n >"
Name_Err_Message = "Provide Valid Full Name\n >"
Age_Err_Message = "Provide Valid Age\n >"
Gender_Err_Message = "Provide Valid Gender M or F\n >"
Game_id_Err_Message = "Provide Valid Game Id\n"
Game_id_Used_Err_Message = "Choose New Game Id , Provided Game Id Already In Use\n >"
Game_Id_Not_Found = "Game Id Not Found Register To Game Again."
Game_Rule_Err = "Provide valid input to start the game\n >"
# Status
UNFINISHED = "UF"
OUT = "L"
FINISHED = "F"
QUIT = "q"
MAX_OVER = "2"
MAX_BALL = "6"
Delay_Time = "2"
### Status ###
# Menu Message
MainMenu = "1.Register\n2.Start Game\n3.Exit\n >"
StartGameMenuWelcomeMessage = "Welcome to the Cricket MUD Game {}"
StartGameMenu = "1.New Game\n2.Resume Game\n3.Exit \n4.Last Score \n >"
SelectTeam = "Select Your Team Your Want to Play Against"
Game_Rules = "\nTo Start the Game Press y\nTo Exit The Game Press e\n"
Bowler_Menu = "{} bowled you {} bowl.\n\nWhat shot you want to play.\n"
String_Space = "--------------------------------------------\n>"
Out_Menu = "Oh So Sorry.You are \n{}.\n\nYour Final Score {}"
final_score = "Score Card Runs:{} Over-{}/Ball-{} \n"
New_Over_Start = "Over Number {} finished.. Keep Going. New Over Started \n"
Last_Over_Message = "You have Successfully Complete The Game And Scored {} Runs.\nYou Have Won {} Trophy"
Shot_Message = "You Hit\n"
Exit_Command = "\nIf You want to Exit Game Press 0\n"
Exit_Command_2 = "{}.Exit\n"
No_Unfinished_Game = "You Don,t Have Unfinished Game,Your New Game Started\n"
Last_Score = "Your last game score is {}."
No_Last_Score = "There is no last score.Play the game and improve you score again"
############# Text Art ##############
One = """
╱╭╮
╭╯┃
╰╮┃
╱┃┃
╭╯╰╮
╰━━╯"""
Second = """
╭━━━╮
┃╭━╮┃
╰╯╭╯┃
╭━╯╭╯
┃┃╰━╮
╰━━━╯"""
Third = """
╭━━━╮
┃╭━╮┃
╰╯╭╯┃
╭╮╰╮┃
┃╰━╯┃
╰━━━╯"""
Four = """
╭╮╱╭╮
┃┃╱┃┃
┃╰━╯┃
╰━━╮┃
╱╱╱┃┃
╱╱╱╰╯"""
Five = """
╭━━━╮
┃╭━━╯
┃╰━━╮
╰━━╮┃
╭━━╯┃
╰━━━╯"""
Six = """
╭━━━╮
┃╭━━╯
┃╰━━╮
┃╭━╮┃
┃╰━╯┃
╰━━━╯"""
Neg_One = """
██████╗░░█████╗░░██╗░░░░░░░██╗██╗░░░░░███████╗██████╗░
██╔══██╗██╔══██╗░██║░░██╗░░██║██║░░░░░██╔════╝██╔══██╗
██████╦╝██║░░██║░╚██╗████╗██╔╝██║░░░░░█████╗░░██║░░██║
██╔══██╗██║░░██║░░████╔═████║░██║░░░░░██╔══╝░░██║░░██║
██████╦╝╚█████╔╝░░╚██╔╝░╚██╔╝░███████╗███████╗██████╔╝
╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝╚═════╝░"""

RULES = """
---------------------------------------------------------------
█▀▀ █▀█ █ █▀▀ █▄▀ █▀▀ ▀█▀   █▀▀ ▄▀█ █▀▄▀█ █▀▀   █▀█ █░█ █░░ █▀▀
█▄▄ █▀▄ █ █▄▄ █░█ ██▄ ░█░   █▄█ █▀█ █░▀░█ ██▄   █▀▄ █▄█ █▄▄ ██▄
---------------------------------------------------------------
** RULE 1: You have total {} over to play cricket.
** RULE 2: Every over have 6 balls.
** RULE 3: First You have to choose the opponent team you want to play.
** RULE 4: A random bowler selected by the system from your choosen team.
** RULE 5: Bowler bowls you the random delivey and shots for you to play.
** RULE 6: If you score 10 runs or below you will get Bronze Trophy.
** RULE 7: If you score 10 to 25 runs you will get Silver Trophy.
** RULE 8: If you score 25 to 50 runs you will get Gold Trophy.
** RULE 9: If you score above 50 runs you will get Diamond Trophy.
** RULE 10: Game have features to start the new game or resume the previous game.
---------------------------------------------------------------
"""
Trophy = """ 
─█▀▀▀█▀█─
──▀▄░▄▀──
────█────
──▄▄█▄▄──
"""
Bronze = """
██████╗░██████╗░░█████╗░███╗░░██╗███████╗███████╗
██╔══██╗██╔══██╗██╔══██╗████╗░██║╚════██║██╔════╝
██████╦╝██████╔╝██║░░██║██╔██╗██║░░███╔═╝█████╗░░
██╔══██╗██╔══██╗██║░░██║██║╚████║██╔══╝░░██╔══╝░░
██████╦╝██║░░██║╚█████╔╝██║░╚███║███████╗███████╗
╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝╚══════╝╚══════╝"""
Silver = """
░██████╗██╗██╗░░░░░██╗░░░██╗███████╗██████╗░
██╔════╝██║██║░░░░░██║░░░██║██╔════╝██╔══██╗
╚█████╗░██║██║░░░░░╚██╗░██╔╝█████╗░░██████╔╝
░╚═══██╗██║██║░░░░░░╚████╔╝░██╔══╝░░██╔══██╗
██████╔╝██║███████╗░░╚██╔╝░░███████╗██║░░██║
╚═════╝░╚═╝╚══════╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝"""
Gold = """
░██████╗░░█████╗░██╗░░░░░██████╗░
██╔════╝░██╔══██╗██║░░░░░██╔══██╗
██║░░██╗░██║░░██║██║░░░░░██║░░██║
██║░░╚██╗██║░░██║██║░░░░░██║░░██║
╚██████╔╝╚█████╔╝███████╗██████╔╝
░╚═════╝░░╚════╝░╚══════╝╚═════╝░"""
Diamond = """
██████╗░██╗░█████╗░███╗░░░███╗░█████╗░███╗░░██╗██████╗░
██╔══██╗██║██╔══██╗████╗░████║██╔══██╗████╗░██║██╔══██╗
██║░░██║██║███████║██╔████╔██║██║░░██║██╔██╗██║██║░░██║
██║░░██║██║██╔══██║██║╚██╔╝██║██║░░██║██║╚████║██║░░██║
██████╔╝██║██║░░██║██║░╚═╝░██║╚█████╔╝██║░╚███║██████╔╝
╚═════╝░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░"""
Bat = """
────▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀█─█
▀▀▀▀▄─█─█─█─█─█─█──█▀█
─────▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀─▀
"""
