from datetime import datetime


class Account:

    @staticmethod
    def current_time():
        utc_time = datetime.now().isoformat()
        return utc_time

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
        self._transaction_list = []
        print(f"Account created for {self._name}")

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.show_balance()
            self._transaction_list.append((Account.current_time(), amount))

    def withdrawal(self, amount):
        if amount > 0:
            if self._balance > amount:
                self._balance -= amount
                self._transaction_list.append((Account.current_time(), -amount))
            else:
                print("The amount must be greater than zero and not more than your balance")
        self.show_balance()

    def show_transaction(self):
        for time, amount in self._transaction_list:
            if amount > 0:
                trans_type = "deposited"
            else:
                trans_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {}".format(amount, trans_type, time))

    def show_balance(self):
        print(f"Balance is {self._balance}")


if __name__ == "__main__":
    success = Account("Success", 500)
    success.show_balance()

    success.deposit(1000)

    success.withdrawal(800)
    success.show_transaction()

    print("=================")
    steph = Account("Steph", 800)
    steph.show_balance()
    steph.deposit(100)
    steph.withdrawal(200)
    steph.show_transaction()

    steph._balance = 200
    steph.show_transaction()
    steph.show_balance()