class Process:
    def __init__(self, tab):
        self.__start_time = None
        self.__end_time = None
        self.__current_necessary_time = int(tab[0])
        self.__necessary_time = int(tab[0])# potrzebny czas do wykonania
        self.__arrival = int(tab[1])  # moment przybycia
        self.__priority = int(tab[2])  # priorytet
        self.__duration_time = None
        self.__start = True
        self.__wait_time = 0
        self.is_finished = False
        return

    @property
    def get_arrival(self):
        return int(self.__arrival)

    @property
    def get_wait(self):
        return self.__wait_time

    @property
    def get_necessary(self):
        return self.__necessary_time

    @property
    def get_current_necessary(self):
        return self.__current_necessary_time

    @property
    def get_priority(self):
        return self.__priority

    @property
    def decrease_priority(self):
        self.__priority -= 1
        return

    @property
    def get_end(self):
        return self.__end_time

    def display(self):
        print(self.__necessary_time, end='              ')
        print(self.__arrival, end='         ')
        print(self.__priority, end='         ')
        print(self.__start_time, end='      ')
        print(self.__end_time, end='     ')
        print(self.__wait_time, end='           ')
        print(self.__current_necessary_time)
        return

    def is_not_int(self):
        if isinstance(self.__current_necessary_time, int) and isinstance(self.__arrival, int) and isinstance(self.__priority, int):
            return False
        else:
            return True

    def is_below_0(self):
        if self.__current_necessary_time <= 0 or self.__arrival <= 0 or self.__priority <= 0:
            return True
        else:
            return False

    def do_step(self, time):
        if self.__start:
            self.__start_time = time - 1
            self.__start = False
        self.__current_necessary_time = self.__current_necessary_time - 1
        if self.__current_necessary_time == 0:
            self.__end_time = time
            self.__wait_time = self.__end_time - self.__arrival - self.__necessary_time
            self.is_finished = True
        return
