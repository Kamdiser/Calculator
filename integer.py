import div, mult, diff, sum
from my_ui import write_line


def integer(act, num1, num2):
    if act == "+":
        write_line(sum.sum(num1, num2))
    elif act == "-":
        write_line(diff.diff(num1, num2))
    elif act == "*":
        write_line(mult.mult(num1, num2))
    elif act == "/":
        if num2 == 0:
            write_line("∞")
        elif num2 == 0 and num1 == 0:
            write_line("nan")
        else:
            write_line(div.div(num1, num2))