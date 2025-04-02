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
    if name in data:
        data[name] += points
    else:
        data[name] = points
        print(f"Added {points} points to {name}. New balance is {data[name]}")

def reedem_points(data, name, points):

    if name in data:
        if data[name] >= points:
            data[name] -= points
            print(f"Reedemed {points} points from {name}. New balance is {data[name]}")
        else:
            print(f"{name} does not have enough points to reedem")
    else: 
         print(f"{name} not founbd in data base")

def list_points(data):

    if not data:
        print("No loyalty points available")
    else:
        print("Loyalty points:")
        for name, points in data.items():
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
    
    if name in data:
        print(f"{name} has {data[name]} points")
    else:
        print(f"{name} not found in database")

def main():
    data = load_loyalty()

    while True:
        command = input(">").strip().split()

        if not command:
            continue
        action = command[0].lower()

        if action == 'add':
            if len(command) == 3:
                name = command[1]
                try:
                    points = int(command[2])
                    add_points(data, name, points)
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
