# Game Data Loading Before Game Starts
# Load  Teams
from game_classes import BowlerClass, TeamClass, ShotClass, PlayerData, Session
import utility_functions as util
import constants as constants
import os

# Load Team Details


def load_team():
    """
    This function load the team data from text file.
    """
    try:
        if os.stat('data_files/teamFile.txt').st_size == 0:
            print(f"Team Data File Is Empty")
            return False
        else:
            with open('data_files/teamFile.txt') as f:
                for line in f:
                    code, name = line.split(",")
                    code = code.strip()
                    name = name.strip()
                    util.teamDic[code] = name
        for k, v in util.teamDic.items():
            print(f'Team Code : {k} | Team Name : {v}')
        return True
    except FileNotFoundError:
        print("File Not Found For Teams Data")
        return False

# Loading Bowler Details for every team
# ind:


def load_bowler_data():
    """
    This function load the bowler data
    """
    try:
        if os.stat("data_files/bowlerFile.txt").st_size == 0:
            print(f"Bowler Data File Is Empty")
            return False
        else:
            for k, v in util.teamDic.items():
                matching_lines = [line for line in open(
                    'data_files/bowlerFile.txt').readlines() if k in line]

                bowler = []
                for tmp in matching_lines:
                    tCode, pType, pCode, pName = tmp.split(",")
                    tCode = tCode.strip()
                    pCode = pCode.strip()
                    pType = pType.strip()
                    pName = pName.strip()
                    print(f"Bowler : {tCode}:{pCode}:{pType}:{pName}")
                    bowler.append(BowlerClass(pType, pCode, pName))
                game = TeamClass(k, v, bowler)
                util.bowlerDic[game.teamCode] = game

            for k, v in util.bowlerDic.items():
                v.showTeam()
        return True

    except FileNotFoundError:
        print("File Not Found For Bowler Data")
        return False

# Load Type of Bowls


def load_bowl_data():
    """
    Load the pace and spin bowler data from the text file
    """
    try:
        if os.stat("data_files/bowlData.txt").st_size == 0:
            print(f"Bowl Data File Is Empty")
            return False
        else:
            with open('data_files/bowlData.txt') as f:
                for line in f:
                    bowl_type, shots = line.split(",")
                    type, bowl = bowl_type.split("|")
                    if type == "PACE":
                        shotList, scoreList = shots.split(":")
                        util.pace_bowl_data[bowl] = ShotClass(
                            shotList.split("|"), scoreList.split("|"))
                    elif type == "SPIN":
                        shotList, scoreList = shots.split(":")
                        util.spin_bowl_data[bowl] = ShotClass(
                            shotList.split("|"), scoreList.split("|"))
            print(f"{util.pace_bowl_data} - {util.spin_bowl_data}")
        return True

    except FileNotFoundError:
        print("File Not Found For Bowl Data")
        return False
# Load Player Data from File


def load_player_data():
    """
    Load the player data from text file for verification purpose or restore old data.
    """
    try:
        with open('data_files/PlayerData.txt') as f:
            for line in f:
                gameId, name, age, gender = line.split("|")
                gameId = gameId.strip()
                name = name.strip()
                age = age.strip()
                gender = gender.strip()
                playerData = PlayerData(gameId, name, age, gender)
                util.player_data[playerData.gameId] = playerData
            print(f"Player Dic Data {util.player_data}")
        return True
    except FileNotFoundError:
        print("File Not Found For Player Data")
        return False

# Load User Session From File


def load_session():
    """
    Load the old session into game when start the game.
    """
    try:

        matching_lines = [line for line in open(
            'data_files/session.txt').readlines() if constants.UNFINISHED in line]
        for sess in matching_lines:
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
            util.session[session_obj.game_id] = session_obj

        return True
    except FileNotFoundError:
        print("File Not Found For Session Data")
        return False


def check_cached_data():
    """
    This function handle all the check for the loading of data.
    If any issue happened or file not found then game will not start
    """
    flag = False
    try:
        if load_team() and len(util.teamDic) > 0:
            if load_bowler_data() and len(util.bowlerDic) > 0 and len(util.bowlerDic) == len(util.teamDic):
                if load_bowl_data() and len(util.pace_bowl_data) > 2 and len(util.spin_bowl_data) > 2:
                    if load_player_data() and load_session():
                        print(
                            f"------------------- Game Data Loaded Success Fully ----------------------------")
                        flag = True
                        return flag

        return flag
    except Exception:
        print("Exception While Loading The Data")
        return flag
