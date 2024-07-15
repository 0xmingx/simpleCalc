import tkinter as tk
import tkinter.messagebox
import decimal
from decimal import Decimal
from math import sqrt


def hdiv(output_txt, dividend, divisor, accuracy=0):
    '''
    参数:
        dividend: 被除数
        divisor: 除数
        accuracy: 除法精度
    返回: 计算结果(字符串)
    '''
    # 定义存储结果的字符串
    res = ''

    # 定义保存正负数的变量
    isNegative = False

    # 确定正负号
    if dividend < 0 and divisor >= 0:
        dividend = abs(dividend)
        isNegative = True
    elif divisor < 0 and dividend >= 0:
        divisor = abs(divisor)
        isNegative = True

    # 在结果添加正负号
    if isNegative:
        res += '-'

    # 计算整数部分
    integer = round(dividend // divisor)

    # 将结果添加入结果
    if accuracy == 0:
        res += str(integer)
    else:
        res += str(integer) + '.'

    # 计算余数
    remainder = dividend % divisor

    # 计算小数部分
    for i in range(accuracy):
        dividend = remainder * 10
        res += str(round(dividend // divisor))
        remainder = dividend % divisor
    
    output_txt.delete('1.0', tk.END)
    output_txt.insert('1.0', res)
    return res


def hmul(output_txt, a, b):
    output_txt.delete('1.0', tk.END)
    output_txt.insert('1.0', a*b)


def hsum(output_txt, a, b):
    output_txt.delete('1.0', tk.END)
    output_txt.insert('1.0', a+b)


def hsub(output_txt, a, b):
    output_txt.delete('1.0', tk.END)
    output_txt.insert('1.0', a-b)


def d2b(output_txt, a):
    output_txt.delete('1.0', tk.END)
    output_txt.insert('1.0', int(bin(int(a))[2:]))


def b2d(output_txt, a):
    output_txt.delete('1.0', tk.END)
    output_txt.insert('1.0', int(str(a), 2))


def hpow(output_txt, a, b):
    output_txt.delete('1.0', tk.END)
    if b < 1:
        output_txt.insert('1.0', float(a)**float(b))
    else:
        output_txt.insert('1.0', a**b)


# like (2**342)*(3**38)*(5**48)*(7**8)*(11**4)*(13**4)*(17**4)*(19**4)*(37**2)*(7440427**2)
def calc_input(output_txt, s):
    output_txt.delete('1.0', tk.END)
    output_txt.insert('1.0', eval(s))


def is_prime(output_txt, a):
    out_s = f'{a} 是质数'

    if a == 0:
        out_s = '0 不是质数'
    elif a == 1:
        out_s = '1 不是质数'
    elif a == 2:
        out_s = '2 是质数'
    elif a > 2:
        if a % 2 == 0:
            b = hdiv(output_txt, a, 2)
            out_s = f'{a} 除以 2 等于 {b}, 不是质数'
        for x in range(3, int(sqrt(a) + 1), 2):
            if a % x == 0:
                b = hdiv(output_txt, a, x)
                out_s = f'{a} 除以 {x} 等于 {b}, 不是质数'
                break

    output_txt.delete('1.0', tk.END)
    output_txt.insert('1.0', out_s)


def pre_calc(output_txt, func_type):

    if num1_entry.get()=='' or num1_entry.get()=='':
        if func_type != 'calc_input':
            return tkinter.messagebox.showinfo('提示', '输入不能为空')
    
    if func_type == 'hsum':
        hsum(output_txt, Decimal(num1_entry.get()), Decimal(num2_entry.get()))
    elif func_type == 'hsub':
        hsub(output_txt, Decimal(num1_entry.get()), Decimal(num2_entry.get()))
    elif func_type == 'hmul':
        hmul(output_txt, Decimal(num1_entry.get()), Decimal(num2_entry.get()))
    elif func_type == 'hdiv':
        hdiv(output_txt, Decimal(num1_entry.get()), Decimal(num2_entry.get()), int(num3_entry.get()))
    elif func_type == 'd2b':
        d2b(output_txt, Decimal(num1_entry.get()))
    elif func_type == 'b2d':
        b2d(output_txt, Decimal(num1_entry.get()))
    elif func_type == 'hpow':
        hpow(output_txt, Decimal(num1_entry.get()), Decimal(num2_entry.get()))
    elif func_type == 'calc_input':
        equation = txt.get('1.0', tk.END)
        try:
            calc_input(output_txt, equation)
        except SyntaxError:
            return tkinter.messagebox.showinfo('提示', '输入错误\n%s'%equation)
    elif func_type == 'is_prime':
        is_prime(output_txt, Decimal(num1_entry.get()))


def reset_all():
    txt.delete('1.0', tk.END)
    num1_entry.delete(0, tk.END)
    num2_entry.delete(0, tk.END)
    num3_entry.delete(0, tk.END)
    num3_entry.insert(0, 10)


decimal.getcontext().prec = decimal.MAX_PREC

win = tk.Tk()
win.title("IntCalc")
win.geometry('800x950')

bg=tk.Label(win, text='IntCalc', justify=tk.CENTER, height=2, width=50 ,font=('Microsoft YaHei', 20))
bg.grid(row=0, columnspan=6)

txt = tk.Text(win, height=12, width=60, font=('Microsoft YaHei', 15), bg='lightcyan')
txt.grid(row=1, column=0, columnspan=6)

num1_label = tk.Label(win, text='a', justify=tk.CENTER, height=2, width=5, font=('Microsoft YaHei', 30))
num1_label.grid(row=2, column=0)
num1_entry = tk.Entry(win, justify=tk.LEFT, width=30, font=('Microsoft YaHei', 20))
num1_entry.grid(row=2, column=1, columnspan=5)

num2_label = tk.Label(win, text='b',justify=tk.CENTER, height=2, width=5, font=('Microsoft YaHei', 30))
num2_label.grid(row=3, column=0)
num2_entry = tk.Entry(win, justify=tk.LEFT, width=30, font=('Microsoft YaHei', 20))
num2_entry.grid(row=3, column=1, columnspan=5)

num3_label = tk.Label(win, text='除法精度',justify=tk.LEFT, height=2, width=10, font=('Microsoft YaHei', 20))
num3_label.grid(row=4, column=0)
num3_entry = tk.Entry(win, justify=tk.LEFT, width=30, font=('Microsoft YaHei', 20))
num3_entry.grid(row=4, column=1, columnspan=5)
num3_entry.insert(0, 10)

sum_button = tk.Button(
    win, text='+', justify=tk.CENTER, width=10, font=('Microsoft YaHei', 20),
    command=lambda:pre_calc(txt, 'hsum')
    )
sum_button.grid(row=5, column=0)

sub_button = tk.Button(
    win, text='-', justify=tk.CENTER, width=10, font=('Microsoft YaHei', 20),
    command=lambda:pre_calc(txt, 'hsub')
    )
sub_button.grid(row=5, column=1)

b_button = tk.Button(
    win, text='二进制', justify=tk.CENTER, width=10, font=('Microsoft YaHei', 20),
    command=lambda:pre_calc(txt, 'd2b')
    )
b_button.grid(row=5, column=2)

d_button = tk.Button(
    win, text='十进制', justify=tk.CENTER, width=10, font=('Microsoft YaHei', 20),
    command=lambda:pre_calc(txt, 'b2d')
    )
d_button.grid(row=5, column=3)

mul_button = tk.Button(
    win, text='x', justify=tk.LEFT, width=10, font=('Microsoft YaHei', 20),
    command=lambda:pre_calc(txt, 'hmul')
    )
mul_button.grid(row=6, column=0)

div_button = tk.Button(
    win, text='/', justify=tk.LEFT, width=10, font=('Microsoft YaHei', 20),
    command=lambda:pre_calc(txt, 'hdiv')
    )
div_button.grid(row=6, column=1)

n_button = tk.Button(
    win, text='n次方', justify=tk.CENTER, width=10, font=('Microsoft YaHei', 20),
    command=lambda:pre_calc(txt, 'hpow')
    )
n_button.grid(row=6, column=2)

calc_button = tk.Button(
    win, text='算式', justify=tk.LEFT, width=10, font=('Microsoft YaHei', 20), bg='lightcyan',
    command=lambda:pre_calc(txt, 'calc_input')
    )
calc_button.grid(row=6, column=3)

is_prime_button = tk.Button(
    win, text='质数判断', justify=tk.LEFT, width=10, font=('Microsoft YaHei', 20), bg='lightcyan',
    command=lambda:pre_calc(txt, 'is_prime')
)
is_prime_button.grid(row=7, column=1)

clr_button = tk.Button(
    win, text='清屏', justify=tk.LEFT, width=10, font=('Microsoft YaHei', 20),
    command=lambda:reset_all()
    )
clr_button.grid(row=7, column=3)

win.mainloop()
