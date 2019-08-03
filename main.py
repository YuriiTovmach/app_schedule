from worker import Worker
from schedule import Schedule


Udon = Worker('Udon', 1, [3,4])
Ramen = Worker('Ramen', 1, [2])
Soba = Worker('Soba' , 2, [1,3])

Noodle_workers = [Soba, Ramen, Udon]
Slots = [1, 2, 3, 4]

print(Schedule(Noodle_workers, Slots))


