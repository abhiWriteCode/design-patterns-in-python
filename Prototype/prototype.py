import copy


class Employees:

    def __init__(self, employees_list=[]):
        self.employees_list = employees_list

    def get_employees_list(self):
        return self.employees_list

    def load_data_from_DB(self):
        self.employees_list.append('John')
        self.employees_list.append('Jonny')
        self.employees_list.append('Janardhan')
        self.employees_list.append('Amar')
        self.employees_list.append('Akhbar')
        self.employees_list.append('Anthony')

    def clone(self):
        # return copy.copy(self)
        return Employees(self.employees_list)


if __name__ == '__main__':
    employees = Employees()
    employees.load_data_from_DB()
    for employee in employees.get_employees_list():
        print(employee, end=' ')
    print()

    employees1 = employees.clone()
    employees1.get_employees_list().append("Raju")
    for employee in employees1.get_employees_list():
        print(employee, end=' ')
    print()

    employees2 = employees.clone()
    employees2.get_employees_list().pop(0)
    for employee in employees2.get_employees_list():
        print(employee, end=' ')
    print()

    print(list(map(id, [employees, employees1, employees2])))
