import unittest
from ostoskori import Ostoskori
from tuote import Tuote


class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.maito = Tuote("Maito", 5)
        self.vesi = Tuote("Vesi", 3)
        self.tuote3 = Tuote("Kahvi", 6)

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.setUp()
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    
    def test_kahden_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        self.setUp()
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.vesi)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    def test_kaksi_samaa_tuotetta(self):
        self.setUp()
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        self.setUp()
        self.kori.lisaa_tuote(self.maito)

        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        self.setUp()
        self.kori.lisaa_tuote(self.maito)

        ostos = self.kori.ostokset()[0]
        nimi = ostos.nimi()

        self.assertEqual(nimi, "Maito")

    def test_lisays_poisto(self):
        self.setUp()
        self.kori.lisaa_tuote(self.maito)

        self.kori.poista_tuote(self.maito)
        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 0)

    
    def test_tyhjenna_toimii(self):
        self.setUp()
        self.kori.lisaa_tuote(self.maito)

        self.kori.tyhjenna()
        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 0)