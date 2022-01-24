class BowlerClass:
    """
    Class Bind The Bowler Data attribute
    """

    def __init__(self, bowler_type, bowlerId, bowlerName):
        self.bowlerId = bowlerId
        self.bowlerName = bowlerName
        self.bowler_type = bowler_type

    def showData(self):
        print(f"{self.bowler_type} | {self.bowlerId} | {self.bowlerName}")


class TeamClass:
    """
    Class Bind The Team Data attribute
    """

    def __init__(self, teamCode, teamName, bowler_list):
        self.teamCode = teamCode
        self.teamName = teamName
        self.bowler_list = bowler_list

    def showTeam(self):
        print(f"teamCode : {self.teamCode} | teamName : {self.teamName}")
        for tmp in self.bowler_list:
            tmp.showData()


class ShotClass:
    """
    Class Bind The Shot Details and Score Data attribute
    """

    def __init__(self, shot_list, score_list):
        self.shot_list = shot_list
        self.score_list = score_list

    def show_shorts(self):
        print(f"shot_list : {self.shot_list} | score_list : {self.shot_list}")

class PlayerData:
    """
    Class Bind The Player Data attribute
    """

    def __init__(self, gameId, name, age, gender):
        self.gameId = gameId
        self.name = name
        self.age = age
        self.gender = gender

    def showPlayerDetails(self):
        print(f"{self.gameId}|{self.name}|{self.age}|{self.gender}")
        return f"{self.gameId}|{self.name}|{self.age}|{self.gender}"


class Session:
    """
    Class Bind The Player Session with stage and status Data attribute
    """

    def __init__(self, game_id, team_code, over, ball, runs, bowlerId, status, trophy):
        self.game_id = game_id
        self.team_code = team_code
        self.over = over
        self.ball = ball
        self.runs = runs
        self.bowlerId = bowlerId
        self.status = status
        self.trophy = trophy

    def show_session(self):
        output_str = f"{self.game_id}|{self.team_code}|{self.over}|{self.ball}|{self.runs}|{self.bowlerId}|{self.status}|{self.trophy}"
        return output_str
