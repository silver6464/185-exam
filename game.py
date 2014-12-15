class Game(object):
    def __init__(self):
        self.teams = {}

    def add_team(self, team):
        self.teams[team.name] = team.score

    def get_team_score(self, team):
        return self.teams.get(team.name)

    def add_score(self,team,score):
        self.teams[team.name] += score
