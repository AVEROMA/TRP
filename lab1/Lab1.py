#Lab_1
import matplotlib.pyplot as plt
import numpy as np
import random
import math

print("введите количество точек: ")
size_point = int(input())
print("введите количество случайных процессов: ")
size_rp = int(input())
print("введите математическое ожидание величины V: ")
mat = int(input())
print("введите среднее квадратичное отклонение величины V: ")
delta = int(input())

step = 0.1 # шаг времени t
fig, ax = plt.subplots()
function_all_value = []

for j in range(size_rp):
    
    psi = 2
    random_value = []
    function_value = []
    korr_value = []

    plt.title("Зависимости: y = V*cos(psi*t-onta)")
    plt.grid(True)  # включение отображение сетки
    onta = random.uniform(0, 2*math.pi)     #генерация случайной велечины
    v = random.normalvariate(mat, delta)    #генерация нормальной СВ
    for i in np.arange(0,size_point,step):
        y = v*math.cos(psi*i-onta)              #вычисление значения функции
        korr = math.cos(psi*i-psi*i)
        function_value.append(y)                #вывод сгенерированного значения
        korr_value.append(korr)
    plt.plot(np.arange(0, size_point, step), function_value) #построение графика по полученным данным
    plt.plot(np.arange(0, size_point, step), korr_value, color = 'r')
    ax.hlines(0,0,size_point, color = 'r')
    ax.hlines(mat+delta,0,size_point, color = 'r')
    ax.hlines(-(mat+delta),0,size_point,color = 'r')
    plt.plot(size_point, 0)
    function_all_value.append(function_value)   #запись полученных данных в массив
print(function_all_value)  
plt.show()