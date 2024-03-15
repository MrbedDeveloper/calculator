
import tkinter as tk
import math
import matplotlib.pyplot as plt

def calculate_square_area(side_length):
    return side_length**2

def calculate_circle_area(radius):
    return math.pi * (radius**2)

def on_click(event):
    text = event.widget.cget("text")
    
    if text.isdigit() or text == ".":
        entry.insert(tk.END, text)
    elif text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Ошибка")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "Удалить":
        entry_str = entry.get()
        entry_str = entry_str[:-1]
        entry.delete(0, tk.END)
        entry.insert(tk.END, entry_str)
    elif text == "Площадь квадрата":
        side_length = float(entry.get())
        area = calculate_square_area(side_length)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(area))
    elif text == "Площадь круга":
        radius = float(entry.get())
        area = calculate_circle_area(radius)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(area))
    elif text == "Диаграмма":
        data = [float(entry.get()), 10, 20]  # Пример данных для построения диаграммы
        plt.bar(['Значение 1', 'Значение 2', 'Значение 3'], data)
        plt.xlabel('Ось X')
        plt.ylabel('Ось Y')
        plt.title('Пример построения диаграммы')
        plt.show()

# Создание графического интерфейса
root = tk.Tk()
root.title("Калькулятор и дополнительные функции")

entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+',
    'Площадь квадрата', 'Площадь круга', 'Диаграмма', 'Удалить'
]

row_num = 1
col_num = 0
for button in buttons:
    btn = tk.Button(root, text=button, padx=15, pady=10)
    btn.grid(row=row_num, column=col_num, padx=5, pady=5)
    btn.bind("<Button-1>", on_click)
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1

root.mainloop()