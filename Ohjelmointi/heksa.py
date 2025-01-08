def muotoile_heksaluvuksi(kokonaisluku, bit_lkm):
    heksaluku = hex(kokonaisluku)
    pituus = int(bit_lkm // 4)

    return heksaluku.lstrip("0x").zfill(pituus)

try:
    luku = int(input("Anna kokonaisluku: "))
    bitit = int(input("Anna heksaluvun pituus (bittien lukumäärä): "))
except ValueError:
    print("Kokonaisluku kiitos!")
else:
    tulos = muotoile_heksaluvuksi(luku, bitit)
    print(tulos)
