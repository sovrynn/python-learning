class Person:
    def __init__(self, name):
        print("Person class constructor")
        self.name = name

    def get_name(self):
        return self.name

    def rename(self, new_name):
        self.name = new_name


class Employee(Person):
    def __init__(self, name, salary):
        print("Employee class constructor")
        self.salary = salary
        Person.__init__(self, name)

    def get_salary(self):
        return self.salary


class Athlete(Person):
    def __init__(self, name, sport):
        print("Athlete class constructor")
        self.sport = sport
        Person.__init__(self, name)

    def get_sport(self):
        return self.sport


p = Athlete("Bob", "soccer")
print(p.get_name())
print(p.get_sport())
