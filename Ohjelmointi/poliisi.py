try:
    matka = float(input("Anna auton kulkema matka (m): "))
    aika = float(input("Anna matkaan kulunut aika (s): "))
except ValueError:
    print("Ei näin")
else:
    nopeus = 3.6 * matka / aika
    print(f"{matka:.2f} metriä {aika:.2f} sekunnissa kulkeneen auton nopeus on {nopeus:.2f} km/h")
