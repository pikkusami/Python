from turtle import *

def piirra_nelio(sivu, x, y):
    # tähän funktio joka piirtää neliön
    # joko punaisena tai sinisenä riippuen
    # siitä onko aloituspisteen x-koordinaatti
    # positiivinen (sininen) vai negativiinen
    # (punainen)

    up()
    if x >= 0:
        goto(x, y)
        down()
        begin_fill()
        color("blue")
        forward(sivu)
        right(90)
        forward(sivu)
        right(90)
        forward(sivu)
        right(90)
        forward(sivu)
        end_fill()
    else:
        goto(x, y)
        down()
        begin_fill()
        color("red")
        forward(sivu)
        right(90)
        forward(sivu)
        right(90)
        forward(sivu)
        right(90)
        forward(sivu)
        end_fill()
        
    
piirra_nelio(40, -100, 100)
piirra_nelio(60, 100, -100)
piirra_nelio(100, -50, -20)
piirra_nelio(80, 90, 30)
done()
