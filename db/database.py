import sqlite3
import pandas as pd


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('db/blood_sugar_tracker.db')
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS measurements (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id INTEGER NOT NULL,
                            glucose_level REAL NOT NULL,
                            measurement_date DATE NOT NULL,
                            FOREIGN KEY (user_id) REFERENCES users(id))''')

        self.conn.commit()

    def add_user(self, user):
        self.cursor.execute("INSERT INTO users (name) VALUES (?)", (user.name,))

        self.conn.commit()

    def add_measurement(self, measurement):
        self.cursor.execute("INSERT INTO measurements (user_id, glucose_level, measurement_date) VALUES (?, ?, ?)",
                            (measurement.user_id, measurement.glucose_level, measurement.measurement_date))
        self.conn.commit()

    # Inne metody obsługujące bazę danych
    def get_measurements(self, user_id):
        self.cursor.execute("SELECT glucose_level, measurement_date FROM measurements WHERE user_id = ?", (user_id,))
        data = self.cursor.fetchall()
        my_data = pd.DataFrame(data, columns=['Pomiar cukru', 'Data pomiaru'])
        sorted_data = my_data.sort_values(by='Data pomiaru', ascending=False)
        print(sorted_data)
        return sorted_data

    def __del__(self):
        self.conn.close()
