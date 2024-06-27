class Category:
    
    def __init__(self, category_name: str) -> None:
        self.ledger = []
        self.category_name = category_name
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.category_name})"
            
    def deposit(self, amount: float, description: str = '') -> None:
        self.ledger.append({'amount': amount, 'description': description})
        
    def withdraw(self, amount: float, description: str = '') -> bool:
        if self.check_funds(amount):
            self.deposit(-amount, description)
            return True
        return False
        
    def get_balance(self) -> float:
        return sum(map(lambda tx: tx['amount'], self.ledger))
    
    def transfer(self, amount: float, destination_category: Category) -> bool:
        if self.check_funds(amount):
            destination_category.deposit(amount, description=f"Transfer from {self.category_name}")
            self.withdraw(amount, description=f"Transfer to {destination_category.category_name}")
            return True
        return False
        
    def check_funds(self, amount: float) -> bool:
        if not (amount > self.get_balance()):
            return True
        return False