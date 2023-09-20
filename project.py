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



'''
# this works
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
        unique_id = f"{user.first_name.upper()[0]}{user.last_name.upper()[0]}{user.date_of_birth.year}-{self.counter:04}"
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

# Generate the unique ID card
id_card = id_card_generator.generate_id_card(user)

print(f"User ID Card: {id_card}")



# this code is not working
class User:
    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth

class IDCardGenerator:
    def __init__(self):
        self.counter = 1

    def generate_id_card(self, user):
        unique_id = f"{user.first_name.upper()[0]}{user.last_name.upper()[0]}{user.date_of_birth.year}-{self.counter:04}"
        self.counter += 1
        return unique_id

# Create an instance of the IDCardGenerator
id_card_generator = IDCardGenerator()
# Get user information
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")

# Create a User instance
user = User(first_name, last_name, date_of_birth)

# Generate the unique ID card
id_card = id_card_generator.generate_id_card(user)

print(f"User ID Card: {id_card}")





#third example
class IDGenerator:
    def __init__(self):
        self.counter = 1

    def generate_id(self):
        unique_id = self.counter
        self.counter += 1
        return unique_id

# Create an instance of the IDGenerator
id_generator = IDGenerator()

# Get input from the user (e.g., name, email, or any identifying data)
user_input = input("Enter input data: ")

# Generate a unique ID based on the counter
unique_id = id_generator.generate_id()

print(f"Unique ID for '{user_input}': {unique_id}")




#secound example
import uuid

def generate_unique_id(input_data):
    # Generate a UUID based on the input data
    unique_id = uuid.uuid5(uuid.NAMESPACE_DNS, input_data)
    return str(unique_id)

# Get input from the user (e.g., name, email, or any identifying data)
user_input = input("Enter input data: ")

# Generate a unique ID based on the input data
unique_id = generate_unique_id(user_input)

print(f"Unique ID for '{user_input}': {unique_id}")



#first example
a = 5
b = 6
sum = a + b

# id of sum variable
print("The id of sum is", id(sum))

# Output: The id of sum is 9789312
'''