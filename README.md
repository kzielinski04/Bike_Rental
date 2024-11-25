# Bike Rental Management System

This is a Python-based **Bike Rental Management System** that allows users to rent bikes, cancel rentals, and generate daily reports. The application is simple to use and stores rental data in JSON files.

---

## Features

1. **Rent a Bike**  
   Users can rent a bike by entering their name and desired rental duration. The cost is calculated automatically and stored in a JSON file.

2. **Cancel a Rental**  
   Users can cancel a rental by providing their name. If a rental with the given name exists, it will be removed.

3. **Generate a Daily Report**  
   The system creates a JSON report of all rentals for the current day.

4. **Menu Interface**  
   A simple command-line interface to navigate through options.

---

## Installation

1. **Prerequisites**  
   Ensure Python 3.10 or later is installed on your machine.

2. **Clone the Repository**  
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
3. **Run the Program**
Execute the script:
```bash
python main.py
```

## Usage
When you run the program, you will see a menu with the following options:
```
---------------------
-----BIKE RENTAL-----
---------------------
1 - RENT A BIKE
2 - CANCEL A RENTAL
3 - GENERATE A DAILY REPORT
4 - EXIT

Choose an option:

    1 - RENT A BIKE: Enter your name and the number of hours you want to rent a bike. The program calculates the cost and saves the details.
    2 - CANCEL A RENTAL: Enter your name to cancel an existing rental.
    3 - GENERATE A DAILY REPORT: Generates a JSON report of all rentals for the current day.
    4 - EXIT: Exit the program.
```
Follow the prompts to interact with the system.

## Daily Report
A daily report is a JSON file generated in the /data/ directory with a name like daily_report_<date>.json. It contains all rentals for the current day in the following format:
```
[
    {
        "Customer name": "Alice",
        "Rental duration": 3,
        "Rental cost": 20
    },
    {
        "Customer name": "Bob",
        "Rental duration": 1,
        "Rental cost": 10
    }
]
```

## Future Improvements

- Email Invoices: Add the ability to send rental invoices via email.