import pytest
from app.calculations import add, subtract, multiply, divide, BankAccount

@pytest.fixture
def zero_bank_account():
    return BankAccount(0)

@pytest.fixture
def bank_account():
    return BankAccount(50)

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

def test_bank_set_initial_amount(bank_account):
    assert bank_account.balance == 50

def test_bank_default_amount(zero_bank_account):
    assert 0 == zero_bank_account.balance
    

def test_withdraw(bank_account):
    bank_account.withdraw(20)
    assert bank_account.balance == 30

def test_deposit(bank_account):
    bank_account.deposit(20)
    assert bank_account.balance == 70

def test_collect_interest(bank_account):
    bank_account.collect_interest()
    assert round(bank_account.balance, 6) == 55


@pytest.mark.parametrize("deposited, withdrew, expected", [(300,200,100),(2,1,1),(50, 10, 40)])

def test_bank_transaction(zero_bank_account, deposited, withdrew, expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrew)
    assert expected == zero_bank_account.balance

def test_insufficient_funds(bank_account):
    with pytest.raises(Exception):
        bank_account.withdraw(100)
    