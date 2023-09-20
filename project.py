import datetime
class User:
    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth

class IDCardGenerator:
    def __init__(self):
        self.counter = 1

    def generate_id_card(self, user):
        # Generate a 9-character numerical ID padded with leading zeros
        unique_id = f"{self.counter:09}"
        self.counter += 1
        return unique_id

# Create an instance of the IDCardGenerator
id_card_generator = IDCardGenerator()

# Get user information
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
dob_str = input("Enter date of birth (YYYY-MM-DD): ")

# Parse the date of birth string to a datetime object
date_of_birth = datetime.datetime.strptime(dob_str, "%Y-%m-%d")

# Create a User instance
user = User(first_name, last_name, date_of_birth)

# Generate the unique numerical ID card
id_card = id_card_generator.generate_id_card(user)

print(f"User ID Card: {id_card}")

