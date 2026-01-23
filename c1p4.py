import os
# Path of the directory you want to list
# You can change this to any valid directory path
directory_path = '/Users/VAISHNAVI'
# Get the list of all files and directories
contents = os.listdir(directory_path)
# Print the contents
print("Contents of the directory:")
for item in contents:
    print(item)
