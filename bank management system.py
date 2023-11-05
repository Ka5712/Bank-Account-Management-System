balance = 10000


class Bank:
    def _init_(self, name, branch):
        self.name = name
        self.branch = branch

    def bankdetails(self):
        return f"the name of bank is {self.name} and branch is in  {self.branch} "


# B1 = Bank("sbi", "sowcarpet")
# print(B1.bankdetails())


class Account:
    def _init_(self, accountnumber, accountname):
        self.accountnumber = accountnumber
        self.accountname = accountname

    def accountdetails(self):
        return f"the acc name is {self.accountname} and acc number is   {self.accountnumber} "


# a1 = Account("21010587", "cyril")
# print(a1.accountdetails())


class Transcation:
    def _init_(self, withdrawl, deposit, balancecheck):
        self.withdrawl = withdrawl
        self.deposit = deposit
        self.balancecheck = balancecheck



    def withdraw(self):
        global balance
        amount = int(input("Enter the amount: "))
        # check for sufficient balance
        if amount > balance:
            return"Insufficient Balance"

        print("Amount withdrawn")
        bal = balance - amount
        return"Available Balance: " + str(bal)

    def deposit(self):
        global bal
        dep = int(input("Enter the amount to deposit: "))
        bal = balance + dep
        print("deposited amount")
        return"Available Balance: " + str(bal)
        print("deposited amount")



    def balancecheck(self):
        return "Updated Balance: " + str(bal)



t1 = Transcation()
print(t1.withdraw())
print(t1.deposit())
print(t1.balancecheck())