import math

def laske_nelio_ala(sivun_pituus):
    return sivun_pituus ** 2

def laske_sektorin_ala(sade, sisakulma):
    return (sisakulma / 360) * math.pi * sade ** 2

def laske_sivun_pituus(hypotenuusa):
    return hypotenuusa / (2 ** 0.5)

def laske_kuvion_ala(x):
    pieni_nelio = laske_nelio_ala(x)
    
    pieni_sade = laske_sivun_pituus(x)
    
    kolmio = pieni_sade ** 2 / 2
    pieni_sektori = laske_sektorin_ala(pieni_sade, 45)
    
    iso_sivu = laske_sivun_pituus(x) * 2
    
    iso_nelio = iso_sivu ** 2
    iso_sektori = laske_sektorin_ala(iso_sivu, 270)
    
    return pieni_nelio + kolmio + pieni_sektori + iso_nelio + iso_sektori


userInp = float(input("Anna x: "))
print("Kuvion ala: " + str(round(laske_kuvion_ala(userInp), 4)))
