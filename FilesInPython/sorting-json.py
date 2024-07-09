import json
import os
 
def save_user_data():
    user_list = []
 
    while True:
        # Accept user input for name, email, and contact
        name = input("Enter name (or 'quit' to exit): ")
 
        if name.lower() == "quit":
            break
 
        email = input("Enter email: ")
        contact = input("Enter contact: ")
 
        # Create a dictionary with the user data
        user_data = {
            "name": name,
            "email": email,
            "contact": contact
        }
 
        user_list.append(user_data)

    if os.path.exists("user_data.json"):
        # Load existing user data from the file
        with open("user_data.json", "r") as file:
            existing_data = json.load(file)
 
        # Append the new user data to the existing data
        user_list.extend(existing_data)
 
    # Open the file in write mode and save the user data as JSON
    with open("user_data.json", "w") as file:
        json.dump(user_list, file)
 
    print("User data saved successfully!")
 
def read_user_data():
    # Check if the file exists
    if not os.path.exists("FilesInPython/user_data.json"):
        print("No user data found.")
        return
 
    # Open the file in read mode
    with open("FilesInPython/user_data.json", "r") as file:
        # Load the JSON data
        user_list = json.load(file)
 
    # Print the user data
    print("User Data:")
    for user_data in user_list:
        print("Name:", user_data["name"])
        print("Email:", user_data["email"])
        print("Contact:", user_data["contact"])
        print()
 
# Save user data
save_user_data()
 
# Read user data from file
read_user_data()