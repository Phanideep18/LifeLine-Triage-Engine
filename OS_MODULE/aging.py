def apply_aging(patients, current_time, threshold=5, boost=2):
    """
    Aging mechanism:
    If a patient waits longer than threshold,
    their priority is increased.
    """

    print("\n========== AGING MECHANISM ==========")

    for patient in patients:
        waiting_time = current_time - patient.arrival_time

        if waiting_time >= threshold:
            old_priority = patient.priority
            patient.priority += boost

            print(
                f"{patient.pid} waited {waiting_time} units "
                f"=> Priority increased from {old_priority} to {patient.priority}"
            )

    return patients
