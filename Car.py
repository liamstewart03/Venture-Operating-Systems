class Car:
    def __init__(self, subclass, model, base_price):
        self.subclass = subclass
        self.model = model
        self.price = base_price

    def __str__(self):
        return f"""
        Subclass: {self.subclass}
        Model: {self.model}
        Price: {self.price}
        """


