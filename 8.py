
class Car:
    def __init__(self, brand, model , battery):
        self.brand = brand
        self.__model = model
        self.battery = battery
    
    def full_name(self):
        return f"{self.brand} {self.__model} {self.battery}"
    
    
    
    
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model, battery)
        self.battery= battery
    
    

my_tesla= ElectricCar("Tesla","Model S","85kWh")
print(isinstance(my_tesla,Car))
print(isinstance(my_tesla,ElectricCar))



