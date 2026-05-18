def priority_scheduling(patients):
    print("\n========== PRIORITY SCHEDULING ==========\n")

    time = 0
    gantt_chart = []

    for patient in patients:
        if time < patient.arrival_time:
            time = patient.arrival_time

        start_time = time
        completion_time = start_time + patient.burst_time

        patient.waiting_time = start_time - patient.arrival_time
        patient.turnaround_time = completion_time - patient.arrival_time
        patient.completion_time = completion_time

        gantt_chart.append((patient.pid, start_time, completion_time))

        time = completion_time

    print("Gantt Chart:")
    for pid, start, end in gantt_chart:
        print(f"| {pid} ", end="")
    print("|")

    for pid, start, end in gantt_chart:
        print(f"{start}    ", end="")
    print(gantt_chart[-1][2])

    print("\nPatient Scheduling Table:")
    print("PID\tPriority\tArrival\tBurst\tWaiting\tTurnaround\tCompletion")

    total_waiting = 0
    total_turnaround = 0

    for p in patients:
        total_waiting += p.waiting_time
        total_turnaround += p.turnaround_time

        print(
            f"{p.pid}\t{p.priority}\t\t{p.arrival_time}\t"
            f"{p.burst_time}\t{p.waiting_time}\t{p.turnaround_time}\t\t{p.completion_time}"
        )

    n = len(patients)

    print("\nAverage Waiting Time:", round(total_waiting / n, 2))
    print("Average Turnaround Time:", round(total_turnaround / n, 2))


def round_robin(patients, time_quantum):
    print("\n========== ROUND ROBIN SCHEDULING ==========\n")

    queue = sorted(patients, key=lambda p: p.arrival_time)

    remaining_time = {}
    completion_time = {}

    for p in queue:
        remaining_time[p.pid] = p.burst_time

    time = 0
    ready_queue = []
    completed = 0
    visited = set()
    gantt_chart = []

    while completed < len(queue):

        for p in queue:
            if p.arrival_time <= time and p.pid not in visited:
                ready_queue.append(p)
                visited.add(p.pid)

        if not ready_queue:
            time += 1
            continue

        current = ready_queue.pop(0)

        start_time = time

        if remaining_time[current.pid] > time_quantum:
            time += time_quantum
            remaining_time[current.pid] -= time_quantum
        else:
            time += remaining_time[current.pid]
            remaining_time[current.pid] = 0
            completion_time[current.pid] = time
            completed += 1

        gantt_chart.append((current.pid, start_time, time))

        for p in queue:
            if p.arrival_time <= time and p.pid not in visited:
                ready_queue.append(p)
                visited.add(p.pid)

        if remaining_time[current.pid] > 0:
            ready_queue.append(current)

    print("Gantt Chart:")
    for pid, start, end in gantt_chart:
        print(f"| {pid} ", end="")
    print("|")

    for pid, start, end in gantt_chart:
        print(f"{start}    ", end="")
    print(gantt_chart[-1][2])

    print("\nPatient Scheduling Table:")
    print("PID\tArrival\tBurst\tWaiting\tTurnaround\tCompletion")

    total_waiting = 0
    total_turnaround = 0

    for p in queue:
        p.completion_time = completion_time[p.pid]
        p.turnaround_time = p.completion_time - p.arrival_time
        p.waiting_time = p.turnaround_time - p.burst_time

        total_waiting += p.waiting_time
        total_turnaround += p.turnaround_time

        print(
            f"{p.pid}\t{p.arrival_time}\t{p.burst_time}\t"
            f"{p.waiting_time}\t{p.turnaround_time}\t\t{p.completion_time}"
        )

    n = len(queue)

    print("\nAverage Waiting Time:", round(total_waiting / n, 2))
    print("Average Turnaround Time:", round(total_turnaround / n, 2))
