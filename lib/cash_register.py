#!/usr/bin/env python3


class CashRegister:
  
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []
  
  def add_item(self, item, price, qty = 1):
    self.total += (price * qty)
    self.items += ([item] * qty)
    self.price = price
    self.qty = qty

  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else:   
      self.total -= (self.total * (self.discount/100))
      print(f"After the discount, the total comes to ${int(self.total)}.") 
      
  def item_list_without_multiples(self):
    return list(set(self.items))
  
  def items_list_with_multiples(self):
    return self.items
  
  def void_last_transaction(self):
    self.items= self.items[:-self.qty]
    self.total -= (self.price * self.qty)

    