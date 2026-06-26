# Day 08 � OOP: Classes & Inheritance
# Date: July 01, 2026
#
# Learning Goals:
# TODO: Fill in what you learned today, code exercises, and notes.

# Intro to class , constructor and methods

import csv


class Item:
    pay_rate=0.8
    all=[]
    def __init__(self ,name:str,price:float,quantity=0):
        
        # Assert checks a condition and raises an error if it is False.
        assert price >=0 , f"price {price} is negative"
        assert quantity >=0 , f"quantity {quantity} is negative"
        
        
        self.name=name
        self.price=price
        self.quantity=quantity
        
        Item.all.append(self)
    
    def calculate_total_price(self ):
        return self.price*self.quantity
    
    def add_quantity(self , quantity):
        
        self.quantity=self.quantity + quantity
        print(f"{self.name} quantity increased to {self.quantity}")
        return self.quantity
    
    def increase_price(self,price):
        self.price+=price
        print(f"{self.name} price increased to {self.price}")
        return self.price
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f:
            reader=csv.DictReader(f)
            items=list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=int(item.get('price')),
                quantity=int(item.get('quantity')),
            )
    @staticmethod   
    def is_integer(num):
        if isinstance(num,float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False
        
    
    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"
    
        
      
# Item.instantiate_from_csv()

item1=Item("Phone",100,5)
item2=Item("Laptop",1000,3)

# print(item1.calculate_total_price())
# print(item1.add_quantity(10))
# print(item1.increase_price(1000))

print(Item.is_integer(4))
print(Item.is_integer(4.5))


# print(item1.calculate_total_price())
# print(item1.add_quantity(10))
# print(item1.increase_price(1000))


print(Item.all)


