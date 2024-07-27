
class Car:
    def __init__(self, brand, model , battery):
        self.brand = brand
        self.model = model
        self.battery = battery
    
    def full_name(self):
        return f"{self.brand} {self.model} {self.battery}"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model, battery)
        self.battery= battery

my_tesla= ElectricCar("tesla","Model S","85kWh")
print(my_tesla.full_name())

