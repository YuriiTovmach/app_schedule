class Worker:

    def __init__(self, name, shifts, slots):
        self.name = name
        self.shifts = shifts
        self.slots = slots

    def copy(self):
        return Worker(self.name, self.shifts, self.slots[:])

    def assign(self, slot):
        assert slot in self.slots
        self.shifts -= 1
        self.slots.remove(slot)

