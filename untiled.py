import time
import struct
from processes import processes

# czas trwania,moment przybycia,priorytet,
dane_txt = open("dane.txt", mode="r+")

F = []
for line in dane_txt:
    F.append(processes(line))
print(F[3].priority)
