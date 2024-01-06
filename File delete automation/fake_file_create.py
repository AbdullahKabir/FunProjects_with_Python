import os
import datetime
from faker import Faker

def create_fake_files(directory, num_files):
    fake = Faker()

    for i in range(num_files):
        # Generate a fake filename and timestamp
        fake_filename = fake.file_name()
        fake_timestamp = fake.date_time_between(start_date="-365d", end_date="now")

        # Create the file path
        file_path = os.path.join(directory, fake_filename+str('.json'))
        file_path = os.path.join(directory, fake_filename)

        # Create the file with fake timestamp
        with open(file_path, 'w') as file:
            file.write(f"Fake file content created at: {fake_timestamp}")

        # Set the fake timestamp for the file
        os.utime(file_path, (fake_timestamp.timestamp(), fake_timestamp.timestamp()))

        print(f"Created file: {fake_filename} with timestamp: {fake_timestamp}")

# Specify the directory where you want to create fake files
directory_to_create = 'S:\Temp'
# Specify the number of fake files to create
num_fake_files = 20

create_fake_files(directory_to_create, num_fake_files)