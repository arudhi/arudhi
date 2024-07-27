
class Car:
    def __init__(self, brand, model , battery):
        self.brand = brand
        self.__model = model
        self.battery = battery
    
    def full_name(self):
        return f"{self.brand} {self.__model} {self.battery}"
    
class Battery:
    def battery_info(self):
        return "This is Battery"

class Engine:
    def engine_info(self):
        return "This is Engine"
    
class ElectricCarTWo(Battery, Engine, Car):
    pass
    
my_new_tesla= ElectricCarTWo("Tesla","Model S","85")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())




