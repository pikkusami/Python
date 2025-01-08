from turtle import *

def piirra_ympyra(x, y, sade):
    # kirjoita funktion sisälle koodi
    # joka piirtää ympyrän tehtävänannon 
    # mukaisesti käyttäen muuttujia
    # x, y ja sade
    up()
    goto(x, y-sade)
    down()
    circle(sade)

piirra_ympyra(50, 50, 30)
piirra_ympyra(-50, 50, 30)
piirra_ympyra(0, 0, 60)
up()
setx(0)
sety(0)
done()
