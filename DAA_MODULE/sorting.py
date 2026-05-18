import time


# Function to display patients briefly
def display_patients(patients):

    print("\n========================================")
    print("PATIENT QUEUE")
    print("========================================")

    for patient in patients:
        print(f"{patient.pid} | " f"{patient.name} | " f"Priority: {patient.priority}")

    print("========================================\n")


# Quick Sort (Descending Priority)
def quick_sort(patients):

    if len(patients) <= 1:
        return patients.copy()

    pivot = patients[len(patients) // 2]

    higher_priority = []
    same_priority = []
    lower_priority = []

    for patient in patients:
        if _has_higher_triage_order(patient, pivot):
            higher_priority.append(patient)
        elif _has_higher_triage_order(pivot, patient):
            lower_priority.append(patient)
        else:
            same_priority.append(patient)

    return quick_sort(higher_priority) + same_priority + quick_sort(lower_priority)


def _has_higher_triage_order(patient, other_patient):
    if patient.priority != other_patient.priority:
        return patient.priority > other_patient.priority

    return patient.arrival_time < other_patient.arrival_time


# Insertion Sort (Descending Priority)
def insertion_sort(patients):

    sorted_patients = patients.copy()

    for i in range(1, len(sorted_patients)):
        current_patient = sorted_patients[i]
        j = i - 1

        while j >= 0 and _has_higher_triage_order(
            current_patient, sorted_patients[j]
        ):
            sorted_patients[j + 1] = sorted_patients[j]
            j -= 1

        sorted_patients[j + 1] = current_patient

    return sorted_patients


# Run Quick Sort and display timing
def run_quick_sort(patients):

    print("\n========== QUICK SORT ==========\n")

    start = time.time()

    quick_sorted = quick_sort(patients)

    end = time.time()

    quick_time = end - start

    print("QUICK SORT OUTPUT:")
    display_patients(quick_sorted)
    print(f"Quick Sort Time: {quick_time:.10f} seconds")
    print("Average Time Complexity: O(n log n)")
    print("Worst Time Complexity: O(n^2)\n")

    return quick_sorted


# Run Insertion Sort and display timing
def run_insertion_sort(patients):

    print("\n========== INSERTION SORT ==========\n")

    start = time.time()

    insertion_sorted = insertion_sort(patients)

    end = time.time()

    insertion_time = end - start

    print("INSERTION SORT OUTPUT:")
    display_patients(insertion_sorted)
    print(f"Insertion Sort Time: {insertion_time:.10f} seconds")
    print("Best Time Complexity: O(n)")
    print("Average/Worst Time Complexity: O(n^2)\n")

    return insertion_sorted
