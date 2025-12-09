import cmd
import shlex
from managers.account_managers import AccountManager
from managers.transaction_managers import TransactionManager
from managers.budget_managers import BudgetManager
from models.account import BankAccount, CashAccount
from exceptions import FinanceError


class FinancialShell(cmd.Cmdmd):
    intro = "Welcome to the Personal Finance Manager"
    prompt = '(finance)'

    def __init__(self):
        super().__init()
        self.acc_manager = AccountManager()
        self.trans_manager = TransactionManager()
        self.budget_manager = BudgetManager()

    def _parse_args(self, arg):
        """Parses arguments, handling quotes."""
        try:
            return shlex.split(arg)
        except ValueError:
            print("Error: Unbalances values in argument ")
            return []
        
    
    # account commands
    def do_add_account_bank(self, arg):
        """Add a bank account. Usage: add_account_bank <id> <name> <currency> <bank_name>"""
        args = self._parse_args(arg)
        if len(args) != 4:
            print("Error: Expected 4 arguments(ID, name and Currency, BankName)")
            return
        
        try:
            acc = BankAccount(args[0], args[1], args[2], args[3])
            self.acc_manager.add_account(acc)
            print(f"Account {args[1]} created")
        except FinanceError as e:
            print(f"Error: {e}")

    def do_add_account_cash(self, arg):
        """Add a cash account. Usage: add_account_cash <id> <name> <currency>"""
        args = self._parse_args(arg)
        if len(args) != 3:
            print("error: Expected 3 arguments(ID, Name and Currency)")
            return
        try:
            acc = CashAccount(args[0], args[1], args[2])
            self.acc_manager.add_account(acc)
            print(f"Cash wallet {args[1]} has been created")
        except FinanceError as e:
            print(f"Error {e}")
        



