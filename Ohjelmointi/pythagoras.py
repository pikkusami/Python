def laske_sivun_pituus(hypotenuusa):
    return hypotenuusa / (2 ** 0.5)

userInp = float(input("Anna tasakylkisen kolmion hypotenuusan pituus: "))

print("Kylkien pituus: " + str(round(laske_sivun_pituus(userInp), 4)))
