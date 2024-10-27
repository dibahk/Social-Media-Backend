import pytest
from app.calculations import add, subtract, multiply, divide, BankAccount

@pytest.mark.parametrize("num1, num2, expected", [(3,2,5),(7,1,8),(12, 4, 16)])
def test_add(num1, num2, expected):
    print("testing add function")
    # sum=
    assert expected == add(num1, num2)
def test_subtract():
    assert subtract(5,3) == 2

def test_multiply():
    assert multiply(2,3)==6

def test_divide():
    assert divide(2,1)==2

def test_bank_set_initial_amount():
    bank_account = BankAccount(50)
    assert bank_account.balance == 50

def test_bank_default_amount():
    bank_account = BankAccount()
    

def test_withdraw():
    bank_account = BankAccount(50)
    bank_account.withdraw(20)
    assert bank_account.balance == 30

def test_deposit():
    bank_account = BankAccount(50)
    bank_account.deposit(20)
    assert bank_account.balance == 70