class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = player1_name
        self.player2 = player2_name
        self.score1 = 0
        self.score2 = 0
        self.scoret = ["Love", "Fifteen", "Thirty", "Forty"]

    def won_point(self, player_name):
        if player_name == "player1":
            self.score1 += 1
        else:
            self.score2 += 1

    def get_score(self):
        if self.score1 == self.score2:
            return self.tasapeli()
        if self.score1 >= 4 or self.score2 >= 4:
            return self.johto_tai_voitto()
        return self.peli_jatkuu()


    def tasapeli(self):
        if self.score1 < 4:
            tulos = self.scoret[self.score1]
            score = f"{tulos}-All"
        else:
            score = "Deuce"

        return score
    
    def johto_tai_voitto(self):
        minus_result = self.score1 - self. score2

        if minus_result == 1:
            score = "Advantage player1"
        elif minus_result == -1:
            score = "Advantage player2"
        elif minus_result >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"

        return score
    
    def peli_jatkuu(self):
        score1 = self.scoret[self.score1]
        score2 = self.scoret[self.score2]

        score = f"{score1}-{score2}"

        return score