from math import *

def muunna_xy_koordinaateiksi(kulma, pituus):
    x = int(round(pituus * cos(kulma)))
    y = int(round(pituus * sin(kulma)))
    
    return x, y

userKulma = float(input("Anna kulma radiaaineina: "))
userPituus= float(input("Anna osoitinvektorin pituus: "))

print("Koordinaatit (x, y): " + str(muunna_xy_koordinaateiksi(userKulma, userPituus)))
