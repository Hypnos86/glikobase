import datetime
from db.database import Database
from models.user import User
from models.measurment import Measurement


def display_menu():
    print("1. Dodaj użytkownika")
    print("2. Dodaj pomiar cukru")
    print("3. Wyświetl dane")
    print("4. Wyjdź")


def main():
    db = Database()  # Inicjalizacja bazy danych
    db.create_tables()  # Stworzenie tabel w bazie danych

    while True:
        display_menu()
        choice = input("Wybierz opcję: ")

        if choice == "1":
            name = input("Podaj imię użytkownika: ")
            user = User(None, name)
            db.add_user(user)
            print("Użytkownik dodany pomyślnie!")
        elif choice == "2":
            user_id = input("Podaj ID użytkownika: ")
            glucose_level = float(input("Podaj poziom cukru: "))
            measurement_date = input("Podaj datę pomiaru (RRRR-MM-DD): ")
            year, month, day = map(int, measurement_date.split('-'))
            measurement_date = datetime.date(year, month, day)
            measurement = Measurement(user_id, glucose_level, measurement_date)
            db.add_measurement(measurement)
            print("Pomiar dodany pomyślnie!")
        elif choice == "3":
            user_id = input("Podaj ID użytkonika: ")
            db.get_measurements(user_id)
        elif choice == "4":
            print("Do widzenia!")
            break
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")


if __name__ == "__main__":
    main()
