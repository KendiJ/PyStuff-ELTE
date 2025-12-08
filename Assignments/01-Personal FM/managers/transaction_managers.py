from exceptions import ValidationError
from storage.csv_storage import CSVStorage
from models.transactions import IncomeTransaction, ExpenseTransaction
class TransactionManager:
    def __init__(self, account_manager):
        self.transactions = []
        self.file_path = "transactions.csv"
        self.account_manager = account_manager

    def add_transactions(self, transaction):
        account_ids = [acc.id for acc in self.account_manager.list_accounts()]

        if transaction.account_id not in account_ids:
            raise ValidationError(f"Account ID {transaction.account_id}, does not exists. Create one first")
        self.transactions.append(transaction)

    def list_transactions(self):
        return self.transactions
    
    def save_data(self):
        data = [t.to_dict() for t in self.transactions]
        fieldnames = ["id"], ["account_id"], ["amount"], ["category"], ["description"], ["date"], ["type"]
        CSVStorage.save(self.file_path, data, fieldnames)
    
    def load_data(self):
        data = CSVStorage.load(self.file_path)
        self.transactions = []
        for row in data:
            if row['type'] == 'income':
                t = IncomeTransaction(row['id'], row['account_id'], row['amount'], row['category'], row['description'], row['date'])
            else:
                t = ExpenseTransaction(row['id'], row['account_id'], row['amount'], row['category'], row['description'], row['date'])
            self.transactions.append(t)
