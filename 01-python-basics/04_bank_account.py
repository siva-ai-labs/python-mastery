
# 04_bank_account.py

balance = 5000.0


def deposit(amount):
    global balance

    if amount <= 0:
        return "Invalid deposit amount"

    balance += amount
    return f"Deposited {amount:.2f} SEK"


def withdraw(amount):
    global balance

    if amount <= 0:
        return "Invalid withdrawal amount"

    if amount > balance:
        return "Insufficient funds"

    balance -= amount
    return f"Withdrawn {amount:.2f} SEK"


print(deposit(2000))
print(withdraw(1500))
print(withdraw(10000))

print(f"Current balance: {balance:.2f} SEK")
