class Customer:
    def __init__(self, name, customer_id, email):
        self.name = name
        self.customer_id = customer_id
        self.email = email
        self.rental_history = []

    def get_customer_info(self):
        print(f"Name: {self.name}\nCustomer ID: {self.customer_id}\nEmail: {self.email}")

    def add_rental(self,rental):
        self.rental_history.append(rental)

    # Learned a pretty important lesson here. Since it's a vehicle object, you can only access it with it's objects
    def get_rental_history(self):
        print(f"{self.name} rented the following vehicles:\n")
        for rental in self.rental_history:
            print(f"Make: {rental.make}\nModel: {rental.model}\nYear: {rental.year}\n")