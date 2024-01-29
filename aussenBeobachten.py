from wetterBeobachter import WetterBeobachter


class AussenBeobachter(WetterBeobachter):
    def __init__(self, wetterstation, außen):
        super().__init__(wetterstation, außen)

    def update(self,temperature):
        #print("Information von der Wetterstation von außen erhalten".temperature)
        self.wetterstation.antwort("Rückmeldung vom Außenbeobachter")
        print(temperature)


