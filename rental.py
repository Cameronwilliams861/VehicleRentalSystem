class Rental:
    def __init__(self, rental_id, customer, vehicle_to, rental_days):
        self.rental_id = rental_id
        self.customer = customer
        self.vehicle_to = vehicle_to
        self.rental_days = rental_days
        self.total_cost = 0
        self.is_active = True

    #self.vehicle.daily_rate is how you would access daily_rate variable in the vehicle class
    def calculate_rental_cost(self):
        self.total_cost = self.vehicle.daily_rate * self.rental_days
        return self.total_cost

    def complete_rental(self):
        self.is_active = self.vehicle.is_available
        print(self.is_active)

    def get_rental_details(self):
        print(f"The Vehicle ID: {self.rental_id}\nCustomer: {self.customer}\nModel: {self.vehicle_to}\nRental Days: {self.rental_days}\nRate: {self.vehicle.daily_rate}\nTotal Cost: {self.total_cost} ")