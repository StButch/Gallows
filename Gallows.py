import turtle
from time import sleep
import sys


def go_to_xy(x, y):
    t.up()
    t.goto(x, y)
    t.down()


def draw_line(from_x, from_y, to_x, to_y):
    go_to_xy(from_x, from_y)
    t.goto(to_x, to_y)


def erase(x, y):
    go_to_xy(x, y)
    t.color('white')
    t.begin_fill()
    t.begin_poly()
    for i in [600, 50] * 2:
        t.forward(i)
        t.left(90)
    t.end_poly()
    t.end_fill()


def draw_head(x, y, r):
    go_to_xy(x, y)
    t.circle(r)


functions = [draw_line] * 4 + [draw_head] + [draw_line] * 5


def draw_gibbet(step, coord):
    t.color('black')
    functions[step](*coord[step])


def draw_word():
    erase(-100, 100)
    t.color('black')
    go_to_xy(-100, 100)
    n = -1
    for y in word:
        n += 1
        z = word.index(y, n)
        go_to_xy(-100 + z * 20, 100)
        if y in otvet:
            t.write(f'{y}', font=('Arial', 28, 'normal'))
        else:
            t.write('*', font=('Arial', 28, 'normal'))


word = list(turtle.textinput('Игрок 1', 'Загадайте слово').lower())
t = turtle.Pen()
t.speed(0)
with open('coord.txt') as file:
    coord_list = [list(map(int, line.strip().split(', '))) for line in file]
# answer = turtle.textinput('Играть?','y/n')
# if answer == 'n':
#     sys.exit()
try_count = 0
otvet = ''
while True:
    draw_word()
    letter = turtle.textinput('Игрок 2', 'Введите букву').lower()
    if len(letter) == 1:
        if letter in word:
            erase(-250, 200)
            go_to_xy(-150, 200)
            t.color('green')
            t.write('Буква угадана', font=('Arial', 28, 'normal'))
            otvet += letter
            if set(otvet) == set(word):
                erase(-250, 200)
                go_to_xy(-150, 200)
                t.color('green')
                t.write('Ура вы победили!!!', font=('Arial', 28, 'normal'))
                draw_word()
                go_to_xy(-150, 150)
                t.color('green')
                t.write(f'Попыток потрачено: {try_count}', font=('Arial', 28, 'normal'))
                break

        else:
            erase(-250, 200)
            go_to_xy(-150, 200)
            t.color('red')
            t.write('Не верно(((', font=('Arial', 28, 'normal'))
            try_count += 1
            draw_gibbet(try_count - 1, coord_list)
            if try_count == 10:
                erase(-250, 200)
                go_to_xy(-150, 230)
                t.color('red')
                t.write('Вы проиграли(((', font=('Arial', 44, 'normal'))
                break
    else:
        erase(-250, 200)
        go_to_xy(-250, 200)
        t.color('black')
        t.write('Нужно ввести только одну букву!', font=('Arial', 28, 'normal'))

sleep(2)