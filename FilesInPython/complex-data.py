def save_user_data():
    # Accept user input for name, email, and contact
    name = input("Enter name: ")
    email = input("Enter email: ")
    contact = input("Enter contact: ")
 
    # Create a string with the user data
    user_data = f"Name: {name}\nEmail: {email}\nContact: {contact}\n"
 
    # Open the file in append mode and write the user data
    #if you use with, you don't have to close the file back.
    with open('user_data.txt', 'a') as file:
        file.write(user_data)
 
    print("User data saved successfully!")
 
def read_user_data():
    # Open the file in read mode
    with open("user_data.txt", "r") as file:
        # Read and print the file contents
        print(file.read())
 
# Save user data
save_user_data()
 
# Read user data from file
read_user_data()