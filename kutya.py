allatnev=["bodri", "blöki", "dézi"]
allatnem=["kan", "kan", "szuka"]

for i in range(0, len(allatnev),1):
    print("AZ első kuyta adata:", allatnev[i], allatnem[i])

class Kutya:
    def __init__(self, nev, nem): #konstruktor, beállítja paraméterek értékét, beállítsa az ADATTAGOKAT
        self.nev=nev #<-adattagok
        self.nem=nem
        #self= a SAJÁT paramétere

kutya1=Kutya("Bodri","kan")
kutya2=Kutya("Blöki","kan")
kutya3=Kutya("Dézi", "szuka")

print("A 2. kutya adata:", kutya2.nev, kutya2.nem)
print("A 1. kutya adata:", kutya1.nev, kutya1.nem)
print("A 3. kutya adata:", kutya3.nev, kutya3.nem)
