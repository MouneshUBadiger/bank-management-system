
class Account:
    def __init__(self, id, holder_name):
        self.id = id
        self.holder_name = holder_name
        self._balance = 0  # Encapsulation

    def check_balance(self):
        print(f'Balance: {self._balance}')

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f'Deposit successful. Updated Balance: {self._balance}')
        else:
            print('Deposit amount must be greater than zero.')

    def withdraw(self, amount):
        if amount <= 0:
            print('Withdrawal amount must be greater than zero.')
        elif self._balance >= amount:
            self._balance -= amount
            print(f'Withdraw successful. Updated Balance: {self._balance}')
        else:
            print('Insufficient balance.')


class SavingsAccount(Account):  # Inheritance
    def calculate_interest(self):
        INTEREST_RATE = 0.04  # 4%
        interest = self._balance * INTEREST_RATE
        print(f'Interest: {interest:.2f}')


class CurrentAccount(Account):
    def withdraw(self, amount):  # Polymorphism
        OVERDRAFT_LIMIT = 1000

        if amount <= 0:
            print('Withdrawal amount must be greater than zero.')
        elif self._balance + OVERDRAFT_LIMIT >= amount:
            self._balance -= amount
            print(f'Withdraw successful. Updated Balance: {self._balance}')
        else:
            print('Withdrawal exceeds the overdraft limit.')


class Bank:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.__accounts = {}

    def create_account(self, id, holder_name, account_type):
        if id in self.__accounts:
            print('Account ID already exists.')
            return None

        if account_type.lower() == 'savings':
            new_account = SavingsAccount(id, holder_name)
        elif account_type.lower() == 'current':
            new_account = CurrentAccount(id, holder_name)
        else:
            print('Invalid account type.')
            return None

        self.__accounts[id] = new_account
        print('Account creation successful.')
        return new_account

    def get_account(self, id):
        if id not in self.__accounts:
            print('Account not found!')
            return None

        account = self.__accounts[id]
        print(f'\nID: {account.id}')
        print(f'Holder Name: {account.holder_name}')
        return account


# Create bank object
mbk = Bank('Mounesh Bank of Karnataka', 'Bagalakot')


# Menu-driven program
while True:
    print('\n========== MOUNESH BANK OF KARNATAKA ==========')
    print('1. Create Account')
    print('2. Deposit Money')
    print('3. Withdraw Money')
    print('4. Check Balance')
    print('5. Calculate Interest')
    print('6. Exit')
    print('===============================================')

    choice = input('Enter your choice (1-6): ')

    if choice == '1':
        account_id = input('Enter account ID: ')
        holder_name = input('Enter account holder name: ')
        account_type = input('Enter account type (Savings/Current): ')

        mbk.create_account(account_id, holder_name, account_type)

    elif choice == '2':
        account_id = input('Enter account ID: ')
        account = mbk.get_account(account_id)

        if account is not None:
            try:
                amount = float(input('Enter deposit amount: '))
                account.deposit(amount)
            except ValueError:
                print('Please enter a valid amount.')

    elif choice == '3':
        account_id = input('Enter account ID: ')
        account = mbk.get_account(account_id)

        if account is not None:
            try:
                amount = float(input('Enter withdrawal amount: '))
                account.withdraw(amount)
            except ValueError:
                print('Please enter a valid amount.')

    elif choice == '4':
        account_id = input('Enter account ID: ')
        account = mbk.get_account(account_id)

        if account is not None:
            account.check_balance()

    elif choice == '5':
        account_id = input('Enter account ID: ')
        account = mbk.get_account(account_id)

        if account is not None:
            if isinstance(account, SavingsAccount):
                account.calculate_interest()
            else:
                print('Interest calculation is available only for Savings accounts.')

    elif choice == '6':
        print('Thank you for using Mounesh Bank of Karnataka!')
        break

    else:
        print('Invalid choice! Please enter a number from 1 to 6.')
