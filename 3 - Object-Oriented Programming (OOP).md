# Object-Oriented Programming (OOP)

## 🎯 Why Use OOP?

- ✅ Organizes code into logical units (classes)
- ✅ Encourages reusability (inheritance)
- ✅ Makes code easier to maintain and extend
- ✅ Useful for modeling real-world entities

## 🧩 Key Concepts

### 1. **Class and Object**

#### ➤ Class
A **class** is a blueprint for creating objects.

```python
class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def display(self):
        print(f"Product: {self.name} (${self.price:.2f}) - Stock: {self.stock}")
```

#### ➤ Object
An object is an instance of a class.

```python
p1 = Product(101, "Wireless Mouse", 25.99, 100)
p1.display()  # Product: Wireless Mouse ($25.99) - Stock: 100
```

### 2. **Encapsulation**
Protect product stock by preventing direct modification.

```python
class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.__stock = stock  # private attribute

    def get_stock(self):
        return self.__stock

    def update_stock(self, amount):
        if amount >= 0:
            self.__stock = amount
        else:
            print("❌ Stock cannot be negative.")
```

### 3. **Abstraction**
Hide the complexity of order total calculation inside an Order class.

```python
class Order:
    def __init__(self):
        self.items = []  # list of (Product, quantity) tuples

    def add_item(self, product, quantity):
        if product.get_stock() >= quantity:
            self.items.append((product, quantity))
        else:
            print(f"❌ Not enough stock for {product.name}")

    def calculate_total(self):
        total = 0
        for product, quantity in self.items:
            total += product.price * quantity
        return total
```

### 4. **Inheritance**
Create a specialized DigitalProduct subclass.

```python
class DigitalProduct(Product):
    def __init__(self, product_id, name, price, file_size_mb):
        super().__init__(product_id, name, price, stock=9999)  # infinite stock
        self.file_size_mb = file_size_mb

    def display(self):
        super().display()
        print(f"File Size: {self.file_size_mb} MB")
```

```python
ebook = DigitalProduct(201, "Python eBook", 9.99, 5)
ebook.display()
```

### 5. **Polymorphism**
Both Product and DigitalProduct have a display() method, but behave differently.

```python
def show_product_info(product):
    product.display()

show_product_info(p1)    # Shows physical product info
show_product_info(ebook) # Shows digital product info with file size
```

## **Special Methods (Dunder Methods)**
Make products printable and comparable.

```python
class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.__stock = stock

    def __str__(self):
        return f"{self.name} (${self.price:.2f})"

    def __eq__(self, other):
        return self.product_id == other.product_id
```

```python
print(p1)  # Wireless Mouse ($25.99)

p2 = Product(101, "Wireless Mouse", 25.99, 100)
print(p1 == p2)  # True
```

## Class vs Instance vs Static Methods
Example with utility method to convert price currency.

```python
class Product:
    exchange_rate = 1.1  # USD to EUR, for example

    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    @classmethod
    def set_exchange_rate(cls, rate):
        cls.exchange_rate = rate

    @staticmethod
    def convert_to_eur(usd_price):
        return usd_price * Product.exchange_rate

    def display_price_in_eur(self):
        eur = self.convert_to_eur(self.price)
        print(f"Price in EUR: €{eur:.2f}")
```

## Best Practices
- Use clear, meaningful class names
- Keep attributes private when needed
- Document classes and methods
- Use inheritance wisely
- Favor composition over inheritance
- Implement __str__ and __repr__
- Write unit tests for classes

