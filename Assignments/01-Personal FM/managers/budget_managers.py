from storage.csv_storage import CSVStorage
from models.budget import Budget
class BudgetManager:
    def __init__(self):
        self.budgets = []
        self.file_path = "budget.csv"

    def add_budget(self, budget):
        self.budgets.append(budget)

    def list_budget(self):
        return self.budgets
    
    def save_data(self):
        data = [b.to_dict() for b in self.budgets]
        fieldsnames = ["id"], ["category"], ["limit_amount"], ["month"]
        CSVStorage.save(self.file_path, data, fieldsnames)

    def load_data(self):
        data = CSVStorage.load(self.file_path)
        self.budgets = []
        for row in data:
            b = Budget(row['id'], row['category'], row['limit_amount'], row['month'])
            self.budgets.append(b)