class Processes:
    def __init__(self, tab):
        self.duration = int(tab[0])  # czas trwania
        self.arrival = int(tab[1])  # moment przybycia
        self.priority = int(tab[2])  # priorytet

    def display(self):
        print(self.duration)
        print(self.arrival)
        print(self.priority)

    def is_not_int(self):
        if isinstance(self.duration, int) and isinstance(self.arrival, int) and isinstance(self.priority, int):
            return False
        else:
            return True

    def is_below_0(self):
        if self.duration < 0 or self.arrival < 0 or self.priority < 0:
            return True
        else:
            return False
