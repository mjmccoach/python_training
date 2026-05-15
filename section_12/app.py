from modules.bank_account import * # ADDED

account = BankAccount("John", 500, "business")

print(account.holder_name)

account.holder_name = 'Ada'  # ADDED
print(account.holder_name)

account.pay_in(50)
print(account.balance)

account.pay_monthly_fee(account.type)
print(account.balance)

account.type = "personal"
account.pay_monthly_fee(account.type)
print(account.balance)

