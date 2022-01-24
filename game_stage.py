from os import utime
from game_classes import BowlerClass
import cached_data as cacheData
import constants as constant
import time


def main_menu(message):
    '''
    In this Function we load the first menu for the user.
    Menu Be Like Register - Login - Exit
    Based on User input, We will go to next stage.
    '''
    print(constant.String_Space+constant.WelcomeMessage+constant.String_Space)
    print(message)
    userInput = cacheData.util.validate_user_input(constant.MainMenu, 1, 3)

    if userInput == 1:
        if cacheData.util.get_player_details(cacheData.util.player_data):
            main_menu(constant.RegisterOption)
    elif userInput == 2:
        start_menu()
    elif userInput == 3:
        play_again()
    else:
        print(constant.Exit_Game_Err)

# function to ask play again or not


def play_again():
    '''
    In this function , We check the user input to start the game or leave the game.
    '''
    print(constant.String_Space+constant.ExitMessage+constant.String_Space)

    # convert the player's input to lower_case
    answer = input(">").lower()

    if "y" in answer:
        main_menu(constant.SelectOption)
    # if player typed "yes" or "y" start the game from the beginning
    else:
        exit()
    # if user types anything besides "yes" or "y", exit() the program


def start_menu():
    '''
    In this Function we verify the user details before start the game.
    If user is already register to the game then game will start.
    Else if user is not verified to game then user need to register to game.
    '''
    game_id = cacheData.util.check_game_id(constant.String_Space+constant.Game_Menu_Game_Id+constant.Exit_Command+constant.String_Space,
                                           constant.Game_id_Err_Message)
    if game_id == 0:
        play_again()

    
    print(constant.String_Space+constant.StartGameMenuWelcomeMessage.format(
        cacheData.util.player_data[game_id].name))
    print(constant.SelectOption)
    user_input = cacheData.util.validate_user_input(
        constant.StartGameMenu+constant.String_Space, 1, 4)
    sessionObj = cacheData.util.create_new_session(game_id)
    if user_input == 1:
        select_team(sessionObj)
    elif user_input == 2:
        resume_game(sessionObj)
    elif user_input == 3:
        play_again()
    elif user_input == 4:
        score_check = cacheData.util.check_last_score(game_id)
        print("\n"+score_check+"\n")
        play_again()
    else:
        print(constant.Exit_Game_Err)


def select_team(sessionObj):
    '''
    In this Function, We create the dynamic team menu for the user selection.
    Based on user input team is selected.
    '''
    print(constant.String_Space+constant.SelectTeam)
    print(constant.SelectOption)

    user_input = cacheData.util.validate_user_input(
        cacheData.util.generate_team_menu()+constant.Exit_Command_2.format(len(cacheData.util.teamDic)+1)+constant.String_Space, 1, len(cacheData.util.teamDic)+1)
    if user_input == len(cacheData.util.teamDic)+1:
        play_again()

    sessionObj.team_code = cacheData.util.generate_team(user_input)
    user_input = cacheData.util.game_rules(constant.RULES.format(constant.MAX_OVER) +
                                           constant.Game_Rules+constant.String_Space, constant.Game_Rule_Err)
    if 'y' in user_input:
        start_over(sessionObj)
    if 'e' in user_input:
        play_again()


def resume_game(session_obj):
    '''
    In this Function we check the user old session and start the previous game
    If user dont have previous game then we need to start the new game.
    '''
    last_session = cacheData.util.check_session(session_obj.game_id)
    if last_session == "":
        print(constant.String_Space +
              constant.No_Unfinished_Game+constant.String_Space)
        select_team(session_obj)
    else:
        user_input = cacheData.util.game_rules(constant.RULES.format(constant.MAX_OVER) +
                                               constant.Game_Rules+constant.String_Space, constant.Game_Rule_Err)
        if 'y' in user_input:
            start_over(last_session)
        if 'e' in user_input:
            play_again()


