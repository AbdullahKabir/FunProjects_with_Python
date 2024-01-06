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
num_fake_files = 100

create_fake_files(directory_to_create, num_fake_files)


# Copyright (c) 2024 Abdullah Md Humayun Kabir
# All rights reserved.

# This file is part of the MyProject "Funprojects with python".
# It is subject to the license terms in the LICENSE file found in the top-level
# directory of this distribution and at https://github.com/AbdullahKabir/FunProjects_with_Python.

# NO WARRANTY. See the LICENSE file for details.

'''
This file is created and maintained by
Abdullah Md Humayun Kabir
Email: abdullah.kabir12@gmail.com

'''
