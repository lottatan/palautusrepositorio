import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()

    print("Players from FIN 2021-01-04 19:15:32.858661")
    #print(response)

    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'], player_dict["team"], player_dict["goals"], player_dict["assists"], player_dict["nationality"]
        )
        if player.nationality == "FIN":
            players.append(player)

    print("Oliot:")
    players.sort(key=lambda x: x.summa, reverse=True)

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
