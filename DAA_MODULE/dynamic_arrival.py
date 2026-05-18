from DAA_MODULE.patient import Patient


def add_dynamic_patient(patients):
    """
    Adds a new emergency patient during simulation.
    This represents dynamic patient arrival.
    """

    new_patient = Patient(
        "P26",
        "EmergencyCase",
        5,  # arrival_time
        155,  # heart_rate
        85,  # blood_pressure
        80,  # oxygen_level
        10,  # severity
        6,  # burst_time
    )

    new_patient.calculate_priority()

    patients.append(new_patient)

    print("\n========== DYNAMIC PATIENT ARRIVAL ==========")
    print(f"New patient arrived: {new_patient.pid}")
    print(f"Name: {new_patient.name}")
    print(f"Priority Score: {new_patient.priority}")

    return patients
