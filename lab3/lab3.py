import numpy as np
import tkinter as tk
from tkinter import *

class ED:
    def __init__(self):
        self.probability_trans = np.array([[0, 0.5, 0.5], [0.8, 0.2, 0], [0.25, 0.25, 0.5]])
        self.weather_dict={0:"Ясно", 1:"Снег", 2:"Дождь"}


    def count_weather(self):
        text.delete("1.0","end")
        state = 0 
        start_matrix = np.array([0,0,0])

        day = int(day_count.get())
        start_matrix[0] = int(clear_count.get())
        start_matrix[1] = int(snow_count.get())
        start_matrix[2] = int(rain_count.get())

        for i in range(day):
            start_matrix = start_matrix.dot(self.probability_trans)
            text.insert(END, ("День:{}".format(i+1) + " (Яcно - {}, Снег - {}, Дождь - {})\n".format(start_matrix[0],start_matrix[1],start_matrix[2])))
            root.update()

        for i in range(day):
            prev_probability = 0
            rand_number = np.random.rand()
            for j in range(3):
                probability = self.probability_trans[state,j]
                if rand_number <= probability + prev_probability and probability != 0:
                    text.insert(END, ("День-{} Матрица[{},{}]".format(i+1, state, j) + " Вероятность: {}".format(self.probability_trans[state,j]) + " Погода: {}\n".format(self.weather_dict[state])))
                    state = j
                    break
                prev_probability = self.probability_trans[state, j]
                root.update()


ed = ED()
root = tk.Tk()
root['bg'] = "black"
root.title("Лабораторная 3")
root.geometry("500x400")


days_label = tk.Label(master = root, bg = "black")
days_label ["text"] = "Количество дней"
days_label.pack()
spinval_1 = StringVar()
day_count = tk.Spinbox(master = root, from_=0, to=100, textvariable=spinval_1)
day_count.pack()


clear_prob = tk.Label(master = root, bg = "black")
clear_prob ["text"] = "начальная вероятность состояния - Ясно"
clear_prob.pack()
spinval_2 = StringVar()
clear_count = tk.Spinbox(master = root, from_=0, to=100, textvariable=spinval_2)
clear_count.pack()


snow_prob = tk.Label(master = root, bg = "black")
snow_prob ["text"] = "начальная вероятность состояния - Снег"
snow_prob.pack()
spinval_3 = StringVar()
snow_count = tk.Spinbox(master = root, from_=0, to=100, textvariable=spinval_3)
snow_count.pack()


rain_prob = tk.Label(master = root, bg = "black")
rain_prob ["text"] = "начальная вероятность состояния - Дождь"
rain_prob.pack()
spinval_4 = StringVar()
rain_count = tk.Spinbox(master = root, from_=0, to=100, textvariable=spinval_4)
rain_count.pack()


btn_encrypt = tk.Button(master = root,
                        text = "Рассчитать", 
                         width=25,height=1,
                        command = ed.count_weather,
                        bg = "black"
                        )
btn_encrypt.pack()


text = tk.Text(master = root, width=60, height=10)
text.pack()
            

root.mainloop()