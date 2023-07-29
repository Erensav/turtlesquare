import turtle
from turtle import *
renk = ["pink","dark red","blue","lime","gold","magenta","dark violet","dark slate blue","aquamarine","cyan","DeepPink","DarkRed","pink","dark red","blue","lime","gold","magenta","dark violet"]
kenar = 0
boy = 150
rsayi =0
t = turtle.Turtle()
while kenar <= 10 :
    t.color(renk[rsayi])
    rsayi += 1
    t.forward(boy)
    t.left(90)
    t.color(renk[rsayi])
    rsayi += 1
    t.forward(boy)
    t.left(90)
    t.color(renk[rsayi])
    rsayi += 1
    t.forward(boy)
    t.left(90)
    t.color(renk[rsayi])
    rsayi += 1
    t.forward(boy)
    t.left(90)
    t.color(renk[rsayi])
    rsayi -= 3

    kenar += 1
    boy = boy - 10

done()
