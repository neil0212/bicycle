class Bicycle:
    def __init__(self,model,weight,cost_produce):
        self.model=model
        self.weight=weight
        self.cost_produce=cost_produce
    
    def __repr__(self):
        bike_info='The {0} | Cost: ${1} Weight: {2}kg'
        return bike_info.format(self.model,self.cost_produce,self.weight)
        
        
class Bike_shops:
    def __init__(self,name,margin,bikes):
        self.name=name
        self.margin=margin
        self.profit=0
        self.inventory={}
        
        for bike in bikes:
            
            bike.markup=int((bike.cost_produce/100)*self.margin)
            bike.price=bike.markup+bike.cost_produce
            self.inventory[bike.model]=bike
            
    def __repr__(self):
        bike_shops_info='\n{0} (${1}profit)\n{2}\n'
        bikes='\n'.join(str(bike) for bike in self.inventory.values())
        return bike_shops_info.format(self.name,self.profit,bikes)
   
    def filter(self,budget):
        bikes=self.inventory.values()
        return [bike for bike in bikes if budget-bike.price>0]
        
    def sell(self,bike,customer):
        
        customer.bike=bike
        customer.fund-=bike.price
        self.profit += bike.markup
        del self.inventory[bike.model]
        
        
class Customer:
    def __init__(self,name,fund):
        self.name=name
        self.fund=fund
        self.bike=None











    