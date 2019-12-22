class Process:
    def __init__(self, tab):
        self.start_time = None
        self.end_time = None
        self.current_necessary_time = int(tab[0])
        self.necessary_time = int(tab[0])# potrzebny czas do wykonania
        self.arrival = int(tab[1])  # moment przybycia
        self.priority = int(tab[2])  # priorytet
        self.duration_time = None
        self.start = True
        self.wait_time = None
        return

    def display(self):
        print(self.current_necessary_time)
        print(self.arrival)
        print(self.priority)

    def is_not_int(self):
        if isinstance(self.current_necessary_time, int) and isinstance(self.arrival, int) and isinstance(self.priority, int):
            return False
        else:
            return True

    def is_below_0(self):
        if self.current_necessary_time < 0 or self.arrival < 0 or self.priority < 0:
            return True
        else:
            return False

    def get_arrival(self):
        return self.arrival

    def do_step(self, time):
        if self.start:
            self.start_time = time-1
            self.start = False
        self.current_necessary_time = self.current_necessary_time - 1
        if self.current_necessary_time == 0:
            self.end_time = time
            self.wait_time = self.end_time - self.arrival - self.necessary_time
        return