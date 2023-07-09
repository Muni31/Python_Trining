# Write a program to handle file open/close and read/write functionality using Exception handling. 
def a(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            print(f"Contents of {file_path}:\n{contents}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IOError:
        print(f"Error reading file '{file_path}'.")

def b(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
            print(f"Successfully wrote to {file_path}.")
    except IOError:
        print(f"Error writing to file '{file_path}'.")

file_path = "1.py"
content = "1.py is opened successfully "

a(file_path)

b(file_path, content)

a(file_path)
