
class Car:
    def __init__(self, brand, model , battery):
        self.brand = brand
        self.model = model
        self.battery = battery
    
    def full_name(self):
        return f"{self.brand} {self.model} {self.battery}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model, battery)
        self.battery= battery
    
    def fuel_type(self):
        return "Charge"

my_tesla= ElectricCar("Tesla","Model S","85kWh")
print(my_tesla.fuel_type())

safari=Car("Tata","Safari", "100kWh")
print(safari.fuel_type())


