class Slot:
    __indexcounter=0
    def __init__(self):
        self.__index = Slot.__indexcounter
        Slot.__indexcounter += 1