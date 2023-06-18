class Fordulo:

    def __init__(self, sor):
        adatok = sor.strip().split(';')
        self.Ev = int(adatok[0])
        self.Het = int(adatok[1])
        self.ford = int(adatok[2])
        self.T13p1 = int(adatok[3])
        self.Ny13p1 = int(adatok[4])
        self.Eredmeny = adatok[5]