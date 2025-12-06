class Budget:
    def __init__(self, b_id, category, limit_amount, month):
        self.id = b_id
        self.category = category
        self.limit_amount = float(limit_amount)
        self.month = month

    def to_dict(self):
        return{
            "id" : self.id,
            "category": self.category,
            "limit_amount": self.limit_amount,
            "month": self.month
        }
    
    def __str__(self):
        return f"[{self.month}] {self.category}: Limit {self.limit_amount}"
