from database.Product import Product

class ProductModel(Product):
    def __init__(self) -> None:
        super().__init__()
        self.p = dict()
        