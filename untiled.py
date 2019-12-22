import time
import struct
from typing import List, Any

from processes import Process


def load_data_from_file(que, algorithm_type):
    dane_txt = open("dane.txt", mode="r+")
    if algorithm_type == "FCFS":
        for line in dane_txt:
            if len(que) == 0:
                que.append(Process(line.split()))
                continue
            if len(que) == 1:
                if que[0].arrival < int(line.split()[1]):
                    que.append(Process(line.split()))
                else:
                    que.insert(1, Process(line.split()))
                continue
            for process in que:
                if int(line.split()[1]) <= process.arrival:
                    que.insert(que.index(process), Process(line.split()))
                    break
                if que.index(process) == len(que)-1:
                    que.append(Process(line.split()))
                    break
    return


def load_data_from_consol(que):
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
        que.append(Process(process_parameters))
    return


def check_data(que):
    for i in que:
        if i.is_not_int():
            print("Dane powinny być liczbami całkowytymi")
            return 1
        if i.is_below_0():
            print("Liczby powinny być nieujemne")
            return 1
    return


def print_tab(que):
    print("CzasDoKonca:", end='   ')
    for process in que:
        print(process.current_necessary_time, end='   ')
    print()
    print("Czas przybycia:", end=' ')
    for process in que:
        print(process.arrival, end='   ')
    print()
    print("Priorytet:", end='      ')
    for process in que:
        print(process.priority, end='   ')
    print()
    print("CzasRozpoczęcia:", end='')
    for process in que:
        print(process.start_time, end='   ')
    print()
    print("CzasZakończenia:", end='')
    for process in que:
        print(process.end_time, end='   ')
    print()
    print("CzasOczekiwania:", end='')
    for process in que:
        print(process.wait_time, end='   ')
    print()

    return


def do_algorithm(que, time):
    for process in que:
        while 0 < process.current_necessary_time:
            if process.arrival < time:
                process.do_step(time)
            time = time + 1


time = 0
que_processes = []; load_data_from_file(que_processes, "FCFS")
do_algorithm(que_processes, time)
print_tab(que_processes)