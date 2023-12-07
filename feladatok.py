def osszegzes(kismacska): #itt a lista helyére bármit lehetne irni mert onnan tudja hogy melyik lista kell hogy ugyanaz a metódus van megadva a mainben
    osszeg=0
    for szam in range(0,len(kismacska),1):
        # osszeg+=szam
        osszeg+=kismacska
    # print(osszeg) -> ezt igy nem tudom másik metódusban/metódussal felhasználni, csak ha RETURNt használjuk
    return osszeg # ha nincs return sehol nem tudom az eredményét kiolvasni!!!