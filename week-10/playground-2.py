class Cat:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def rename(self, new_name):
        self.name = new_name


c = Cat("Mylo")
print(c.get_name())
c.rename("Marty")
print(c.get_name())
