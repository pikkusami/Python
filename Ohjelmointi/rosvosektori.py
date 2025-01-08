import math

def laske_sektorin_ala(sade, kulma):
    return (kulma / 360) * math.pi * sade ** 2

userSade = float(input("Anna ympyrän säde: "))
userKulma = float(input("Anna sektorin sisäkulma asteina: "))

print("Sektorin pinta-ala " + str(round(laske_sektorin_ala(userSade, userKulma), 4)))
