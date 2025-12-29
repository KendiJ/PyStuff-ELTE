class PersonalFinance :
    def __init__(self, id, name):
        self.id = id
        self.name = name

obj1 = PersonalFinance(10, "A")
obj2 = PersonalFinance(12, "B")

personal_finance_dict = {
        obj1.id: obj1.name,
        obj2.id: obj2.name,
    }
print(personal_finance_dict)