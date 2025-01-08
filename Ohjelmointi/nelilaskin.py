operaatio = input("Valitse operaatio (+, -, *, /): ")

if operaatio in ("+", "-", "*", "/"):
    try:
        luku1 = float(input("Anna luku 1: "))
        luku2 = float(input("Anna luku 2: "))
    except ValueError:
        print("Ei tämä ole mikään luku")
    else:
        if operaatio == "+":
            print(luku1 + luku2)
        elif operaatio == "-":
            print(luku1 - luku2)
        elif operaatio == "*":
            print(luku1 * luku2)
        elif operaatio == "/":
            if luku2 == 0:
                print("Tällä ohjelmalla ei pääse äärettömyyteen")
            else:
                print(luku1 / luku2)
else:
    print("Operaatiota ei ole olemassa")
