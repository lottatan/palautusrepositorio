from statistics1 import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or

class QueryBuilder:
    def __init__(self, query):
        self.query = query

    def build(self):
        return self.query

    def playsIn(self, team):
        return QueryBuilder(And(self.query), PlaysIn(team))

    def hasAtLeast(self, amount, goals):
        return QueryBuilder(And(self.query), HasAtLeast(amount, goals))

    def hasFewerThan(self, amount, goals):
        return QueryBuilder(And(self.query), HasFewerThan(amount, goals))

    def oneOf(self, m1, m2):
        return QueryBuilder(Or(m1, m2))
