import time


# Function to display patients briefly
def display_patients(patients):

    print("\n========================================")
    print("PATIENT QUEUE")
    print("========================================")

    for patient in patients:
        print(f"{patient.pid} | " f"{patient.name} | " f"Priority: {patient.priority}")

    print("========================================\n")


# Selection Sort (Descending Priority)
def selection_sort(patients):

    sorted_patients = patients.copy()

    n = len(sorted_patients)

    for i in range(n):

        max_index = i

        for j in range(i + 1, n):

            if sorted_patients[j].priority > sorted_patients[max_index].priority:
                max_index = j

        # Swap
        sorted_patients[i], sorted_patients[max_index] = (
            sorted_patients[max_index],
            sorted_patients[i],
        )

    return sorted_patients


# Merge Function
def merge(left, right):

    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i].priority >= right[j].priority:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Merge Sort
def merge_sort(patients):

    if len(patients) <= 1:
        return patients

    mid = len(patients) // 2

    left_half = merge_sort(patients[:mid])
    right_half = merge_sort(patients[mid:])

    return merge(left_half, right_half)


# Compare Sorting Algorithms
def compare_sorting_algorithms(patients):

    print("\n========== SORTING COMPARISON ==========\n")

    # Selection Sort Timing
    start = time.time()

    selection_sorted = selection_sort(patients)

    end = time.time()

    selection_time = end - start

    print("SELECTION SORT OUTPUT:")
    display_patients(selection_sorted)

    print(f"Selection Sort Time: {selection_time:.10f} seconds")
    print("Time Complexity: O(n^2)\n")

    # Merge Sort Timing
    start = time.time()

    merge_sorted = merge_sort(patients)

    end = time.time()

    merge_time = end - start

    print("MERGE SORT OUTPUT:")
    display_patients(merge_sorted)

    print(f"Merge Sort Time: {merge_time:.10f} seconds")
    print("Time Complexity: O(n log n)\n")
