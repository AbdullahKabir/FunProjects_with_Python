# Copyright (c) 2024 Abdullah Md Humayun Kabir
# All rights reserved.

# This file is part of the MyProject "Funprojects with python".
# It is subject to the license terms in the LICENSE file found in the top-level
# directory of this distribution and at https://github.com/AbdullahKabir/FunProjects_with_Python.

# NO WARRANTY. See the LICENSE file for details.

import os
import datetime

def delete_old_files(directory):
    current_time = datetime.datetime.now()
    threshold_60_days_ago = current_time - datetime.timedelta(days=60)
    threshold_7_days_ago = current_time - datetime.timedelta(days=7)

    for filename in os.listdir(directory):
        
        file_path = os.path.join(directory, filename)
        # Check if it's a file and not a directory
        if os.path.isfile(file_path):
            # Get the creation time of the file
            creation_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
            if creation_time > threshold_60_days_ago:
                print(f"This file is modified within 60days: {creation_time - threshold_60_days_ago}")
                if creation_time < threshold_7_days_ago and creation_time.weekday() == 6:
                    print(f"This file is modified within 7days or on Sunday: {filename} {creation_time - threshold_7_days_ago}")
                    continue  # Skip this file
                # Delete the file
                os.remove(file_path)
                print(f"Deleted: {filename}")
                print(" ")
            # Check if the file is created more than 60 days ago
            elif creation_time < threshold_60_days_ago:
                print(f"This file is modified after 60days: {filename} {creation_time - threshold_60_days_ago}" )
                # Check if the file is created within the last 7 days and not on Sunday
                os.remove(file_path)
                print(f"Deleted: {filename}")
                print(" ")

# Specify the directory where you want to delete old files
directory_to_clean = 'S:\Temp'
delete_old_files(directory_to_clean) 

'''
This file is created and maintained by
Abdullah Md Humayun Kabir
Email: abdullah.kabir12@gmail.com

'''