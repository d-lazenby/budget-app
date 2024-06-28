from src.app import Category

def test_init():
    cat = Category(category_name='category_name')
    assert not cat.ledger
    assert cat.category_name == 'category_name'
    
def test_deposit():
    cat = Category(category_name='category_name')
    cat.deposit(amount=100)
    assert cat.ledger[0] == {'amount': 100, 'description': ''}
    
    cat.deposit(amount=200, description='200 deposited')
    assert cat.ledger[1] == {'amount': 200, 'description': '200 deposited'}
    
def test_get_balance():
    cat = Category(category_name='category_name')
    assert cat.get_balance() == 0
    
    cat.deposit(amount=100)
    cat.deposit(amount=200)
    assert cat.get_balance() == 300
    
def test_check_funds():
    cat = Category(category_name='category_name')
    # False if balance < amount, True otherwise
    assert not cat.check_funds(amount=100)
    cat.deposit(amount=150)
    assert cat.check_funds(amount=100)

def test_withdraw():
    cat = Category(category_name='category_name')
    cat.deposit(1000)
    cat.withdraw(100)
    # Object should be created in ledger and description empty
    assert cat.ledger[1] and (not cat.ledger[1]['description']) 
    # Return True if withdrawal takes place, False otherwise
    assert cat.withdraw(100) and (not cat.withdraw(10000))

def test_transfer():
    cat1 = Category(category_name='Category1')
    cat2 = Category(category_name='Category2')
    
    cat1.deposit(1000)
    # Transfer from cat1 to cat2 should return True if cat1.balance > amount, False otherwise
    assert cat1.transfer(amount=100, destination_category=cat2) and (not cat1.transfer(amount=10000, destination_category=cat2))
    assert cat2.get_balance() == 100 and cat1.get_balance() == 900