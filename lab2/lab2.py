import numpy as np 
import math
class Workshop:
    def __init__(self):
        self.count_machine_one = 0
        self.count_machine_two = 0
        self.count_machine_three = 0
        self.time_machine_one = 0
        self.time_machine_two = 0
        self.time_machine_three = 0
        self.max_machine_one = 0
        self.max_machine_two = 0
        self.max_machine_three = 0

    def __del__(self):
        del self.count_machine_one
        del self.count_machine_two
        del self.count_machine_three
        del self.time_machine_one
        del self.time_machine_two
        del self.time_machine_three
        del self.max_machine_one
        del self.max_machine_two
        del self.max_machine_three

    def details_time_arraived(self):    #время прибытия
       return math.floor(np.random.normal(1,1))

    def machine_time(self, index_machine):  #время работы 
        machine = {
            1: np.random.normal(1,0),
            2: np.random.normal(1,0),
            3: np.random.normal(1,0)
        }
        return math.floor(machine[index_machine])

    def transfer_time(self, index_transfer):    #время передачи от станка к станку
        transfer = {
            1: np.random.normal(0,0),
            2: np.random.normal(0,0),
            3: 0
        }
        return math.floor(transfer[index_transfer])

    def count_machine(self, index_machine, var):    #подсчет количества деталей у каждого станка
        if index_machine == 1:
            self.count_machine_one += var
        elif index_machine == 2:
            self.count_machine_two += var
        elif index_machine == 3:
            self.count_machine_three += var
    

    def count_time(self, index_machine, var):   #подсчет времени каждого станка
        if index_machine == 1:
            self.time_machine_one += var
        elif index_machine == 2:
            self.time_machine_two += var
        elif index_machine == 3:
            self.time_machine_three += var

    def count_max(self, index_machine, var):    #подсчет макс кол-ва деталей в очереди
        if index_machine == 1:
            self.max_machine_one = var
        elif index_machine == 2:
            self.max_machine_two = var
        elif index_machine == 3:
            self.max_machine_three = var
    def getCount_machine(self):     #получить кол-во деталей
        return  self.count_machine_one, self.count_machine_two, self.count_machine_three

    def getTime_machine(self):      #получить время
        return self.time_machine_one, self.time_machine_two, self.time_machine_three

    def getMax_machine(self, index_machine):    #получить макс деталей в очереди
        if index_machine == 1:
            return self.max_machine_one
        elif index_machine == 2:
            return self.max_machine_two
        elif index_machine == 3:
            return self.max_machine_three



class Details:
    def __init__(self):
        self.time_que = 0
        self.time_arraived = 0
    
    def setTime_arraived(self, time_arraived):  #установить время прибытия
        self.time_arraived += time_arraived

    def getTime_arraived(self):         #получить время прибытия
        return self.time_arraived

    def getTime_queue(self):        #получить время в очереди
        return self.time_que

    def setTime_queue(self, time):      #установить время в очереди
        self.time_que += time
    
def work(time_modeling):    #моделирование
    i = 1
    index = 1
    details_queue = []
    workshop = Workshop()
    all_detail = 0
    transfer_time = 0
    size_queue_details = []
    queue_time = []
    time_arraived = workshop.details_time_arraived()

    while i <= time_modeling:   #запуск моделирования до интервала времени
        if i % time_arraived == 0:
            add_details(details_queue,workshop,time_arraived, i)
            all_detail += 1

        if len(details_queue) > 0: #If lenght of details is not null then we do work_machine()
            time = work_machine(details_queue,-1,queue_time,workshop,index)
            i += time

            if time_arraived > i%time_arraived: #If time_arraived more then i%time_arraived remainder then we add details
                add_details(details_queue,workshop,time_arraived, i)
                size_queue_details.append(len(details_queue))
                all_detail += 1

            if len(details_queue) >= 2:     #если деталей больше 2, то обрабатываем новую деталь
                details_queue[-2].setTime_queue(time)
                time = work_machine(details_queue,-2,queue_time,workshop,index)
            else:
                time = 0

            transfer_time = workshop.transfer_time(index)   #время передачи от станка к станку
            i += abs(transfer_time - time)

            if index < 3:
                index+=1 
            else: 
                index = 1
         
        i += 1
    count_one, count_two, count_three = workshop.getCount_machine()
    time_one, time_two, time_three = workshop.getTime_machine()
    max_one, max_two, max_three = workshop.getMax_machine(1), workshop.getMax_machine(2), workshop.getMax_machine(3)
    print("avg details in queue: " + str(sum(size_queue_details)/len(size_queue_details)))
    print("avg time in queue: " + str(sum(queue_time)/len(queue_time)))
    print("all detail: " + str(all_detail))
    print("serving detail: " + str(count_three))
    print("coeff machine one: " + str(time_one / time_modeling) + "\n"
        "coeff machine two: " + str(time_two / time_modeling) + "\n"
        "coeff machine three: " + str(time_three / time_modeling) + "\n")

    print("time machine one: " + str(time_one) + "\n"
        "time machine two: " + str(time_two) + "\n"
        "time machine three: " + str(time_three) + "\n")

    print("max queue machine one: " + str(max_one) + "\n"
        "max queue machine two: " + str(max_two) + "\n"
        "max queue machine three: " + str(max_three) + "\n")
    
def add_details(details_queue, workshop ,time_arraived, i): #добавление деталей в очередь
        details_queue.insert(0, Details())
        time_arraived = workshop.details_time_arraived()
        details_queue[0].setTime_arraived(time_arraived)

def work_machine(details_queue,index_details,queue_time,workshop, index):   #работа станков

    machine_time = workshop.machine_time(index)
    workshop.count_machine(index, 1)
    if len(details_queue) > workshop.getMax_machine(index): #если очередь больше чем значения в классе, то перезапись значения
        workshop.count_max(index,len(details_queue))
    if index == 3:
        queue_time.append(details_queue[index_details].getTime_queue())
        details_queue.pop(index_details)
    workshop.count_time(index, machine_time)

    return machine_time

work(int(input("Введите интервал времени для моделирования: ")))