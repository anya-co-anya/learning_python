'''
Implement 2 classes, the first one is the Boss and the second one is the Worker.
Worker has a property 'boss', and its value must be an instance of Boss.
You can reassign this value, but you should check whether the new value is Boss.
Each Boss has a list of his own workers. You should implement a method that allows you to add workers to a Boss.
You're not allowed to add instances of Boss class to workers list directly via access to attribute, use getters and setters instead!
'''


class Boss:
    id_list = []

    def __init__(self, id_: int, name: str, company: str):
        if Boss.validate_id(id_, Boss.id_list):
            self.id = id_
            Boss.id_list.append(id_)
        else:
            raise ValueError('id exists')
        self.name = name
        self.company = company
        self.workers = []


    @staticmethod
    def validate_id(value, all_ids):
        '''check if new id doesn`t already exist'''
        if value in all_ids:
            return False
        else:
            return True

    def add_worker(self, worker):
        self.workers.append({'id': worker.id, 'name': worker.name, 'company': worker.company})

    def remove_worker(self, worker):
        for i in range(len(self.workers)):
            if self.workers[i].get('id') == worker.id:
                self.workers.pop(i)
                break




class Worker:
    id_list = []

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        if Boss.validate_id(id_, Worker.id_list):
            self.id = id_
            Worker.id_list.append(id_)
        else:
            raise ValueError('id exists')
        self.name = name
        self.company = company
        if isinstance(boss, Boss):
            self.__boss = boss
            boss.add_worker(self)

    @property
    def boss(self):
        return self.__boss

    @boss.setter
    def boss(self, new_boss):
        if isinstance(new_boss, Boss):
            self.__boss.remove_worker(self)
            self.__boss = new_boss
            self.__boss.add_worker(self)


if __name__ == '__main__':
    maks = Boss(3434, 'Maks', 'Google')
    masha = Boss(3429, 'Masha', 'PT')
    olga = Worker(3452, 'Olga', 'Samsung', maks)

    print(maks.workers)
    olga.boss = masha

    print(f'Maks: {maks.workers}')
    print(f'Masha: {masha.workers}')



