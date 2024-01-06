# Automated file deleting and creating fake files

This directory contains two python files,  

- First one is to create files with fake timestamp  
- Second one is to delete files based on conditions 
  
__Use of this__: These files can be used to maintain server backup files. To maintain different server sometimes the server is configured in such a way that it will backup itself everyday.Keeping all the files can result consuming a lot of space.

__Requirments__: 
- Python3
- Faker : This is a python library to create files with fake timestamp

To install "Faker" use
`pip install faker`  

__Steps__:  

__To Create fake files__:
1. Install python and required libraries
2. Open Command promt
3. Navigate to the directory
4. Open the file named "fake_file_create.py"
5. Give the path where the fake files needs to be created in the variable called "directory_to_create"
6. save the file
7. run `python fake_file_create.py`  

__To delete__
1. Install python
2. open command promt
3. Navigate to file directory
4. Open the file named "auto_delete.py"
5. Give the path from which the files will be deleted in the variable called "directory_to_clean"
6. save the file
7. run `python auto_delete.py`  

__Given Conditions__  
##### Fake File Create  
This fake file creation will create 100 files with the time stamp within previous 365 days  
__Remember__: This will create files with fake timestamp of modification date not creation date
##### Auto Delete   
The auto delete script will delete the all the files which are older then 60 days  
This will also delete files which are older then 7 days and was not created on Sunday
