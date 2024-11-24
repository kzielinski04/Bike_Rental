import json, datetime, os, smtplib
from datetime import datetime

#This function calculates rental cost, depending on rental duration
def calculate_cost(rental_duration:int) -> int:
    match rental_duration:
        case rental_duration if isinstance(rental_duration, int) == False or rental_duration < 1:
            print("Invalid rental duration!\n")
        case 1:
            return 10
        case _:
            return 10 + ((rental_duration - 1) * 5)

#This function allows user to rent a bike and save data to the file         
def rent_bike(customer_name:str, rental_duration:int):
    if rental_duration < 1:
        print("Invalid rental duration!\n")
    else:    
        rental = {"Customer name" : customer_name, "Rental duration" : rental_duration, "Rental cost" : calculate_cost(rental_duration)}
        save_rental(rental)

#This function saves rental to the file
def save_rental(rental:dict):
    rentals = load_rentals()
    rentals.append(rental)
    with open("./data/rentals.json", 'w') as file:
        json.dump(rentals, file, indent = 3)

#This function loads rentals from the file
def load_rentals():
    if not os.path.exists("./data/rentals.json"):
        return []
    with open("./data/rentals.json", 'r') as file:
        rentals = json.load(file)
    return rentals

#This function cancels rental
def cancel_rental(customer_name:str):
    rentals = load_rentals()
    updated_rentals = [rental for rental in rentals if rental["Customer name"] != customer_name]
    if len(updated_rentals) != len(rentals):
        with open("./data/rentals.json", 'w') as file:
            json.dump(updated_rentals, file, indent = 3)
        print("Rental has been cancelled successfully!\n")
        menu()
    else:
        print("Rental not found!\n")
        menu()

#This functions generates a report, that contains all rentals for the current day
def generate_daily_report():
    report_date = datetime.now().strftime("%d-%m-%y")
    report_name = f"./data/daily_report_{report_date}.json"
    rentals = load_rentals()
    with open(report_name, 'w') as file:
        json.dump(rentals, file, indent = 3)
    print(f"Daily report for {report_date} has been created!\n")

#Simple menu
def menu():
    print("---------------------")
    print("-----BIKE RENTAL-----")
    print("---------------------")
    print("1 - RENT A BIKE")
    print("2 - CANCEL A RENTAL")
    print("4 - GENERATE A DAILY REPORT")
    print("5 - EXIT")
    choice = int(input("Choose an option: "))
    match choice:
        case 1:
            try:
                customer_name = input("What's your name?: ")
                rental_duration = int(input("For how many hours would you like to rent a bike?: "))
                print(f"That'll cost {calculate_cost(rental_duration)} PLN.\n")
                rent_bike(customer_name, rental_duration)
                menu()
            except ValueError:
                print("Invalid rental duration!\n")
                menu()
        case 2:
            customer_name = input("What's your name?: ")
            cancel_rental(customer_name)
            menu()
        case 4:
            generate_daily_report()
            menu()
        case 5:
            exit()
menu()