import tkinter as tk
from functools import partial
from tkinter import END

from gpiozero import PWMLED

root = tk.Tk()
root.geometry('400x500')
root.resizable(False, False)

red_out = PWMLED(18)
green_out = PWMLED(23)
blue_out = PWMLED(24)


def check_btn_cl():
    if state.get():
        num_red.config(state="normal")
        num_green.config(state='normal')
        num_blue.config(state='normal')
        scale_widget.config(state='disabled')
        scale_widget2.config(state='disabled')
        scale_widget3.config(state='disabled')
    else:
        num_red.config(state="disabled")
        num_green.config(state='disabled')
        num_blue.config(state='disabled')
        scale_widget.config(state='normal')
        scale_widget2.config(state='normal')
        scale_widget3.config(state='normal')


def change_color(value, color):
    if value:  # если ползунки
        if color == 'red':
            red_out.value = float(value) / 255
            num_red.config(state='normal')
            num_red.delete(0, END)
            num_red.insert(0, value)
            num_red.config(state='disabled')
        elif color == 'green':
            green_out.value = float(value) / 255
            num_green.config(state='normal')
            num_green.delete(0, END)
            num_green.insert(0, value)
            num_green.config(state='disabled')
        elif color == 'blue':
            blue_out.value = float(value) / 255
            num_blue.config(state='normal')
            num_blue.delete(0, END)
            num_blue.insert(0, value)
            num_blue.config(state='disabled')
    else:  # если кнопки
        if color == 'red':
            red_out.value = 1
            green_out.value = 0
            blue_out.value = 0
        elif color == 'green':
            red_out.value = 0
            green_out.value = 1
            blue_out.value = 0
        elif color == 'blue':
            red_out.value = 0
            green_out.value = 0
            blue_out.value = 1
        elif color == 'white':
            red_out.value = 1
            green_out.value = 1
            blue_out.value = 1
        elif color == 'grey':
            red_out.value = 0.5
            green_out.value = 0.5
            blue_out.value = 0.5
        elif color == 'black':
            red_out.value = 0
            green_out.value = 0
            blue_out.value = 0
        elif color == '#ffff00':
            red_out.value = 1
            green_out.value = 1
            blue_out.value = 0
        elif color == '#ff00ff':
            red_out.value = 1
            green_out.value = 0
            blue_out.value = 1
        elif color == '#00ffff':
            red_out.value = 0
            green_out.value = 1
            blue_out.value = 1


def num_btn_cl():
    try:
        red_val = float(num_red.get())
        green_val = float(num_green.get())
        blue_val = float(num_blue.get())
    except ValueError:
        tk.messagebox.showerror('Ошибка', 'Значения неверные')
    else:
        if (red_val <= 255 and red_val >= 0) and (green_val <= 255 and green_val >= 0) and (
                blue_val <= 255 and blue_val >= 0):
            red_out.value = red_val / 255
            green_out.value = green_val / 255
            blue_out.value = blue_val / 255
        else:
            tk.messagebox.showerror('Ошибка', 'Значения неверные')


# ползунки


scale_widget = tk.Scale(root, orient="horizontal", resolution=1, from_=0, to=255, length=150, command=partial(change_color, color='red'))
label_1 = tk.Label(root, text="RED")
label_1.grid(row=1, column=0)
scale_widget.grid(row=1, column=1)
num1 = tk.StringVar()
num_red = tk.Entry(root, width=10, textvariable=num1, state='disabled')
num_red.grid(row=1, column=2)

scale_widget2 = tk.Scale(root, orient="horizontal", resolution=1, from_=0, to=255, length=150, command=partial(change_color, color='green'))
label_2 = tk.Label(root, text="GREEN")
label_2.grid(row=2, column=0)
scale_widget2.grid(row=2, column=1)
num2 = tk.StringVar()
num_green = tk.Entry(root, width=10, textvariable=num2, state='disabled')
num_green.grid(row=2, column=2)

scale_widget3 = tk.Scale(root, orient="horizontal", resolution=1, from_=0, to=255, length=150, command=partial(change_color, color='blue'))
label_3 = tk.Label(root, text="BLUE")
label_3.grid(row=3, column=0)
scale_widget3.grid(row=3, column=1)
num3 = tk.StringVar()
num_blue = tk.Entry(root, width=10, textvariable=num3, state='disabled')
num_blue.grid(row=3, column=2)

state = tk.BooleanVar()
check = tk.Checkbutton(root, variable=state, text='Ввод', font=('Arial Bold', 12), command=check_btn_cl)
check.grid(row=0, column=2)

label_1 = tk.Label(root, text="ПАЛИТРА:")
label_1.grid(row=5, column=0)

button0 = tk.Button(root, font=('Arial Bold', 9), text="Применить", command=num_btn_cl)
button0.grid(row=4, column=2)
# кнопки

button1 = tk.Button(root, bg='red', bd=1,
                    height=3, width=8, activebackground='red', command=partial(change_color, 0, 'red'))
button1.grid(row=6, column=0)

button2 = tk.Button(root, bg='green', bd=1,
                    height=3, width=8, activebackground='green', command=partial(change_color, 0, 'green'))
button2.grid(row=6, column=1)

button3 = tk.Button(root, bg='blue', bd=1,
                    height=3, width=8, activebackground='blue', command=partial(change_color, 0, 'blue'))
button3.grid(row=6, column=2)

label_1 = tk.Label(root, text="          ")
label_1.grid(row=7, columnspan=2)

button4 = tk.Button(root, bg='white', bd=1,
                    height=3, width=8, activebackground='white', command=partial(change_color, 0, 'white'))
button4.grid(row=8, column=0)

button5 = tk.Button(root, bg='grey', bd=1,
                    height=3, width=8, activebackground='grey', command=partial(change_color, 0, 'grey'))
button5.grid(row=8, column=1)

button6 = tk.Button(root, bg='black', bd=1,
                    height=3, width=8, activebackground='black', command=partial(change_color, 0, 'black'))
button6.grid(row=8, column=2)

label_1 = tk.Label(root, text="          ")
label_1.grid(row=9, columnspan=2)

button7 = tk.Button(root, bg='#ffff00', bd=1,
                    height=3, width=8, activebackground='#ffff00', command=partial(change_color, 0, '#ffff00'))
button7.grid(row=10, column=0)

button8 = tk.Button(root, bg='#ff00ff', bd=1,
                    height=3, width=8, activebackground='#ff00ff', command=partial(change_color, 0, '#ff00ff'))
button8.grid(row=10, column=1)

button9 = tk.Button(root, bg='#00ffff', bd=1,
                    height=3, width=8,  activebackground='#00ffff', command=partial(change_color, 0, '#00ffff'))
button9.grid(row=10, column=2)

root.mainloop()
