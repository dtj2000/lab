import pytest
import account


def test_deposit():
    assert account.Account("Test", 0).deposit(10) is True
    assert account.Account("Test", 0).deposit(-10) is False
    assert account.Account("Test", 0).deposit(0) is False
    assert account.Account("Test", 0).deposit(10.5) is True

def test_withdraw():
    assert account.Account("Test", 10).withdraw(10) is True
    assert account.Account("Test", 10).withdraw(10.5) is False
    assert account.Account("Test", 10).withdraw(0) is False
    assert account.Account("Test", 10).withdraw(-10) is False
