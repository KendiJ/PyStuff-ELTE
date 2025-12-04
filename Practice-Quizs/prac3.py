# Create a class called Student.
# The __init__ method should take name and grades (a list of numbers).
# Add a method called get_average() that returns the average of the student's grades.
# Add a method called has_passed() that returns True if the average is 50 or higher, and False otherwise.
# Test: Create a student named "John" with grades [40, 60, 50] and print if he passed.

class Student:
    def __init__ (self, name, grades):
        self.name = name
        self.grades = grades

    def get_average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def has_passed(self):
        if self.get_average() >= 50:
            return True
        else:
            return False

john = Student("John", [40, 66, 50])

print(f"John's average: {john.get_average()}")
print(f"Did he pass: {john.has_passed()}")