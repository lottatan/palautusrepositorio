from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostoskori = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        maara = 0
        for tuote in self.ostoskori:
            maara += Ostos(tuote).lukumaara()
        
        return maara

        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        hinta = 0
        for tuote in self.ostoskori:
            hinta += Ostos(tuote).hinta()
        
        return hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        if lisattava in self.ostoskori:
            Ostos(lisattava).muuta_lukumaaraa(1)
            self.ostoskori.append(lisattava)
        if lisattava not in self.ostoskori:
            self.ostoskori.append(lisattava)

    def poista_tuote(self, poistettava: Tuote):
        Ostos(poistettava).muuta_lukumaaraa(-1)

    def tyhjenna(self):
        self.ostoskori = []
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.ostoskori
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
