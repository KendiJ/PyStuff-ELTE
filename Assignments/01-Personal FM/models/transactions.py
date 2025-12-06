class Transactions:
    def __init__(self, t_id, account_id, amount, category, description, date):
        self.id = t_id
        self.account = account_id
        self.amount = float(amount)
        self.category = category
        self.description = description
        self.date = date
        self.type = "generic"

    def to_dict(self):
        return{
            "id": self.id,
            "account": self.account,
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date,
            "type": self.type,
        }
    
    def __str__(self):
        return f"[{self.date}] {self.description}: {self.amount} {self.category}"
    
class IncomeTransaction(Transactions):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type =  "income"

class ExpenseTransaction(Transactions):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = "espense"