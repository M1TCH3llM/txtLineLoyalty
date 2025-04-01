"""importing the required libraries"""
import os

"""defining the path of the loyalty.txt file"""
LOYALTY_FILE = 'loyalty.txt'

def load_loyalty():
    
    data = {}
    """function to load the loyalty points from the loyalty.txt file"""
    if os.path.exists(LOYALTY_FILE):

        with open(LOYALTY_FILE, 'r') as f:

            for line in f:
                name, points = line.strip().split(",")

                data[name] = int(points)

    return data

def save_loyalty(data):
    """function to save the loyalty points to the loyalty.txt file"""
    with open(LOYALTY_FILE, 'w') as f:

        for name, points in data.items():
            f.write(f"{name},{points}\n")

def add_points(data, name, points):
    if name in data:
        data[name] += points
    else:
        data[name] = points
        print(f"Added {points} points to {name}. New balance is {data[name]}")

def welcome_message():
    print("Welcome to the Loyalty Points App")
    print("-------------------------------")

def main():
    data = load_loyalty()

    while True:
        name = input("Enter the customer's name: ")
        points = int(input("Enter the number of points to add: "))

        add_points(data, name, points)

        save_loyalty(data)

        if input("Do you want to add more points? (y/n) ") != 'y':
            break