
class Car:
    def __init__(self, brand, model , battery):
        self.brand = brand
        self.__model = model
        self.battery = battery
    
    def full_name(self):
        return f"{self.brand} {self.__model} {self.battery}"
    
    
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    @property
    def model(self):
        return self.__model
    
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model, battery)
        self.battery= battery
    
    

my_tesla= ElectricCar("Tesla","Model S","85kWh")

print(my_tesla.general_description())

safari=Car("Tata","Safari", "100kWh")

print(safari.general_description())


print(safari.model)
print(my_tesla.model)