import time
import struct
from typing import List, Any
import copy
import sys
from processes import Process


class Scheduler:

    def __init__(self):
        self.__average_wait = 0.0
        self.__time = 0
        self.__que = []
        self.__end_time = 0
        self.__selected_process = None

    def print_end_time(self):
        print(self.__end_time)

    def load_data_from_file(self):
        try:
            dane_txt = open("dane.txt", mode="r+")
            i = 0
            for line in dane_txt:
                i += 1
                if line.count(' ') == 2:
                    self.__que.append(Process(line.split()))
                else:
                    print()
                    print("Niepoprawnie zapisany wiersz numer {}".format(i))
                    print(
                        "Proszę wypełnić plik (oddzielając dane spacją a procesy znakiem nowej lini) w następującej formie:")
                    print("'Czas potrzebny do wykonania' 'Czas przybycia' 'Priorytet'")
                    print("Proszę również usunąć niepoprawne spacje i znaki nowego wiersza")
                    print()
                    input("Naciśnij klawisz by zakończyć program")
                    sys.exit(-1)
        except ValueError:
            print("Plik powinien być wypełniony liczbami całkowitymi")
            input("Naciśnij klawisz by zakończyć program")
            sys.exit(-1)
        self.check_data()

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
        self.check_data()
        return

    def check_data(self):
        for i in self.__que:
            if i.is_not_int():
                print()
                print("Dane powinny być liczbami całkowytymi")
                print(
                    "Proszę wypełnić plik (oddzielając dane spacją a procesy znakiem nowej lini) w następującej formie:")
                print("'Czas potrzebny do wykonania' 'Czas przybycia' 'Priorytet'")
                print()
                input("Naciśnij klawisz by zakończyć program")
                sys.exit(-1)
            if i.is_below_0():
                print()
                print("Liczby powinny być dodatnie")
                print()
                input("Naciśnij klawisz by zakończyć program")
                sys.exit(-1)
            if len(self.__que) == 0:
                print()
                print("Plik jest pusty")
                print()
                input("Naciśnij klawisz by zakończyć program")
                sys.exit(-1)
        return

    def que_print(self):
        print("Necessary | Arrival | Priority | Start | End | Wait | CurrentNecessary  ")
        for process in self.__que:
            process.display()
        return

    def aging_priorities(self):
        for i in range(len(self.__que)):
            if self.__que[i].get_arrival > self.__time:
                if self.__que[i].get_wait > (1 / 10) * self.__time:
                    self.__que[i].decrease_priority()

    def run_FCFS(self):
        que = copy.copy(self.__que)
        self.__selected_process = que[0]
        do_while = True
        while do_while:
            do_while = False
            for process in que:  # aby w selected było cokolwiek co juz arrival
                if process.get_arrival < self.__time and not process.is_finished:
                    self.__selected_process = process
            for process in que:  # aby w selected by najmniejszy arrival
                if process.get_arrival < self.__time and not process.is_finished:
                    if process.get_arrival < self.__selected_process.get_arrival:
                        self.__selected_process = process
                    if process.get_arrival == self.__selected_process.get_arrival:  # jeśli te same wartości
                        if self.__selected_process.get_current_necessary > process.get_current_necessary:
                            self.__selected_process = process
                        if self.__selected_process.get_current_necessary == process.get_current_necessary:  # jeśli te same wartości
                            if self.__selected_process.get_priority > process.get_priority:
                                self.__selected_process = process
            if self.__selected_process.get_arrival < self.__time and self.__selected_process.get_current_necessary > 0:
                while not self.__selected_process.is_finished:  # wykonujemy
                    self.__selected_process.do_step(self.__time)
                    self.__time += 1
                self.__average_wait += self.__selected_process.get_wait
                self.__end_time = self.__selected_process.get_end
            else:
                self.__time += 1
            for process in que:  # sprawdzamy czy już wyjśc z while
                if not process.is_finished:
                    do_while = True
        self.__average_wait /= len(self.__que)
        print()
        print("Average wait time: {}ms".format(round(self.__average_wait, 2)))
        print("Finished time: {}ms".format(self.__end_time))
        self.que_print()
        return

    def run_SJF(self):
        que = copy.copy(self.__que)
        self.__selected_process = que[0]
        do_while = True
        while do_while:
            do_while = False
            for process in que:  # aby w selected było cokolwiek co juz arrival i do wykonania
                if process.get_arrival < self.__time and not process.is_finished:
                    self.__selected_process = process
            for process in que:  # aby w selected by najmniejszy current
                if process.get_arrival < self.__time and not process.is_finished:
                    if process.get_current_necessary < self.__selected_process.get_current_necessary:
                        self.__selected_process = process
                    if process.get_current_necessary == self.__selected_process.get_current_necessary:
                        if process.get_arrival < self.__selected_process.get_arrival:
                            self.__selected_process = process
                        if self.__selected_process.get_arrival == process.get_arrival:  # jeśli te same wartości
                            if self.__selected_process.get_priority > process.get_priority:
                                self.__selected_process = process

            if self.__selected_process.get_arrival < self.__time and self.__selected_process.get_current_necessary > 0:
                while not self.__selected_process.is_finished:  # wykonujemy
                    self.__selected_process.do_step(self.__time)
                    self.__time += 1
                self.__average_wait += self.__selected_process.get_wait
                self.__end_time = self.__selected_process.get_end
            else:
                self.__time += 1
            for process in que:  # sprawdzamy czy już wyjśc z while
                if not process.is_finished:
                    do_while = True
        self.__average_wait /= len(self.__que)
        print()
        print("Average wait time: {}ms".format(round(self.__average_wait, 2)))
        print("Finished time: {}ms".format(self.__end_time))
        self.que_print()
        return

    def run_priority(self):
        que = copy.copy(self.__que)
        self.__selected_process = self.__que[0]
        do_while = True
        while do_while:
            do_while = False
            for process in que:  # aby w selected było cokolwiek co juz arrival i do wykonania
                if process.get_arrival < self.__time and not process.is_finished:
                    self.__selected_process = process
            for process in que:  # aby w selected by najmniejszy priorytet
                if process.get_arrival < self.__time and not process.is_finished:
                    if process.get_priority < self.__selected_process.get_priority:
                        self.__selected_process = process
                    if process.get_priority == self.__selected_process.get_priority:
                        if process.get_current_necessary < self.__selected_process.get_current_necessary:
                            self.__selected_process = process
                        if process.get_current_necessary == self.__selected_process.get_current_necessary:
                            if process.get_arrival < self.__selected_process.get_arrival:
                                self.__selected_process = process
            if self.__selected_process.get_arrival < self.__time and self.__selected_process.get_current_necessary > 0:
                while not self.__selected_process.is_finished:  # wykonujemy
                    self.__selected_process.do_step(self.__time)
                    self.__time += 1
                self.__average_wait += self.__selected_process.get_wait
                self.__end_time = self.__selected_process.get_end
            else:
                self.__time += 1
            for process in self.__que:  # sprawdzamy czy już wyjśc z while
                if not process.is_finished:
                    do_while = True
            self.aging_priorities()
        self.__average_wait /= len(self.__que)
        print()
        print("Average wait time: {}ms".format(round(self.__average_wait, 2)))
        print("Finished time: {}ms".format(self.__end_time))
        self.que_print()
        return

    def run(self):  # F
        que = copy.copy(self.__que)
        average_wait: float = 0.0
        while len(que) > 0:
            number_of_selected_process = 0
            for i in range(0, len(que)):
                if 0 < que[i].get_current_necessary:
                    if que[i].get_arrival < que[number_of_selected_process].get_arrival:
                        number_of_selected_process = i
            if que[number_of_selected_process].get_arrival < self.__time:
                while 0 < self.__que[number_of_selected_process].get_current_necessary:
                    que[number_of_selected_process].do_step(self.__time)
                    self.__time += 1
                que.pop([number_of_selected_process])
                # del que[number_of_selected_process]
                average_wait += self.__que[number_of_selected_process].get_wait
                self.__end_time = self.__que[number_of_selected_process].get_end
            else:
                self.__time += 1

        print()
        print("czas po wykonaniu: {}".format(self.__time))
        average_wait /= len(self.__que)
        print("Average wait time: {}ms".format(round(average_wait, 2)))
        print("Finished time: {}ms".format(self.__end_time))
        self.que_print()
        return


    def run_round_robin(self, quantum):
        que = copy.copy(self.__que)
        count_length = 0
        for process in que:#sort zeby zacząc od tego co pierwszy arrival
            count_length += process.get_current_necessary
        quantum = count_length/(5*len(que))
        for process in que:
            index_min_process = que.index(process)
            for index_process in range(que.index(process),len(que)):
                if que[index_process].get_arrival < process.get_arrival:
                    index_min_process = index_process
            tmp = process
            que[que.index(process)] = que[index_min_process]
            que[index_min_process] = tmp
        while len(que) > 0:#poczatek algorytmu
            for process in que:
                if (
                        process.get_arrival - self.__time) > 2 * quantum:  # ulepszenie aby nie czekał na pierwszy proces o póżnym przybyciu
                    self.__time += 1
                    continue
                i = 0
                while i < quantum:
                    if process.get_arrival < self.__time and process.get_current_necessary > 0:
                        process.do_step(self.__time)
                        i += 1
                    if process.get_current_necessary == 0:
                        i += 1
                    self.__time += 1
                if process.get_current_necessary == 0:
                    self.__average_wait += process.get_wait
                    self.__end_time = process.get_end
                    del que[que.index(process)]
        self.__average_wait /= len(self.__que)
        print()
        print("Average time: {}ms".format(round(self.__average_wait, 2)))
        print("Finished time: {}ms".format(self.__end_time))
        print("Quantum: {}ms".format(round(quantum, 2)))
        self.que_print()
        return
