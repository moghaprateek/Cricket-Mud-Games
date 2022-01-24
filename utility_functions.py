from game_classes import PlayerData, Session
import constants
import random

###########################################
"""
All the cached data stored in the below Python Objects
"""
# Store Team Details Team Code : Team Name
teamDic = {}
# pace:spin:
bowlerDic = {}
# Store The Player Details
player_data = {}
# Store the Player game state
session = {}
pace_bowl_data = {}
spin_bowl_data = {}

###########################################


def validate_user_input(message, firstOption, lastOption):
    """
    This function is the common function for all the menu
    Validate the user input into number form and into range
    """
    inputRange = list(range(firstOption, lastOption+1))
    while True:
        try:
            value = int(input(message))
        except ValueError:
            print(constants.Input_Err_Message +
                  f" {firstOption} - {lastOption}")
            continue

        if not(value in inputRange):
            print(constants.Input_Err_Message +
                  f" {firstOption} - {lastOption}")
            continue
        else:
            break
    return value

############## Registration Flow   ######################


def print_player_details():
    """
    Print The Player Details from the cached data
    """
    for a, b in player_data.items():
        b.showPlayerDetails()


def store_player(playerObj):
    """
    This Function Store The new register data in player file.
    """
    player_data[playerObj.gameId] = playerObj

    f = open("data_files/PlayerData.txt", "a")
    temp = "\n"+playerObj.showPlayerDetails()
    f.write(temp)
    f.close()


def reload_player_data():
    """
    This function reload the data from text file to re run the previous game.
    """
    with open('data_files/PlayerData.txt') as f:
        for line in f:
            gameId, name, age, gender = line.split("|")
            gameId = int(gameId.strip())
            name = name.strip()
            age = int(age.strip())
            gender = gender.strip()
            playerData = PlayerData(gameId, name, age, gender)
            player_data[playerData.gameId] = playerData


def verify_game_id(gameId):
    """
    This function validate the previous session in file or not.
    """
    reload_player_data()
    if gameId in player_data:
        return True
    else:
        return False


def check_session(game_id):
    """
    This function reload the previous session from the data.
    """
    matching_lines = [line for line in open(
        'data_files/session.txt').readlines() if constants.UNFINISHED in line]
    for sess in matching_lines:
        game_id, team_code, over, ball, runs, bowlerId, status, trophy = sess.split(
            "|")
        game_id = game_id.strip()
        team_code = team_code.strip()
        over = int(over.strip())
        ball = int(ball.strip())
        runs = int(runs.strip())
        bowlerId = bowlerId.strip()
        status = status.strip()
        trophy = trophy.strip()
        session_obj = Session(game_id, team_code, over,
                              ball, runs, bowlerId, status, trophy)
        session[session_obj.game_id] = session_obj

    if game_id in session:
        session_obj = session.get(game_id)
        return session_obj
    else:
        return ""


def check_last_score(game_id):
    """
    This function reload the previous session from the data.
    """
    matching_lines = [line for line in open(
        'data_files/session.txt').readlines() if constants.FINISHED in line]
    score_dic = {}
    for sess in matching_lines:
        game_id, team_code, over, ball, runs, bowlerId, status, trophy = sess.split(
            "|")
        game_id = game_id.strip()
        team_code = team_code.strip()
        over = int(over.strip())
        ball = int(ball.strip())
        runs = int(runs.strip())
        bowlerId = bowlerId.strip()
        status = status.strip()
        trophy = trophy.strip()
        session_obj = Session(game_id, team_code, over,
                              ball, runs, bowlerId, status, trophy)
        score_dic[session_obj.game_id] = session_obj

    if game_id in score_dic.keys():
        session_obj = score_dic.get(game_id)
        return constants.Last_Score.format(session_obj.runs)
    else:
        return constants.No_Last_Score


def check_game_id(message, err):
    """
    Verify the game id from the register file.
    """
    while True:
        try:
            value = int(input(message))
            if value == 0:
                break
        except ValueError:
            print(err)
            continue

        if verify_game_id(value):
            break
        else:
            print(constants.Game_Id_Not_Found)
            continue

    return value


def validate_input(message, err, tag):
    """
    Validate the player details and store it in text file
    """
    value = ""
    if tag == "NAME":
        while True:
            value = input(message)
            if not (len(value.strip()) > 0):
                print(err)
                continue
            else:
                break
    if tag == "AGE":
        while True:
            try:
                value = int(input(message))
            except ValueError:
                print(err)
                continue
            else:
                break
    if tag == "GENDER":
        while True:
            value = input(message)
            if not (len(value.strip()) > 0 and (value == "M" or value == "F")):
                print(err)
                continue
            else:
                break
    if tag == "GAMEID":
        while True:
            try:
                value = int(input(message))
            except ValueError:
                print(err)
                continue

            if verify_game_id(value):
                print(constants.Game_id_Used_Err_Message)
                continue
            else:
                break

    return value


