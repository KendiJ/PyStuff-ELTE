from exceptions import ValidationError
class Account:
    def __init__(self, account_id, name, currency):
        self.id = account_id
        self.name = name
        self.currency = currency
        self.type = "general"

        if not name:
            raise ValidationError("Account name cannot be empty")
    
    def to_dict(self):
        return{
            "id": self.id,
            "name": self.name,
            "currency": self.currency,
            "type": self.type
        }
    
    def __str__(self):
        return f"[{self.id}] {self.name} ({self.currency}) - {self.type}"
    

    #Subclass 1
class BankAccount(Account):
    def __init__(self, account_id, name, currency, bank_name = "Generic bank"):
        super().__init__(account_id, name, currency)
        self.type = "bank"
        self.bank_name = bank_name

    def to_dict(self):
        data = super().to_dict()
        data["bank_name"] = self.bank_name
        return data
    
    #Subclass 2
class CashAccount(Account):
    def __init__(self, account_id, name, currency):
        super().__init__(account_id, name, currency)
        self.type = "cash"
     