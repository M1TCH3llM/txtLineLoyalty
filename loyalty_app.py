"""importing the required libraries"""
import os

"""defining the path of the loyalty.txt file"""
LOYALTY_FILE = 'loyalty.txt'

'''defining the functions to load the loyalty points, save the loyalty points, add points to the customer, reedem points from the customer, list the points of the customer, show the points of the customer, and the welcome message'''
def load_loyalty():
    
    data = {}
    """function to load the loyalty points from the loyalty.txt file"""
    if os.path.exists(LOYALTY_FILE):
        '''opening the loyalty.txt file in read mode and reading the data from the file'''
        with open(LOYALTY_FILE, 'r') as f:
            '''iterating through the file and splitting the data by comma'''
            for line in f:
                name, points = line.strip().split(",")
                '''storing the data in the dictionary'''
                data[name] = int(points)

    return data

def save_loyalty(data):
    """function to save the loyalty points to the loyalty.txt file"""
    '''opening the loyalty.txt file in write mode and writing the data to the file'''
    with open(LOYALTY_FILE, 'w') as f:
        '''iterating through the dictionary and writing the data to the file'''
        for name, points in data.items():
            '''writing the data to the file'''
            f.write(f"{name},{points}\n")

'''defining the functions to add points to the customer, reedem points from the customer, list the points of the customer, show the points of the customer, and the welcome message'''
def add_points(data, name, points):
    '''checking if the name is in the data'''
    if name in data:
        '''adding the points to the existing points'''
        data[name] += points
        '''printing the message'''
    else:
        '''adding the points to the data'''
        data[name] = points
        '''printing the message'''
        print(f"Added {points} points to {name}. New balance is {data[name]}")

'''defining the function to reedem points from the customer'''
def reedem_points(data, name, points):
    '''checking if the name is in the data'''
    if name in data:
        '''checking if the points are greater than or equal to the points'''
        if data[name] >= points:
            '''deducting the points from the existing points'''
            data[name] -= points
            '''printing the message'''
            print(f"Reedemed {points} points from {name}. New balance is {data[name]}")

        else:
            '''printing the message if the points are not enough to reedem'''
            print(f"{name} does not have enough points to reedem")
    else: 
         '''printing the message if name not found in data'''
         print(f"{name} not founbd in data base")

'''defining the function to list the points of the customer'''
def list_points(data):
    '''checking if the data is empty'''
    if not data:
        print("No loyalty points available")
    else:
        '''printing the loyalty points'''
        print("Loyalty points:")
        '''iterating through the dictionary and printing the data'''
        for name, points in data.items():
            '''printing the data'''
            print(f"{name}: {points}")

def welcome_message():
    print("Welcome to the Loyalty Points App")
    print("-------------------------------")
    print("Commands:")
    print("  add <name> <points> - Adds points to a customer.")
    print("  redeem <name> <points> - Redeems points from a customer.")
    print("  show <name> - Shows a customer's points.")
    print("  list - Lists all customers.")
    print("  help - Displays this help message.")
    print("  exit - Exits the application.")

def Help_message():
    print("Commands:")
    print("  add <name> <points> - Adds points to a customer.")
    print("  redeem <name> <points> - Redeems points from a customer.")
    print("  show <name> - Shows a customer's points.")
    print("  list - Lists all customers.")
    print("  help - Displays this help message.")
    print("  exit - Exits the application.")

def show_points(data, name):
    '''checking if the name is in the data'''
    if name in data:
        '''printing the points of the customer'''
        print(f"{name} has {data[name]} points")
    else:
        '''printing the message if name not found in data'''
        print(f"{name} not found in database")

'''defining the main function'''
def main():
    '''loading the loyalty points from the loyalty.txt file'''
    '''calls the load_loyalty function'''
    data = load_loyalty()

    '''running the loop until the user exits the application'''
    while True:
        '''taking the input from the user'''
        command = input(">").strip().split()
        '''checking if the command is empty'''
        if not command:
            '''continuing the loop'''
            continue
        '''getting the action from the command'''
        action = command[0].lower()

        '''checking the action, adding points, reedem points, show points, list points, help, and exit'''
        if action == 'add':
            '''checking the length of the command'''
            if len(command) == 3:
                '''getting the name and points from the command'''
                name = command[1]
                '''checking if the points is integer'''
                try:
                    '''converting the points to integer'''
                    points = int(command[2])
                    '''calling the add_points function'''
                    add_points(data, name, points)
                    '''handling the exception'''
                except ValueError:
                    print("Invalid points value")
            else:
                print("Usage: add <name> <points>")

        elif action == 'redeem':
            if len(command) == 3:
                name = command[1]
                try:
                    points = int(command[2])
                    reedem_points(data, name, points)
                except ValueError:
                    print("Invalid points value")
            else:
                print("Usage: redeem <name> <points>")
        elif action == 'show':
            if len(command) == 2:
                show_points(data, command[1])
            else:
                print("Usage: show <name>")
        elif action == 'list':
            list_points(data)
        elif action == 'help':
            Help_message()
        elif action == 'exit':
            save_loyalty(data)
            break
        else:
            print("Invalid command")

if __name__ == '__main__':
    welcome_message()
    main()
