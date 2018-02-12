import tkinter
from math import *
from Vektor import Vektor
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
AKSIOM = 'F++F++F++F'
STARTING_ANGLE = pi / 2
ANGLE = pi / 4
NEW_F = 'F-F++F-F'
STEPS = 3
LENGTH = 300//2**STEPS

DRAW_RULES = [
    ['line',['F','H']],
    ['move',['A','B']]
]

#DRAW_RULES[0][1][1] - 'H'

RULES = [
    ['F','F-F++F-F'],
    ['G','G'],
    ['H','FF'],
    ['A','A'],
    ['B','FBF'],
    ['C','ABC']
]


def new_formula(steps):
    formula = AKSIOM
    for i in range(steps):
        formula = formula.replace('F', NEW_F, -1)
    return formula


class Cherepashka:
    def __init__(self, x0, y0, alpha):
        self.x0 = x0
        self.y0 = y0
        self.alpha = alpha
        self.length = LENGTH

        self._process_formula(new_formula(STEPS))

    def _lineto(self, x1, y1):
        canvas.create_line((xs(self.x0), ys(self.y0)), xs(x1), ys(y1), fill='black')
        self.x0 = x1
        self.y0 = y1

    def _moveto(self, x1, y1):
        self.x0 = x1
        self.y0 = y1

    def _nextxy(self):
        x1 = self.x0 + self.length * cos(self.alpha)
        y1 = self.y0 + self.length * sin(self.alpha)
        return x1, y1

    def _rotate(self, direction):
        if direction == '+':
            self.alpha += ANGLE
        else:
            self.alpha -= ANGLE

    def _line(self):
        x, y = self._nextxy()
        self._lineto(x,y)

    def _process_formula(self, formula):
        formula = list(formula)
        for l in formula:
            if l=='F':
                self._line()
            elif l=='+' or l=='-':
                self._rotate(l)


tortilla = Cherepashka(0,0,pi/2)
canvas.pack()
main.mainloop()
