import time
import struct
from typing import List, Any

from processes import Processes


def load_data_from_file(tab):
    dane_txt = open("dane.txt", mode="r+")

    for line in dane_txt:
        try:
            tab.append(Processes(line.split()))
        except:
            print('Dane w pliku są niepoprawne')
    return


def load_data_from_consol(tab):
    print("Proszę wpisać informację o procesach")
    next_process = bool(1)
    while next_process:
        process_parameters = []
        string_parameters = ["Czas trwania: ","Czas przybycia: ", "Priorytet: "]
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
        tab.append(Processes(process_parameters))
    return


def check_data(tab):
    for i in tab:
        if i.is_not_int():
            print("Dane powinny być liczbami całkowytymi")
            return 1
        if i.is_below_0():
            print("Liczby powinny być nieujemne")
            return 1
    return


tab_processes = []
load_data_from_file(tab_processes)
check_data(tab_processes)
