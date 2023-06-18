from fordulo import Fordulo

fordulok = []

def FajlOlvas():
    f = open('toto.txt', 'r', encoding='utf-8')
    f. readline()
    for sor in f:
        fordulok.append(Fordulo(sor))
    print('3.1 feladat: Adatok beolvasása és tárolása')
    f.close()

def GetTeliOssz():
    ossz = 0
    for fordulo in fordulok:
        ossz += fordulo.T13p1
    return ossz 

def CheckDontetlen():
    for fordulo in fordulok:
        if 'X' not in fordulo.Eredmeny:
            return True
    return False

# Főprogram:
print('3. feladat: Toto')
FajlOlvas()
print(f'3.2 feladat: Fogadási fordulók száma: {len(fordulok)}')
print(f'3.3 feladat: Telitalálatos szelvények száma: {GetTeliOssz()} darab')
if CheckDontetlen():
    print('3.4 feladat: Volt döntetlen mentes forduló')
else:
    print('3.4 feladat: Nem volt döntetlen mentes forduló')