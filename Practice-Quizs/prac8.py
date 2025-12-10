class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class UnderGrads(Student):
     def __init__(self, id, name, age):
         super().__init__(id, name)
         self.age = age

class StudentManager:
    def __init__ (self, list):
        self.list = list

    def add_stdnt(self, student):
        self.list.append(student)
        return
    
        