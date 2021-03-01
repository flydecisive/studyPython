import turtle

t = turtle.Pen()
sides = int(turtle.numinput("Ввод сторон", "Какое количество сторон хотите выбрать?", 4, 1, 8))

colors = ["black", "red", "green", "orange", "blue", "purple", "pink", "brown"]

for x in range(360):
    t.color(colors[x%sides])
    t.circle(x)
    t.left(360 / sides)