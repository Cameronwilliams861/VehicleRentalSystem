class Vehicle:
    def __init__(self, vehicle_id, make, model, year, daily_rate):
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.year = year
        self.daily_rate = daily_rate
        self.is_available = True

    def get_vehicle_info(self):
        print(self.vehicle_id, self.make, self.model, self.year, self.daily_rate)

    def rent_vehicle(self):
        self.is_available = False
        return self.is_available

    def return_vehicle(self):
        self.is_available = True
        return self.is_available