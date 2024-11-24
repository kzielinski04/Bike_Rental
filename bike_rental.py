import json, datetime, os, smtplib

'''
##### Milestone 3: Praca z plikiem rentals.json
1. **Funkcja load_rentals()**
   - Implementuj funkcję do odczytu istniejących wynajmów z pliku `rentals.json`.
   - Wyświetl wszystkie zapisane wynajmy.

2. **Funkcja cancel_rental(customer_name)**
   - Implementuj funkcję do anulowania wynajmu na podstawie imienia klienta.
   - Wczytaj dane z pliku `rentals.json`, usuń odpowiedni rekord i zapisz zmodyfikowane dane z powrotem do pliku.
'''

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
    rental = {"Customer name" : customer_name, "Rental duration" : rental_duration, "Rental cost" : calculate_cost(rental_duration)}
    save_rental(rental)

#This function saves rental to the file
def save_rental(rental:dict):
    if os.path.exists("./data/rentals.json"):
        load_rentals()
    else:
        rentals = []
    rentals.append(rental)
    with open("./data/rentals.json", 'w') as file:
        json.dump(rentals, file, indent = 3)

#This function loads rentals from the file
def load_rentals():
    if os.path.exists("./data/rentals.json"):
        with open("./data/rentals.json", 'r') as file:
            rentals = json.load(file)

#Simple menu
def menu():
    print("---------------------")
    print("-----BIKE RENTAL-----")
    print("---------------------")
    print("1 - RENT A BIKE")
    print("2 - EXIT")
    choice = int(input("Choose an option: "))
    match choice:
        case 1:
            customer_name = input("What's your name?: ")
            rental_duration = int(input("For how many hours would you like to rent a bike?: "))
            print(f"That'll cost {calculate_cost(rental_duration)} PLN.\n")
            rent_bike(customer_name, rental_duration)
            menu()
        case 2:
            exit()

menu()