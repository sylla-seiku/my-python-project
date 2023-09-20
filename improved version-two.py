# This code right here generates a new ID every time I enter a value however there is a flow.
# If i enter the same information twice it generates a different ID everytime.
import random
import datetime

class User:
    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth

class IDCardGenerator:
    def __init__(self):
        self.id_file = "generated_ids.txt"  # File to store generated IDs
        self.generated_ids = set(self.load_generated_ids())

    def generate_id_card(self, user):
        while True:
            # Generate a random 9-digit numerical ID
            unique_id = ''.join(str(random.randint(0, 9)) for _ in range(9))
            
            # Check if the generated ID is unique
            if unique_id not in self.generated_ids:
                self.generated_ids.add(unique_id)
                self.save_generated_ids()
                return unique_id

    def load_generated_ids(self):
        try:
            with open(self.id_file, "r") as file:
                return {line.strip() for line in file}
        except FileNotFoundError:
            return set()

    def save_generated_ids(self):
        with open(self.id_file, "w") as file:
            file.writelines(id + "\n" for id in self.generated_ids)

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

# Generate the unique 9-digit numerical ID and save it
id_card = id_card_generator.generate_id_card(user)

print(f"User ID Card: {id_card}")
