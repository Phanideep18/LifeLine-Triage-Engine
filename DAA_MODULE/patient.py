class Patient:
    TIME_UNIT = "minutes"

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
        waiting_time = getattr(self, "waiting_time", "N/A")
        turnaround_time = getattr(self, "turnaround_time", "N/A")
        completion_time = getattr(self, "completion_time", "N/A")

        print(f"""
Patient ID       : {self.pid}
Name             : {self.name}
Arrival Time     : {self.arrival_time} {self.TIME_UNIT}
Heart Rate       : {self.heart_rate}
Blood Pressure   : {self.blood_pressure}
Oxygen Level     : {self.oxygen_level}
Severity         : {self.severity}
Burst Time       : {self.burst_time} {self.TIME_UNIT}
Priority Score   : {self.priority}
Waiting Time     : {waiting_time} {self.TIME_UNIT if waiting_time != "N/A" else ""}
Turnaround Time  : {turnaround_time} {self.TIME_UNIT if turnaround_time != "N/A" else ""}
Completion Time  : {completion_time} {self.TIME_UNIT if completion_time != "N/A" else ""}
""")


def select_patient_details(patients):
    print("\n========== PATIENT DETAIL VIEW ==========\n")
    print("Enter Patient ID to view full details.")
    print("Enter Q to exit.\n")

    for index, patient in enumerate(patients, start=1):
        print(f"{index}. {patient.pid} | {patient.name} | Priority: {patient.priority}")

    patients_by_id = {patient.pid.upper(): patient for patient in patients}

    while True:
        try:
            choice = input("\nPatient ID: ").strip()
        except EOFError:
            print("\nDetail view skipped because no input was provided.")
            return

        if choice.lower() == "q":
            print("Exiting patient detail view.")
            return

        normalized_choice = choice.upper().replace(" ", "")
        if normalized_choice.isdigit():
            normalized_choice = "P" + normalized_choice

        selected_patient = patients_by_id.get(normalized_choice)

        if selected_patient:
            selected_patient.display()
        else:
            print("Invalid Patient ID. Please enter a valid ID like P1, P5, or P26.")
