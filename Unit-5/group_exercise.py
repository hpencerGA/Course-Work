#create a class OrderManager
#Implement methods to do the following:
#- read a file called orders.json, store
#in a class variable called orderlist
#- get the total number of orders
#- get the person with the most orders
#- get the person with the largest total order value
#- ge the most expensive item ordered
#- get the most frequently ordered item

import json

#- get the total number of orders

class ordermanager:
    def __init__(self):
        self.orders= []

    #- read a file called orders.json, store
    #in a class variable called orderlist
    def read_file(self, file):
        with open(file, 'r') as input_file:
            self.orders = json.load(input_file)

    #- get the total number of orders
    def num_orders(self):
        order_count = 0
        #for each customer count the order
        for customers in self.orders:
            order_count += len(customer['orders'])
        return order_count


    #- get the person with the most orders
    def most_orders(self):
        current_highest = 0
        name_of_highest = ''
        
        #heck each customer fo highes tnumber

        for customer in self.orders:
            if len(customer['orders']) > current_highest:
                #update current highest and name of highest
                current_highest = len(customer['orders'])
                name_of_highest = customer['cusotmer name']

    #- get the person with the largest total order value
    def highest_value(self):
        current_highest = 0.0
        name_of_highest = ''

    #for each customer, check if they have the highest total value
    for customer in self.orders:
        orders_total = 0.0
        #add up prices
        for item in customer['orders']:
            price = float(item['price'][1:])
            orders_total += price
        if orders_total > current_highest:
            #update current_highest and name_of_highest
            current_highest = orders_total
            name_of_highest = customer['customer_name']

    return name_of_highest

    # get the most expensive item ordered
    def most_expensive(self):
        current_highest_most = 0.0
        name_of_most = ' '
        #for each customer cheack each of their orders
        for customer in self.orders:
            for item in customer ['orders']:


    #- get the most frequently ordered item
    def frequently_ordered(self):
        num_orders = {}
        most_ordered = self.orders[0]['orders'][0]['item']
        #for each customer count each of their orders
        for customer in self.orders:
            for item in customer["orders"]:
                name_of_item = item['item']
                num_orders [name_of_item] = num_orders.get(name_of_item, 0) + 1
        #look for order with highest number of orders
        for item in num_orders:
            if num_orders(item) > num_orders[most_ordered]:
                most_ordered = item
    
    return most_ordered

manager = ordermanager() 
manager.read_file(orders.json)
print(manager.numorders())
print(manager.highest())
print(manager.most_orders())
print(manager.highest_value())
print(manager.most_expensive())
print(manager.frequently_ordered())

