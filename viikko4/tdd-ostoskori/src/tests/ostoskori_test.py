import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 3)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
    
    def test_kahden_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        vesi = Tuote("Vesi", 1)
        self.kori.lisaa_tuote(vesi)

        self.assertEqual(self.kori.hinta(), 4)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    def test_kaksi_samaa_tuotetta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 6)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset()[0]
        nimi = ostos.nimi()

        self.assertEqual(nimi, "Maito")

    def test_lisays_poisto(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.kori.poista_tuote(maito)
        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 0)

    
    def test_tyhjenna_toimii(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.kori.tyhjenna()
        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 0)