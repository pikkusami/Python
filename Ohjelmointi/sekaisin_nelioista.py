def laske_nelion_ala(sivu):
    return sivu ** 2
    
userInp = float(input("Anna neliön sivun pituus: "))
print("Neliön pinta-ala: " + str(round(laske_nelion_ala(userInp), 4)))
