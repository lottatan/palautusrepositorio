import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(PlayerReaderStub())

    def test_search_toimii(self):
        player = self.statistics.search("Semenko")
        self.assertAlmostEqual(str(player), "Semenko EDM 4 + 12 = 16")

    def test_search_ei_toimi(self):
        player = self.statistics.search("Tanner")
        self.assertAlmostEqual(player, None)

    def test_palauttaa_joukkueen(self):
        team = self.statistics.team("EDM")
        maara = len(team)
        self.assertAlmostEqual(maara, 3)

    def test_top_pisteet(self):
        pelaajat = self.statistics.top(0, 1)
        tulos = []
        for pelaaja in pelaajat:
            tulos.append(pelaaja.name)

        self.assertEqual(pelaaja.name,"Gretzky")

    def test_top_maalit(self):
        pelaajat = self.statistics.top(0, 2)
        tulos = []
        for pelaaja in pelaajat:
            tulos.append(pelaaja.name)

        self.assertEqual(pelaaja.name, "Lemieux")

    def test_top_syotot(self):
        pelaajat = self.statistics.top(0, 3)
        tulos = []
        for pelaaja in pelaajat:
            tulos.append(pelaaja.name)

        self.assertEqual(pelaaja.name, "Gretzky")