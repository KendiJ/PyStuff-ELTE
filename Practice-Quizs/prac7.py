

class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class UnderGrads(Student):
    def __init__(self, id, name, age):
        super().__init__(id, name)
        self.age = age

class StdtManage():
    def __init__(self, list):
        self.list = list

    def add_std(self, student):
        self.list.append(student)
        return         