def start_over(session_obj):
    '''
    This Function control the Over , Handle the Out , Change the Over
    Control the Player Trophy.
    '''
    last_bowl_obj = BowlerClass("", "", "")
    while True:
        bowlerObj = cacheData.util.find_bowler_id(session_obj, last_bowl_obj)
        last_bowl_obj = bowlerObj
        session_obj.bowlerId = bowlerObj.bowlerId
        bowler_type = bowlerObj.bowler_type
        session_obj = play_overs(session_obj, bowlerObj, bowler_type)
        print_trophy_menu = ""
        if session_obj.status == constant.OUT:
            print(constant.Out_Menu.format(constant.Neg_One, session_obj.runs))
            print_trophy_menu = check_trophy(session_obj)

            print(constant.String_Space+constant.Last_Over_Message.format(
                session_obj.runs, print_trophy_menu+"\n")+constant.String_Space)
            session_obj.status = constant.FINISHED
            cacheData.util.write_session(session_obj)
            play_again()
            return

        if session_obj.status == constant.QUIT:
            session_obj.status = constant.UNFINISHED
            cacheData.util.write_session(session_obj)
            play_again()
            return

        session_obj.over = session_obj.over+1
        session_obj.ball = 0

        if session_obj.over >= int(constant.MAX_OVER):
            print_trophy_menu = check_trophy(session_obj)
            print(constant.String_Space+constant.Last_Over_Message.format(
                session_obj.runs, print_trophy_menu+"\n")+constant.String_Space)
            session_obj.status = constant.FINISHED
            cacheData.util.write_session(session_obj)
            return

        print(constant.String_Space +
              constant.New_Over_Start.format(session_obj.over)+constant.String_Space)

        time.sleep(int(constant.Delay_Time))


def check_trophy(session_obj):
    '''
    Check for the player trophy.
    Based on the player run scored, trophy awarded
    '''
    print_trophy_menu = ""
    if session_obj.runs <= 10:
        session_obj.trophy = "Bronze"
        print_trophy_menu = constant.Bronze+" " + constant.Trophy
    elif session_obj.runs <= 25 and session_obj.runs > 10:
        session_obj.trophy = "Silver"
        print_trophy_menu = constant.Silver + " " + constant.Trophy
    elif session_obj.runs <= 50 and session_obj.runs > 25:
        session_obj.trophy = "Gold"
        print_trophy_menu = constant.Gold + " " + constant.Trophy
    elif session_obj.runs > 50:
        session_obj.trophy = "Diamond"
        print_trophy_menu = constant.Diamond + " " + constant.Trophy
    return print_trophy_menu


def play_overs(session_obj, bowlerObj, bowler_type):
    '''
    In this Function we create the menu for the user with ball , bowler name , shot into menu
    Based on the user input what shot you have to play and score achive.
    '''
    bowl = []
    while True:
        bowl = cacheData.util.find_random_ball(bowler_type, bowl)
        shortObj = bowl[1]
        output = constant.Bowler_Menu.format(bowlerObj.bowlerName, bowl[0])

        final_score_menu = constant.final_score.format(
            session_obj.runs, session_obj.over+1, session_obj.ball+1)

        short_menu = ""
        count = 1
        for shorts in shortObj.shot_list:
            short_menu = f"{short_menu}{count}.{shorts} \n"
            count = count+1

        user_input = cacheData.util.validate_user_input(constant.String_Space +
                                                        output+short_menu+constant.Exit_Command_2.format(len(shortObj.shot_list)+1)+constant.String_Space+final_score_menu+constant.String_Space, 1, len(shortObj.shot_list)+1)

        if user_input == len(shortObj.shot_list)+1:
            session_obj.status = constant.QUIT
            return session_obj

        score = shortObj.score_list[user_input-1]
        if int(score) == -1:
            session_obj.status = constant.OUT
            return session_obj

        print_shot_message(score)
        session_obj.runs = session_obj.runs+int(score)
        session_obj.ball = session_obj.ball+1
        if session_obj.ball == int(constant.MAX_BALL):
            return session_obj


def print_shot_message(score):
    '''
    This Function create the Score and Image for the Console Output.
    '''
    if int(score) == 1:
        print(constant.Shot_Message+" "+constant.Bat+" "+constant.One)
    elif int(score) == 2:
        print(constant.Shot_Message+" "+constant.Bat+" "+constant.Second)
    elif int(score) == 3:
        print(constant.Shot_Message+" "+constant.Bat+" "+constant.Third)
    elif int(score) == 4:
        print(constant.Shot_Message+" "+constant.Bat+" "+constant.Four)
    elif int(score) == 5:
        print(constant.Shot_Message+" "+constant.Bat+" "+constant.Five)
    elif int(score) == 6:
        print(constant.Shot_Message+" "+constant.Bat+" "+constant.Six)