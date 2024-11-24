import json, datetime, os, smtplib

'''
1. **Funkcja rent_bike(customer_name, rental_duration)**
   - Implementuj funkcję, która przyjmuje imię klienta i czas wynajmu.
   - W funkcji wywołaj `calculate_cost()` do obliczenia kosztu wynajmu.
   - Zapisz szczegóły wynajmu do pliku JSON, korzystając z `save_rental()`.

2. **Funkcja calculate_cost(rental_duration)**
   - Implementuj obliczenia kosztu wynajmu roweru.
   - Zasady: pierwsza godzina kosztuje 10 zł, każda następna to 5 zł.

3. **Funkcja save_rental(rental)**
   - Implementuj funkcję zapisującą wynajem do pliku `rentals.json`.
   - Sprawdź, czy plik `rentals.json` istnieje, jeśli nie - utwórz go.
   - Użyj funkcji `json.dump()` do zapisu danych w pliku.
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
        
def rent_bike(customer_name:str, rental_duration:int):
    rental = {"customer_name" : customer_name, "rental_duration" : rental_duration, "rental_cost" : calculate_cost(rental_duration)}
    save_rental(rental)

def save_rental(rental:dict):
    if os.path.exists("./data/rentals.json"):
        with open("./data/rentals.json", 'r') as file:
            rentals = json.load(file)
    else:
        rentals = []
    rentals.append(rental)
    with open("./data/rentals.json", 'w') as file:
        json.dump(rentals, file, indent = 3)