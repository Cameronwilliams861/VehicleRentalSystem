from vehicle import Vehicle
class Rental:
    def __init__(self, rental_id, customer, vehicle, rental_days):
        self.rental_id = rental_id
        self.customer = customer
        #In main.py I'm passing in the object here, so you can make calls to it's objects
        self.vehicle = vehicle
        self.rental_days = rental_days
        self.total_cost = 0
        self.is_active = True

    #self.vehicle.daily_rate is how you would access daily_rate variable in the vehicle class
    def calculate_rental_cost(self):
        print("Below is the vehicle object:")
        print(self.vehicle)
        print("Below is a calculation of the (vehicle Object).daily_rate * self.rental_days")
        self.total_cost = self.vehicle.daily_rate * self.rental_days
        print(self.vehicle.daily_rate * self.rental_days)
        return self.total_cost

    def complete_rental(self):
        if self.is_active:
            self.is_active = False
            self.vehicle.return_vehicle()
            return True
        else:
            return False

    def get_rental_details(self):
        print(f"The Vehicle ID: {self.rental_id}\nCustomer: {self.customer.name}\nModel: {self.vehicle.model}\nRental Days: {self.rental_days}\nRate: {self.vehicle.daily_rate}\nTotal Cost: {self.total_cost} ")