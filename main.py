import tkinter as tk
import tkinter.messagebox
import decimal
from decimal import Decimal


def hdiv(dividend, divisor, accuracy=0):
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
    res += str(integer) + '.'

    # 计算余数
    remainder = dividend % divisor

    # 计算小数部分
    for i in range(accuracy):
        dividend = remainder * 10
        res += str(round(dividend // divisor))
        remainder = dividend % divisor
    
    txt.delete('1.0', tk.END)
    txt.insert('1.0', res)


def hmul(a, b):
    txt.delete('1.0', tk.END)
    txt.insert('1.0', a*b)


def hsum(a, b):
    txt.delete('1.0', tk.END)
    txt.insert('1.0', a+b)


def hsub(a, b):
    txt.delete('1.0', tk.END)
    txt.insert('1.0', a-b)


decimal.getcontext().prec = decimal.MAX_PREC

win = tk.Tk()
win.title("IntCalc")
win.geometry('650x600')

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

num3_label = tk.Label(win, text='除法精度',justify=tk.LEFT, height=2, width=5, font=('Microsoft YaHei', 13))
num3_label.grid(row=7, column=0)
num3_entry = tk.Entry(win, justify=tk.LEFT, width=15, font=('Microsoft YaHei', 20))
num3_entry.grid(row=7, column=1)
num3_entry.insert(0, 10)

sum_button = tk.Button(win, text='+', justify=tk.CENTER, width=10, font=('Microsoft YaHei', 20) ,command=lambda:hsum(Decimal(num1_entry.get()), Decimal(num2_entry.get())))  # 文本框创建
sum_button.grid(row=4, column=0)

sub_button = tk.Button(win, text='-', justify=tk.CENTER, width=10, font=('Microsoft YaHei', 20), command=lambda:hsub(Decimal(num1_entry.get()), Decimal(num2_entry.get())))  # 文本框创建
sub_button.grid(row=4, column=1)

mul_button = tk.Button(win, text='x', justify=tk.LEFT, width=10, font=('Microsoft YaHei', 20), command=lambda:hmul(Decimal(num1_entry.get()), Decimal(num2_entry.get()))) # 文本框创建
mul_button.grid(row=5, column=0)

div_button = tk.Button(win, text='/', justify=tk.LEFT, width=10, font=('Microsoft YaHei', 20), command=lambda:hdiv(Decimal(num1_entry.get()), Decimal(num2_entry.get()), int(num3_entry.get())))  # 文本框创建
div_button.grid(row=5, column=1)

win.mainloop()
