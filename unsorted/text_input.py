# import turtle
# name = turtle.textinput("Введите свое имя", "Как тебя зовут?")
# turtle.Pen().write(name)

import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green", "orange", "purple", "white", "gray"]

#name = turtle.textinput("Введите свое имя", "Как тебя зовут?")
sides = int(turtle.numinput("Сколько сторон", "Сколько сторон вы хотите (1 - 8)?", 
        4, 1, 8))

for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x * 3 / sides + x)
    #t.write(name, font = ("Times New Roman", int((x + 4) / 4), "bold"))
    t.left(360 / sides + 1)
    t.width(x * sides / 200)
