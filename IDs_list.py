import random

class IdNumbers:
    last_20_ids = []  # not more that 20 IDs,
    all_id_numbers = []
    last_id = 0


    def __init__(self):
        self.__id_number = IdNumbers.last_id
        IdNumbers.last_id += 1
        IdNumbers.all_id_numbers.append(self.__id_number)

    @property
    def id_number(self):
        return self.__id_number

    @classmethod
    def last_viewed(cls, current_id) -> list:
        if len(IdNumbers.last_20_ids) >= 20:
            IdNumbers.last_20_ids.pop()

        if current_id.__id_number in IdNumbers.last_20_ids:
            a = IdNumbers.last_20_ids.pop(IdNumbers.last_20_ids.index(current_id.__id_number))
            IdNumbers.last_20_ids.insert(0, a)
        else:
            IdNumbers.last_20_ids.insert(0, current_id.__id_number)
        return IdNumbers.last_20_ids



if __name__ == '__main__':
    id_0 = IdNumbers()
    id_1 = IdNumbers()
    id_2 = IdNumbers()

    print(IdNumbers.last_viewed(id_1))
    print(IdNumbers.last_viewed(id_0))
    print(IdNumbers.last_viewed(id_2))
    print(IdNumbers.last_viewed(id_1))
    print('-------')

    for i in range(1, 25):
        print(IdNumbers.last_viewed(IdNumbers()))
        print(f'size: {len(IdNumbers.last_20_ids)}')
        print('-------')


