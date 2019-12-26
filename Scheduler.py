import time
import struct
from typing import List, Any
import copy
from processes import Process


class Scheduler:
    def __init__(self):
        self.__time = 0
        self.__que = []
        self.average_wait: float = 0.0

    def load_data_from_file(self):
        dane_txt = open("dane.txt", mode="r+")
        for line in dane_txt:
            self.__que.append(Process(line.split()))

        return

    def load_data_from_consol(self):
        print("Proszę wpisać informację o procesach")
        next_process = bool(1)
        while next_process:
            process_parameters = []
            string_parameters = ["Czas trwania: ", "Czas przybycia: ", "Priorytet: "]
            for step in range(0, 3):
                process_parameters.append(input(string_parameters[step]))
            while True:
                print("Następny proces?(Wpisz T lub N)")
                tmp = input()
                if tmp == "T":
                    next_process = bool(1)
                    break
                if tmp == "N":
                    next_process = bool(0)
                    break
            self.__que.append(Process(process_parameters))
        return

    def check_data(self):
        for i in self.__que:
            if i.is_not_int():
                print("Dane powinny być liczbami całkowytymi")
                return 1
            if i.is_below_0():
                print("Liczby powinny być nieujemne")
                return 1
        return

    def que_print(self):
        print("Necessary | Arrival | Priority | Start | End | Wait | CurrentNecessary  ")
        for process in self.__que:
            process.display()
        return

    def sort_FCFS(self):
        for i in range(len(self.__que)):
            j = len(self.__que) - 1
            while i < j:
                if self.__que[j - 1].get_arrival > self.__que[j].get_arrival:
                    tmp = self.__que[j]
                    self.__que[j] = self.__que[j - 1]
                    self.__que[j - 1] = tmp
                j -= 1
        return

    def sort_SJF(self):
        for i in range(len(self.__que)):
            j = len(self.__que) - 1
            while i < j:
                if self.__que[j - 1].get_necessary > self.__que[j].get_necessary:
                    tmp = self.__que[j]
                    self.__que[j] = self.__que[j - 1]
                    self.__que[j - 1] = tmp
                j -= 1
        return

    def sort_priority(self):
        for i in range(len(self.__que)):
            j = len(self.__que) - 1
            while i < j:
                if self.__que[j - 1].get_priority > self.__que[j].get_priority:
                    tmp = self.__que[j]
                    self.__que[j] = self.__que[j - 1]
                    self.__que[j - 1] = tmp
                j -= 1
        return

    def aging_priorities(self):
        for i in range(len(self.__que)):
            if self.__que[i].get_arrival > self.__time:
                if self.__que[i].get_wait > (9/10)*self.__time:
                    self.__que[i].decrease_priority()

    def run(self):
        average_wait: float = 0.0

        algorithm_completed = False
        while not algorithm_completed:
            algorithm_completed = True
            touch_process = False
            for process in self.__que: #SCFS and SJF
                if not process.is_finished:
                    algorithm_completed = False
                if process.get_arrival < self.__time:
                    while 0 < process.get_current_necessary:
                        process.do_step(self.__time)
                        self.__time += 1
                        touch_process = True
                    average_wait += process.get_wait
                    self.aging_priorities()
            if not touch_process:
                self.__time += 1



        average_wait /= len(self.__que)
        print("Average wait time: {}ms".format(average_wait))
        print("Finished time: {}ms".format(self.__time - 1))
        self.que_print()
        return

    def run_round_robin(self, quantum):
        que = copy.copy(self.__que)
        while len(que) > 0:
            for process in que:
                if (process.get_arrival - self.__time) > 2*quantum: # ulepszenie aby nie czekał na pierwszy proces o póżnym przybyciu
                    self.__time += 1
                    continue
                i = 0
                while i < quantum:
                    if process.get_arrival < self.__time and process.get_current_necessary > 0:
                        process.do_step(self.__time)
                    i += 1
                    self.__time += 1
                if process.get_current_necessary == 0:
                    self.average_wait += process.get_wait
                    del que[que.index(process)]

        print("Average time: {}ms".format(self.average_wait))
        print("Finished time: {}ms".format(self.__time - 1))
        self.que_print()
        return
