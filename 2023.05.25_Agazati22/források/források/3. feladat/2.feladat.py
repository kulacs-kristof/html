import random

print('2. feladat: Halmaz-e?')

def CheckHalmaz(lista):
    for szam in lista:
        db = 0
        for ell in lista:
            if szam == ell:
                db += 1
        if db > 1:
            return False
    return True

for i in range(8):
    lista = []
    for j in range(5):
        lista.append(random.randint(0,9))
    print(f'{i + 1}. {lista} -> ', end='')
    if CheckHalmaz(lista):
        print('Halmaznak tekinthető!')
    else:
        print('Halmaznak nem tekinthető!')
