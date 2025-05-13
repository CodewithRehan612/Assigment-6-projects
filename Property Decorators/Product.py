class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price

# Example usage:
if __name__ == "__main__":
    p = Product(100)
    print(p.price)  # Get price
    p.price = 150   # Set price
    print(p.price)
    del p.price     # Delete price
    try:
        print(p.price)
    except AttributeError as e:
        print(f"Error: {e}") 