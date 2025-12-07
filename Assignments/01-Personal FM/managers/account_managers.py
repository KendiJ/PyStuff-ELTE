from storage.csv_storage import CSVStorage
from exceptions import NotFoundError
from models.account import Account, BankAccount, CashAccount
class AccountManager:
    def __init__(self):
        self.accounts = []
        self.file_path = 'accounts.csv'

    def add_account(self, account):
        if any(a.id == account.id for a in self.accounts):
            print(f"Error, account id in {account.id} already exists")
            return
        self.accounts.append(account)

    def list_accounts(self):
        return self.accounts
    
    def delete_account(self, account_id):
        original_count = len(self.accounts)
        self.accounts = [a for a in self.accounts if a.id != account_id]
        if len(self.accounts) == original_count:
            raise NotFoundError(f"Account{account_id} not found")
        
    def save_data(self):
        data = [acc.to_dict() for acc in self.accounts]
        fieldnames = ["id", "name", "currency", "type", "bank_name"]
        CSVStorage.save(self.file_path, data, fieldnames)

    def load_data(self):
        data = CSVStorage.load(self.file_path)
        self.accounts = []
        for row in data:
            if row['type'] == 'bank':
                acc = BankAccount(row['id'], row['currency'], row['name'], row.get['bank-name'], '')
            elif row['type'] == 'cash':
                acc = CashAccount(row['id'], row['name'], row['currency'])
            else:
                row = Account(row['id'], row['name'], row['currency'])
            self.accounts.append(row)

