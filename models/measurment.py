class Measurement:
    def __init__(self, user_id, glucose_level, measurement_date):
        self.user_id = user_id
        self.glucose_level = glucose_level
        self.measurement_date = measurement_date

    def __repr__(self):
        return f"Measurement(user_id={self.user_id}, glucose_level={self.glucose_level}, measurement_date={self.measurement_date})"
