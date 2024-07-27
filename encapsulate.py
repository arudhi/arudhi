
class Car:
    def __init__(self, brand, model , battery):
        self.__brand = brand
        self.model = model
        self.battery = battery
    
    def get_brand(self):
        return self.__brand + " !"
    
    def full_name(self):
        return f"{self.__brand} {self.model} {self.battery}"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model, battery)
        self.battery= battery

my_tesla= ElectricCar("tesla","Model S","85kWh")
print(my_tesla.full_name())
#print(my_tesla.__brand)
print(my_tesla.get_brand())

