verouudistus = {
    "jaa": 0,
    "ei": 0,
    "eos": 0,
    "virhe": 0
}
nalle_puh_presidentiksi = {
    "jaa": 12,
    "ei": 0,
    "eos": 5,
    "virhe": 4
}

def aanesta(sanakirja):
    print("Suoritetaanko verouudistus?")
    vastaus = input("Anna äänesi, vaihtoehdot ovat: jaa, ei, eos ").lower()
    
    if vastaus not in ("jaa", "ei", "eos"):
        sanakirja["virhe"] += 1
    else:
        sanakirja[vastaus] += 1

def nayta_tulokset(sanakirja):
    print("Jaa  : {}".format(chr(35) * sanakirja["jaa"]))
    print("Ei   : {}".format(chr(35) * sanakirja["ei"]))
    print("Eos  : {}".format(chr(35) * sanakirja["eos"]))
    print("Virhe: {}".format(chr(35) * sanakirja["virhe"]))

aanesta(verouudistus)
nayta_tulokset(verouudistus)
aanesta(nalle_puh_presidentiksi)
nayta_tulokset(nalle_puh_presidentiksi)
