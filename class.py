#Basic Class and Object
class Car:
    def __init__(self, ubrand, umodel):
        self.brand = ubrand
        self.model = umodel
    
    def full_name(self):
        return f"{self.brand} {self.model}"
        
    

my_car = Car("toyota","corolla")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())

my_new_car = Car("Tata","Safari")
print(my_new_car.model)
print(my_new_car.brand)
print(my_new_car.full_name())