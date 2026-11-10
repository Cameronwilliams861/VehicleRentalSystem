from vehicle import Vehicle
from customer import Customer
from rental import Rental
from rentalcompany import RentalCompany

car1 = Vehicle(vehicle_id = 500, make="Toyota", model="4Runner", daily_rate=50, year="2025")
car2 = Vehicle(vehicle_id = 501, make="Honda", model="CR-V", daily_rate=50, year="2025")

customer1 = Customer(name="Cameron",customer_id="5000",email="Camjamwam@gmail.com")

#Testing out the customer class
customer1.get_customer_info()
customer1.add_rental(car1)
customer1.add_rental(car2)
customer1.get_rental_history()

#Testing out the Rental class
rental1 = Rental(rental_id = car1.vehicle_id, customer=customer1.name, vehicle = car1.model, rental_days= 5)
rental1.calculate_rental_cost()
print("\n")
rental1.complete_rental()
print("\n")
rental1.get_rental_details()
