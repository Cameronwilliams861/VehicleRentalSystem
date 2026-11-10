class RentalCompany:
    def __init__(self, company_name):
        # Company attributes
        self.company_name = company_name
        self.vehicles = []
        self.customers = []
        self.rentals = []

    # Add a vehicle to the company's fleet
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    # Register a new customer
    def register_customer(self, customer):
        self.customers.append(customer)

    # Find a vehicle using its vehicle ID
    def find_vehicle(self, vehicle_id):
        #Loop through the objects in self.vehicle
        #Since "vehicles" will be a vehicle object, we should be able to call it's parameters to pull it's value

        for vehicles in self.vehicles:
            if vehicles.vehicle_id == vehicle_id:
                return True
        return False


    # Find a customer using their customer ID
    def find_customer(self, customer_id):
        for customers in self.customers:
            if customers.customer_id == customer_id:
                return True
        return False

    # Create a rental for a customer and vehicle
    def rent_vehicle(self, customer_id, vehicle_id, rental_days):
        #if the vehicle is available, the customer should be able to rent it
        pass

    # Complete an existing rental
    def return_vehicle(self, rental_id):
        pass

    # Display a report of the company's activity
    def generate_company_report(self):
        pass