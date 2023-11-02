from database.Customer import Customer

class CustomerModel(Customer):
    def __init__(self) -> None:
        super().__init__()
        
        self.id = None
        self.name = None
       
    # Query builder ???
    def query(self):
        pass