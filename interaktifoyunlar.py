import turtle
import time
import random

es = turtle.Turtle()
wn = turtle.Screen()

wn.title("cizim oyunu")
wn.bgcolor("yellow")


def yazi(name, x, y, size):
    es.up()
    es.hideturtle()
    es.goto(x, y)
    es.color("black")
    es.write(name, align="center", font=("Arilal", size, "normal"))
#zaman
def gerisayim(num):
    saat = turtle.Turtle()
    saat.up()
    saat.hideturtle()
    saat.speed(1)
    saat.color("black")
    saat.goto(-50, 200)
    for i in range(num, -1, -1):
        saat.clear()
        if i == 0:
            saat.color("black")
            saat.goto(-20, 200)
            saat.write("Game Over! ", font=("Arilal", 15, "normal"))
            break
        saat.write(f"Time:{i}", font=("Arilal", 20, "normal"))
        time.sleep(1)

top = turtle.Turtle()

top.shape("turtle")
top.up()
top.goto(random.randint(-180, 180), random.randint(-180, 180))












yazi("Yakalama Oyunu", 0, 250, 25)
gerisayim(4)








wn.mainloop()