def get_player_details(player_dic):
    """
    Getting Player Details for registration
    Store in text file
    """
    print(constants.Register_Message)

    name = validate_input(constants.Enter_Name,
                          constants.Name_Err_Message, "NAME")
    age = validate_input(constants.Enter_Age,
                         constants.Age_Err_Message, "AGE")
    gender = validate_input(constants.Enter_Gender,
                            constants.Gender_Err_Message, "GENDER")
    game_id = validate_input(constants.Enter_Custom_Game_Id,
                             constants.Game_id_Err_Message, "GAMEID")

    store_player(PlayerData(game_id, name, age, gender))

    return True
############## Registration Flow   ######################

##### Start Game Menu #####


def generate_team_menu():
    """
    Using cached team data to build team menu.
    """
    count = 1
    menu = ""
    for teamCode, team in teamDic.items():
        menu = menu+str(count)+"."+team+"\n"
        count = count+1
    return menu


def generate_team(user_input):
    """

    """
    tmp = list(teamDic)
    index = tmp[user_input-1]
    return index


def game_rules(message, err):
    """
    Create the menu to start the game 
    """
    value = ""
    while True:
        value = input(message).lower()
        if not len(value.strip()) > 0:
            print(err)
        if 'y' in value:
            break
        elif 'e' in value:
            break
        else:
            continue
    return value

##### Start Game Menu #####
### Session ###


def create_new_session(game_id):
    """
    Create the New game session for the player to start the game
    """
    session = Session(game_id, "", 0, 0, 0, "",
                      constants.UNFINISHED, "")
    return session


def find_bowler_id(session_obj, last_obj):
    """
    Using the cached bowler data and find the random bowler id 
    """
    b_list = bowlerDic.get(session_obj.team_code).bowler_list
    bowler_obj = random.choice(b_list)
    while True:
        if last_obj.bowler_type == "":
            return bowler_obj
        else:
            if last_obj.bowlerId == bowler_obj.bowlerId:
                bowler_obj = random.choice(b_list)
            else:
                return bowler_obj


def find_random_ball(ball_type, last_bowl):
    """
    using the cached the bowl data and find the random ball
    On every call
    """
    obj_val = random_ball_func(ball_type)
    while True:
        if len(last_bowl) == 0:
            return obj_val
        else:
            if last_bowl[0] == obj_val[0]:
                obj_val = random_ball_func(ball_type)
            else:
                return obj_val


def random_ball_func(ball_type):
    if ball_type == "PACE":
        temp = list(pace_bowl_data.items())
        obj_val = random.choice(temp)
        return obj_val
    elif ball_type == "SPIN":
        temp = list(spin_bowl_data.items())
        obj_val = random.choice(temp)
        return obj_val

### Session ###


def write_session(session_obj_run):
    """
    Remove the player old session and write it into file.
    """
    temp_session_dic = {}
    final_session_list = []

    with open('data_files/session.txt') as f:
        for sess in f:
            game_id, team_code, over, ball, runs, bowlerId, status, trophy = sess.split(
                "|")
            game_id = game_id.strip()
            team_code = team_code.strip()
            over = over.strip()
            ball = ball.strip()
            runs = runs.strip()
            bowlerId = bowlerId.strip()
            status = status.strip()
            trophy = trophy.strip()
            session_obj = Session(game_id, team_code, over,
                                  ball, runs, bowlerId, status, trophy)
            temp_session_dic[session_obj.game_id +
                             session_obj.status] = session_obj

    status = False
    for k, v in temp_session_dic.items():
        if k == str(session_obj_run.game_id)+constants.UNFINISHED:
            if status:
                continue
            v.game_id = session_obj_run.game_id
            v.team_code = session_obj_run.team_code
            v.over = session_obj_run.over
            v.ball = session_obj_run.ball
            v.runs = session_obj_run.runs
            v.bowlerId = session_obj_run.bowlerId
            v.status = session_obj_run.status
            v.trophy = session_obj_run.trophy
            final_session_list.append(v)
            status = True
        else:
            final_session_list.append(v)

    if status == False:
        final_session_list.append(session_obj_run)
    value = ""

    for sess_obj in final_session_list:
        value = value+sess_obj.show_session()+'\n'

    write_session_file(value)


def write_session_file(final_data):
    """
    This function write the session into file with file handler.
    """
    f = open("data_files/session.txt", "w")
    f.write(final_data)
    f.close()
