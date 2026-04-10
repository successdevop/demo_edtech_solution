from datetime import datetime


class Account:
    """ Simple account class with balance """
    __cur_time = datetime.now().isoformat()

    def __init__(self, name: str, balance: float):
        self .name = name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        self.transactions.append((Account.__cur_time, amount))

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append((Account.__cur_time, -amount))
        else:
            print("Insufficient balance")

    def show_balance(self):
        print(f"Balance is {self.balance:,}")

    def show_transactions(self):
        for t_time, t_amount in self.transactions:
            if t_amount > 0:
                t_type = "deposited"
            else:
                t_type = "withdrawn"
                t_amount *= -1
            print(f"[{t_time}] {t_type}: #{t_amount}")


if __name__ == "__main__":
    tim = Account("Tim", 0)
    tim.show_balance()

    tim.deposit(1_000)
    tim.show_balance()

    tim.withdraw(500)
    tim.show_balance()

    tim.withdraw(2000)
    tim.show_balance()
    tim.show_transactions()

