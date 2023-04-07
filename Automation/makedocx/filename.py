import os

# Get the path of the first folder
folder_path1 = input("Enter the path of the first folder: ")

# Get the list of files in the first folder
files1 = os.listdir(folder_path1)

# Filter the list to include only .py files
py_files1 = [file for file in files1 if file.endswith('.py')]

# Create a list of filenames without the .py extension
file_names1 = [file[:-3] for file in py_files1]

# Print the list of filenames without the .py extension in the first folder
print("The filenames without the .py extension in the first folder are:")
print(file_names1)

# Get the path of the second folder
folder_path2 = input("Enter the path of the second folder: ")

# Get the list of files in the second folder with .png extension
files2 = os.listdir(folder_path2)

png_files2 = [file for file in files2 if file.endswith('.png')]

# Print the list of .png files in the second folder
print("The .png files in the second folder are:")
print(png_files2)