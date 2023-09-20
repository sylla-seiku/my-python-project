import random
import datetime

class User:
    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth

class IDCardGenerator:
    def generate_id_card(self, user):
        # Generate a random 9-digit numerical ID
        unique_id = ''.join(str(random.randint(0, 9)) for _ in range(9))
        return unique_id

# Create an instance of the IDCardGenerator
id_card_generator = IDCardGenerator()

# Get user information
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
dob_str = input("Enter date of birth (MM-DD-YYYY): ")

# Parse the date of birth string to a datetime object
date_of_birth = datetime.datetime.strptime(dob_str, "%m-%d-%Y")

# Create a User instance
user = User(first_name, last_name, date_of_birth)

# Generate the random 9-digit numerical ID
id_card = id_card_generator.generate_id_card(user)

print(f"User ID Card: {id_card}")
