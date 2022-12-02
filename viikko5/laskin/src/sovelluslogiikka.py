class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.aiempi = 0

    def miinus(self, arvo):
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.aiempi = self.tulos
        self.tulos = arvo
    
    def kumoa(self):
        self.tulos = self.aiempi
