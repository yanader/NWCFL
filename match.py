class Match:
    def __init__(self, home_team: str, away_team: str, competition: str):
        self.__home_team = home_team
        self.__away_team = away_team
        self.__competition = competition
        self.__reported_scores = []

    def add_score(self, score: str):
        parts = score.split('-')
        self.__reported_scores.append((parts[0], parts[1]))
