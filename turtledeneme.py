import turtle
from turtle import *
title("                   kaplumbaga        cizimi        sanati")
bgcolor("red")
kaplumbaga2 = turtle.Turtle()
kaplumbaga = turtle.Turtle()
kap3 = turtle.Turtle()
kaplumbaga.color("white")
#hilal cizimi
kaplumbaga2.color("white")
kaplumbaga2.up()
kaplumbaga2.begin_fill()
kaplumbaga2.goto(-150,0)
kaplumbaga2.down()
kaplumbaga2.circle(120)
kaplumbaga2.end_fill()

kaplumbaga2.up()
kaplumbaga2.goto(-120,31)
kaplumbaga2.down()
kaplumbaga2.color("red")
kaplumbaga2.begin_fill()
kaplumbaga2.circle(95)
kaplumbaga2.end_fill()
kaplumbaga2.color("white")

#yildiz cizimi
yildiz = 0
kaplumbaga.up()
kaplumbaga.goto(20,50)
kaplumbaga.down()
kaplumbaga.begin_fill()
while yildiz <= 4 :
    kaplumbaga.left(54)
    kaplumbaga.forward(160)
    kaplumbaga.left(90)
    yildiz += 1
kaplumbaga.end_fill()
kaplumbaga.color("red")

#dikdortgen
kap3.color("white")
kap3.up()
kap3.goto(0,-40)
kap3.down()
kap3.forward(300)
kap3.left(90)
kap3.forward(300)
kap3.left(90)
kap3.forward(650)
kap3.left(90)
kap3.forward(300)
kap3.left(90)
kap3.forward(350)



done()




