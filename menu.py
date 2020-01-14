import time
import struct
from typing import List, Any

from Scheduler import Scheduler
from processes import Process

scheduler = Scheduler()
scheduler.load_data_from_file()
scheduler.run_round_robin(10)


# try:
#     scheduler = Scheduler()
#     incorrect_choice = True
#     while incorrect_choice:
#         tmp = input("Skąd wczytać dane? Plik='P' Konsola='K'")
#         if tmp == 'K':
#             scheduler.load_data_from_consol()
#             incorrect_choice = False
#         elif tmp == 'P':
#             scheduler.load_data_from_file()
#             incorrect_choice = False
#         else:
#             print("Wpisz 'P' lub 'K'!")
#
#     incorrect_choice = True
#     while incorrect_choice:
#         tmp = input("Jaki Algorytm? FCFS='C'|SJF='F'|RoundRobin='R'|Priorytetowy z postarzaniem='P'")
#         if tmp == 'R':
#             scheduler.run_round_robin(10)
#             incorrect_choice = False
#             continue
#         if tmp == 'P' or tmp == 'F' or tmp == 'C':
#             if tmp == 'P':
#                 #scheduler.sort_priority()
#                 scheduler.run()
#                 incorrect_choice = False
#             if tmp == 'F':
#                 #scheduler.sort_SJF()
#                 scheduler.run()
#                 incorrect_choice = False
#             if tmp == 'C':
#                 #scheduler.sort_FCFS()
#                 scheduler.run()
#                 incorrect_choice = False
#         else:
#             print("Wpisz 'P' lub 'F' lub 'C' lub 'R'!")
# except FileNotFoundError:
#     print()
#     print("Brak pliku. Proszę stworzyć plik 'dane.txt'")
#     print()
#     input("Naciśnij klawisz by zakończyć program")
# except ZeroDivisionError:
#     print()
#     print("Proszę wypełnić plik (oddzielając dane spacją a procesy znakiem nowej lini) w następującej formie:")
#     print("'Czas potrzebny do wykonania' 'Czas przybycia' 'Priorytet'")
#     print()
# input("Naciśnij klawisz by zakończyć program")















