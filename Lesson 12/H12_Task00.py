# Задача 0
# Реализовать класс лифта Elevator. Класс должен обладать методом, lift, отвечающий за вызов лифта.
# При сложении/вычитании экземпляров класса должно возвращаться значение производимой математической операции.
# Если производить вычитание у лифта, который еще не совершал поднятий,
# должна быть выведена ошибка неправильной операции.
# Предусмотреть возможность сравнения какой из лифтов совершил большее количество поднятий.
# Также необходимо предусмотреть подсчет общего количества поднятий всех лифтов.
# При строчных операциях необходимо вывести детальную информацию по лифту:
# наименование, количество поднятий и процент от общего количества поднятий всех лифтов.


class Elevator:
    elevators = []

    def __init__(self, name, lifts=0):
        self.lifts = lifts
        self.name = name
        self.__class__.elevators.append(self)

    def lift(self):
        self.lifts += 1

    def __add__(self, other):
        return self.lifts + other.lifts

    def __sub__(self, other):
        if self.lifts == 0:
            return 'Wrong operation!'

        else:
            return self.lifts - other.lifts

    def __lt__(self, other):
        return self.lifts < other.lifts

    def __gt__(self, other):
        return self.lifts > other.lifts

    def __eq__(self, other):
        return self.lifts == other.lifts

    @classmethod
    def lifts_sum(cls):
        return sum(elevator.lifts for elevator in cls.elevators)

    def __str__(self):
        self.percent = self.lifts/self.__class__.lifts_sum() * 100
        return '\nElevator name - {}\nTotal lifts - {}\nPercent - {}\n'.format(self.name, self.lifts, self.percent)


lift1 = Elevator('lift1')
lift1.lift()
lift1.lift()
lift2 = Elevator('lift2')
lift2.lift()
lift2.lift()
lift2.lift()
lift2.lift()
lift3 = Elevator('lift3')
lift3.lift()
print(lift1 - lift2, lift3 - lift2, lift3 + lift2, lift1 < lift3, lift1 > lift2, lift2 == lift3)
print(lift1, lift2, lift3)
