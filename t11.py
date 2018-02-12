import tkinter
from math import *
from random import randint

SCREEN_SIZE = (600, 600)


def xs(x):
    return SCREEN_SIZE[0] // 2 + x


def ys(y):
    return SCREEN_SIZE[1] // 2 - y


def oxs(x):
    return x - SCREEN_SIZE[0] // 2


def oys(y):
    return SCREEN_SIZE[1] // 2 - y


class Screen:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def w(self):
        return self.width

    def h(self):
        return self.height


scr = Screen(SCREEN_SIZE[0], SCREEN_SIZE[1])

main = tkinter.Tk()
canvas = tkinter.Canvas(main, bg='white', height=scr.h(), width=scr.w())
canvas.create_line((xs(0), ys(scr.h() // 2)), xs(0), ys(-scr.h() // 2), fill='#336699')
canvas.create_line((xs(-scr.w() // 2), ys(0)), xs(scr.w() // 2), ys(0), fill='black')
coords = []
n = int(input())
for i in range(n):
    coords.append(randint(-scr.w() // 2, scr.w() // 2))
    coords.append(randint(-scr.h() // 2, scr.h() // 2))

print(coords)

my_beautiful_polygon = canvas.create_polygon(coords, fill='white', width=3,outline = 'red')


def reddraw_polygon():
    canvas.coords(my_beautiful_polygon,coords)


def remove_point(event):
    coords.pop()
    coords.pop()
    print(coords)
    reddraw_polygon()



def add_point(event):
    coords.append(event.x)
    coords.append(event.y)
    print(coords)
    reddraw_polygon()







canvas.bind('<Button 1>', add_point)
canvas.bind('<Button 3>', remove_point)

canvas.pack()
main.mainloop()
