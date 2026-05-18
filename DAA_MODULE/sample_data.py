from DAA_MODULE.patient import Patient
# Sample Patient Data

   
patients = [

    Patient("P1", "Rahul", 0, 130, 90, 85, 9, 6),
    Patient("P2", "Asha", 1, 95, 120, 97, 4, 3),
    Patient("P3", "Kiran", 2, 125, 95, 88, 8, 5),
    Patient("P4", "Meena", 3, 110, 105, 92, 5, 4),
    Patient("P5", "Arjun", 4, 140, 85, 80, 10, 7),

    Patient("P6", "Sneha", 5, 100, 115, 95, 3, 2),
    Patient("P7", "Vikram", 6, 128, 98, 89, 7, 6),
    Patient("P8", "Divya", 7, 90, 110, 99, 2, 3),
    Patient("P9", "Rohan", 8, 135, 92, 84, 9, 5),
    Patient("P10", "Priya", 9, 118, 108, 93, 4, 4),

    Patient("P11", "Anil", 10, 145, 88, 82, 10, 8),
    Patient("P12", "Kavya", 11, 105, 112, 96, 5, 3),
    Patient("P13", "Suresh", 12, 122, 99, 87, 8, 6),
    Patient("P14", "Neha", 13, 98, 118, 98, 3, 2),
    Patient("P15", "Manoj", 14, 138, 91, 83, 9, 7),

    Patient("P16", "Ritika", 15, 150, 86, 81, 10, 8),
    Patient("P17", "Deepak", 16, 102, 109, 94, 5, 3),
    Patient("P18", "Nisha", 17, 127, 97, 88, 8, 5),
    Patient("P19", "Varun", 18, 132, 93, 85, 9, 6),
    Patient("P20", "Pooja", 19, 108, 114, 97, 4, 4),

    Patient("P21", "Ajay", 20, 142, 89, 82, 10, 7),
    Patient("P22", "Shreya", 21, 99, 117, 96, 3, 2),
    Patient("P23", "Harish", 22, 124, 96, 89, 7, 5),
    Patient("P24", "Lavanya", 23, 111, 103, 91, 6, 4),
    Patient("P25", "Tarun", 24, 136, 90, 84, 9, 6)

]




# Calculate priority for all patients
for patient in patients:
    patient.calculate_priority()

# Display all patient details
if __name__ == "__main__":

    print("\n========== SAMPLE PATIENT DATA ==========\n")

    for patient in patients:
        patient.display()
