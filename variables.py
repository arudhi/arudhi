
class Car:
    total_car = 0

    def __init__(self, brand, model , battery):
        self.brand = brand
        self.model = model
        self.battery = battery
        Car.total_car += 1
    
    def full_name(self):
        return f"{self.brand} {self.model} {self.battery}"
    
   
Car("Tata","Safari", "100kWh")
Car("Mahindra","Scorpio","110kWh")
print(Car.total_car)




