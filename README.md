# Loyalty Points App

This is a simple command-line application for managing customer loyalty points. It allows you to add, redeem, and view loyalty points for customers.

## Features

-**Add Points:** Add loyalty points to a customer's account.
-**Redeem Points:** Redeem loyalty points from a customer's account.
-**Show Points:** Display the current loyalty points for a specific customer.
-**List Points:** List all customers and their loyalty points.
-**Persistence:** Loyalty point data is stored in a `loyalty.txt` file, ensuring data persistence between sessions.
-**Help Command:** Provides a list of available commands.

## Getting Started

### Prerequisites

-Python 3.x installed on your system.

### Installation

1. Clone or download the repository containing the `loyalty_points.py` file.
2. Open a terminal or command prompt and navigate to the directory containing the file.

### Usage

1. Run the application by executing the following command:

    ```bash
    python loyalty_points.py
    ```

2. The application will display a welcome message and a list of available commands.

3. Use the following commands to manage loyalty points:

    - `add <name> <points>`: Adds `<points>` to the customer named `<name>`.
    - `redeem <name> <points>`: Redeems `<points>` from the customer named `<name>`.
    - `show <name>`: Shows the current points for the customer named `<name>`.
    - `list`: Lists all customers and their points.
    - `help`: Displays the help message with available commands.
    - `exit`: Exits the application.

### Example

```bash
> add Alice 100
Added 100 points to Alice. New balance is 100
> add Bob 50
Added 50 points to Bob. New balance is 50
> list
Loyalty points:
Alice: 100
Bob: 50
> redeem Alice 30
Reedemed 30 points from Alice. New balance is 70
> show Alice
Alice has 70 points
> show charlie
charlie not found in database
> exit
```