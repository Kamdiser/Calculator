import div, mult, diff, sum
from fractions import Fraction
from my_ui import write_line


def calc_fraction(act, a, b, c, d):
    if act == "+":
        write_line(sum.sum(Fraction(a, b), Fraction(c, d)))
    elif act == "-":
        write_line(diff.diff(Fraction(a, b), Fraction(c, d)))
    elif act == "*":
        write_line(mult.mult(Fraction(a, b), Fraction(c, d)))
    elif act == "/":
        write_line(div.div(Fraction(a, b), Fraction(c, d)))

