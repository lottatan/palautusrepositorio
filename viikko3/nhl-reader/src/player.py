import requests

class Player:
    def __init__(self, name, team, goals, assists, nationality):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
        self.summa = self.goals + self.assists
        self.nationality = nationality
    
    def __str__(self):
        return f"{self.name:20} {self.team} {self.assists} + {self.goals} = {self.summa}"

class PlayerReader:
    def __init__(self, url):
        self.reader = requests.get(url).json()



class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = []
        for player_dict in self.reader.reader:
            player = Player(
                player_dict['name'], player_dict["team"], player_dict["goals"], player_dict["assists"], player_dict["nationality"]
            )
            if player.nationality == nationality:
                players.append(player)

        players.sort(key=lambda x: x.summa, reverse=True)

        return players
