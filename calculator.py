# Создать калькулятор для работы с рациональными и комплексными числами,
# организовать меню, добавив в неё систему логирования.

import draw_board, my_ui, repeat_calc
from my_ui import write_line, in_int, in_act, in_txt, in_comp
from integer import integer
from calc_fraction import calc_fraction
from complex_num import complex_num


def simple_calc():
    draw_board.draw_board()
    while True:
        write_line("Выберите числовое множество для ввода: целое число 'I', рациональное 'R' или комплексное 'C'")
        set_sel = in_txt("> ").upper()
        if set_sel == "I":
            write_line("Приступим к вычислению челых чисел!")
            num1 = int(in_int("x: "))
            num2 = float(in_int("y: "))
            act = in_act()
            integer(act, num1, num2)
        elif set_sel == "R":
            write_line("Приступим к вычислению рациональных чисел!")
            act = in_act()
            a = int(in_int("Делитель_1: "))
            b = int(in_int("Делимое_1: "))
            c = int(in_int("Делитель_2: "))
            d = int(in_int("Делимое_2: "))
            calc_fraction(act, a, b, c, d)
        elif set_sel == "C":
            write_line("Приступим к вычислению комлексных чисел!")
            comp_first = in_comp('Введите первое комплексное число: ')
            comp_two = in_comp('Введите второе комплексное число: ')
            comp_act = in_act()
            write_line(complex_num(comp_first, comp_two, comp_act))
        else:
            write_line("Жмакай 'I' или 'R' или 'C'")
        while True:
            f = in_txt('ещё раз?\n').upper()
            if f == 'Y':
                simple_calc()
            elif f == 'N':
                write_line("Chao!")
                exit()
            else:
                write_line("Выберите "'y'" или "'n'"")

simple_calc()