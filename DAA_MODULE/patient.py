class Patient:
    def __init__(
        self,
        pid,
        name,
        arrival_time,
        heart_rate,
        blood_pressure,
        oxygen_level,
        severity,
        burst_time,
    ):

        # Basic Details
        self.pid = pid
        self.name = name
        self.arrival_time = arrival_time

        # Medical Vitals
        self.heart_rate = heart_rate
        self.blood_pressure = blood_pressure
        self.oxygen_level = oxygen_level
        self.severity = severity

        # Treatment Time
        self.burst_time = burst_time

        # Calculated Later
        self.priority = 0

    # Function to calculate emergency priority
    def calculate_priority(self):

        priority_score = 0

        # Oxygen Level Check
        if self.oxygen_level < 90:
            priority_score += 5

        # Heart Rate Check
        if self.heart_rate > 120:
            priority_score += 3

        # Blood Pressure Check
        if self.blood_pressure < 100:
            priority_score += 2

        # Symptom Severity
        priority_score += self.severity

        self.priority = priority_score

    # Display patient details
    def display(self):
        print(f"""
Patient ID       : {self.pid}
Name             : {self.name}
Arrival Time     : {self.arrival_time}
Heart Rate       : {self.heart_rate}
Blood Pressure   : {self.blood_pressure}
Oxygen Level     : {self.oxygen_level}
Severity         : {self.severity}
Burst Time       : {self.burst_time}
Priority Score   : {self.priority}
""")
