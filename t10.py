import tkinter
from math import *
from random import randint

SCREEN_SIZE = (600, 600)


def xs(x):
    return SCREEN_SIZE[0] // 2 + x


def ys(y):
    return SCREEN_SIZE[1] // 2 - y


main = tkinter.Tk()
canvas = tkinter.Canvas(main, bg='white', height=SCREEN_SIZE[1], width=SCREEN_SIZE[0])
canvas.create_line((xs(0), ys(SCREEN_SIZE[1] // 2)), xs(0), ys(-SCREEN_SIZE[1] // 2), fill='#336699')
canvas.create_line((xs(-SCREEN_SIZE[0] // 2), ys(0)), xs(SCREEN_SIZE[0] // 2), ys(0), fill='black')


class Vektor:
    def __init__(self, x=None, y=None, l=None, a=None):
        if x is not None and y is not None:
            self.x = x
            self.y = y
        elif l is not None and a is not None:
            self.x = l
            self.y = 0
            if a != 0:
                v1 = self.rotate(a)
                self.x = v1.x
                self.y = v1.y

    def rotate(self, a):
        a = a / 180 * pi
        x = self.x * cos(a) - self.y * sin(a)
        y = self.x * sin(a) + self.y * cos(a)
        return Vektor(x, y)


class NUgolnik:
    def __init__(self, amount, side_length, starting_angle, speed, color):

        self.speed = speed
        self.color = color

        self.phi = 360 / amount
        self.radius = side_length / (2 * sin(self.phi / 360 * pi))
        v0 = Vektor(l=self.radius, a=0)
        v1 = Vektor(l=self.radius, a=0)

        self.s = []
        ss = []

        for i in range(0, amount):
            v2 = Vektor(x=v1.x - v0.x, y=v1.y - v0.y)
            v2 = v2.rotate(180 + starting_angle)
            self.s.append(v2.x)
            self.s.append(v2.y)
            ss.append(xs(v2.x))
            ss.append(ys(v2.y))
            v1 = v0.rotate(self.phi * (i + 1))

        red = hex(randint(0, 255)).split('x')[-1]
        green = hex(randint(0, 255)).split('x')[-1]
        blue = hex(randint(0, 255)).split('x')[-1]
        color = '#' + red.zfill(2) + green.zfill(2) + blue.zfill(2)

        self.canvas_object = canvas.create_polygon(ss, fill=color, width=3, outline=self.color)

    def rotate(self, angle):
        ss = [0] * len(self.s)
        for j in range(len(self.s) // 2):
            v3 = Vektor(x=self.s[2 * j], y=self.s[2 * j + 1]).rotate(angle * self.speed)
            ss[2 * j], ss[2 * j + 1] = xs(v3.x), ys(v3.y)
        canvas.coords(self.canvas_object, ss)


def value_map(range_min, range_max, value_min, value_max, value):
    range_total = range_max - range_min
    value_total = value_max - value_min
    if value > value_max:
        value = value_max
    if value < value_min:
        value = value_min
    if value_total > 0:
        return int(value / value_total * range_total)


polygons = []
polygons_amount = 128
for n in range(polygons_amount):
    nn = value_map(0, 1536, 0, polygons_amount, n)
    if 0 <= nn <= 255:
        red = hex(255).split('x')[-1]
        green = hex(nn % 256).split('x')[-1]
        blue = hex(0).split('x')[-1]
    if 256 <= nn <= 511:
        red = hex(255 - nn % 256).split('x')[-1]
        green = hex(255).split('x')[-1]
        blue = hex(0).split('x')[-1]
    if 512 <= nn <= 767:
        red = hex(0).split('x')[-1]
        green = hex(255).split('x')[-1]
        blue = hex(nn % 256).split('x')[-1]
    if 768 <= nn <= 1023:
        red = hex(0).split('x')[-1]
        green = hex(255 - nn % 256).split('x')[-1]
        blue = hex(255).split('x')[-1]
    if 1024 <= nn <= 1279:
        red = hex(nn % 256).split('x')[-1]
        green = hex(0).split('x')[-1]
        blue = hex(255).split('x')[-1]
    if 1280 <= nn <= 1535:
        red = hex(255).split('x')[-1]
        green = hex(0).split('x')[-1]
        blue = hex(255 - nn % 256).split('x')[-1]
    color = '#' + red.zfill(2) + green.zfill(2) + blue.zfill(2)

    size = value_map(0, 300, 0, polygons_amount, n)

    polygons.append(NUgolnik(randint(2, 2), 350 - size, 0, (n+1) / (polygons_amount/10), color))


def rotate(alpha):
    alpha += 1
    for n in range(polygons_amount):
        polygons[n].rotate(alpha)
    main.after(30, rotate, alpha)


rotate(0)
canvas.pack()
main.mainloop()