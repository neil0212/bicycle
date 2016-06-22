import random
from bicycle import Bicycle,Bike_shops,Customer

#Create bikes

bikes=[
     Bicycle('tiger',12,80)
    ,Bicycle('elephant',10,160)
    ,Bicycle('zebra',12,240)
    ,Bicycle('mouse',10,400)
    ,Bicycle('dragon',8,560)
    ,Bicycle('dinosaur',6,960)
    ]
shop= Bike_shops('ZOO',20,bikes)

customers=[
    Customer('Neil',200)
    ,Customer('Chris',500)
    ,Customer('Andrew',1000)]

for customer in customers:
    bikes=','.join(bike.model for bike in shop.filter(customer.fund))
    print (customer.name, '|' ,bikes)
    
print (shop)

customer_info='{0} bought the {1} at {2}, and they have ${3} left over.'

for customer in customers:
    affordables = shop.filter(customer.fund)
    shop.sell(random.choice(affordables), customer)
    
    print (customer_info.format(
        customer.name, customer.bike.model,
        customer.bike.price, customer.fund
        ))
        
        
print (shop)
