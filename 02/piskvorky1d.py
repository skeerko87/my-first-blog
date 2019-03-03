import random  # (příp. import jiných věci, které budou potřeba)

def tah(pole, cislo_policka, symbol):
    """Vrátí pole s daným symbolem umístěným na danou pozici"""
    ...

def tah_hrace(pole):
    """Zeptá se hráče kam chce hrát a vrátí pole se zaznamenaným tahem"""
    ...
    input('Kam chceš hrát? ')
    ...

def piskvorky1d():
    """Spustí hru

    Vytvoří hrací pole a střídavě volá tah_hrace a tah_pocitace
    dokud někdo nevyhraje"""
    while ...:
        ...
        tah_hrace(...)
        ...

# Puštění hry!
piskvorky1d()
