from DAA_MODULE.sample_data import patients
from DAA_MODULE.patient import select_patient_details
from DAA_MODULE.sorting import run_quick_sort, quick_sort, display_patients

from OS_MODULE.scheduling import priority_scheduling, round_robin
from DAA_MODULE.dynamic_arrival import add_dynamic_patient
from OS_MODULE.aging import apply_aging

print("\n========== LIFELINE HOSPITAL TRIAGE ENGINE ==========\n")

print("Original Patient Queue:")
display_patients(patients)

print("\n========== DAA MODULE ==========")
run_quick_sort(patients)

sorted_patients = quick_sort(patients)

print("\nFinal Sorted Queue Sent from DAA Module to OS Module:")
display_patients(sorted_patients)

print("\n========== OS MODULE ==========")

priority_scheduling(sorted_patients)

round_robin(sorted_patients, time_quantum=3)
print("\n========== BONUS FEATURES ==========")

aged_patients = apply_aging(sorted_patients, current_time=10)

aged_sorted_patients = quick_sort(aged_patients)

print("\nQueue After Aging:")
display_patients(aged_sorted_patients)

updated_patients = add_dynamic_patient(aged_sorted_patients)

updated_sorted_patients = quick_sort(updated_patients)

print("\nQueue After Dynamic Arrival and Re-Sorting:")
display_patients(updated_sorted_patients)

print("\nFinal Scheduling After Aging and Dynamic Arrival:")
priority_scheduling(updated_sorted_patients)

select_patient_details(updated_sorted_patients)
