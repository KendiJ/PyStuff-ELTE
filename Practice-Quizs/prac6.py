import csv
class Person:
    def __init__(self, name, occupation, salary):
        self.name = name
        self.occupation = occupation
        self.salary = salary
    
    def to_dict(self):
        return{'Name': self.name, 'Occupation': self.occupation, 'Salary': self.salary}
    
people_objs = [
    Person("Alice", "Eng", 2000),
    Person("Bob", "Dev", 3000),
    Person("Bill", "Acc", 1500)
]

data_to_write = [p.to_dict() for p in people_objs]
fieldnames = ['Name', 'Occupation', 'Salary']
file_path_oop = 'people_oop.csv'

with open(file_path_oop, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader() #writes the header of Row from fields name
    writer.writerows(data_to_write) # writes lists of dictionaries

print(f"CSV file '{file_path_oop}' created from class objects")