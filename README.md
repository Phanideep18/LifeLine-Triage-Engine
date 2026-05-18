# LifeLine — Hospital Emergency Triage Engine

> **Hackathon PS-01** | Domain: Healthcare | Difficulty: Beginner–Intermediate  
> DAA: Sorting & Efficiency Analysis | OS: Process Scheduling

---

## Problem Statement

City General Hospital's ER receives dozens of patients simultaneously during peak hours. Manual triage by nurses is slow and error-prone, costing critical minutes. **LifeLine** is an automated triage system that prioritizes patients based on their medical vitals and applies OS scheduling algorithms to optimize treatment workflow.

---

## Concepts Implemented

### DAA — Design & Analysis of Algorithms
| Algorithm | Time Complexity | Space Complexity | Use Case |
|---|---|---|---|
| Quick Sort | O(n log n) avg | O(log n) | Primary sorting algorithm for patient prioritization |

- Quick Sort uses a divide-and-conquer approach with mid-point pivot selection
- Efficiently sorts patients in descending priority order with arrival time as tiebreaker
- Single execution time measurement displayed with average and worst-case complexity analysis

### OS — Operating Systems
| Scheduler | Type | Purpose |
|---|---|---|
| Priority Scheduling | Non-preemptive | Highest priority patient treated first to completion |
| Round Robin | Preemptive | Each patient gets a fixed time quantum (3 min), then re-queued |

- Each patient is modeled as a **process** with burst time (treatment duration) and arrival time
- Both schedulers produce a **Gantt chart**, per-patient **waiting time**, **turnaround time**, and averages

### Bonus Features
- **Aging mechanism** — Patients waiting beyond a threshold (5 time units) automatically receive a priority boost (+2), preventing starvation of low-priority patients
- **Dynamic arrivals** — New patients can be added mid-simulation; the queue is instantly re-sorted and re-scheduled
- **Patient detail view** — Interactive feature to query individual patient information including vitals and scheduling times

---

## Priority Scoring

Each patient is scored based on their vitals:

| Vital | Condition | Score Added |
|---|---|---|
| Oxygen Level | < 90% | +5 |
| Heart Rate | > 120 bpm | +3 |
| Blood Pressure | < 100 mmHg | +2 |
| Symptom Severity | Base severity score | variable |

**Calculation:** `priority = oxygen_score + heart_rate_score + bp_score + severity`

---

## Project Structure

```
LifeLine-Triage-Engine/
├── main.py                    ← Entry point - orchestrates the simulation
├── DAA_MODULE/
│   ├── patient.py             ← Patient class definition
│   ├── sample_data.py         ← Pre-loaded patient dataset (25 patients)
│   ├── sorting.py             ← Quick Sort implementation
│   └── dynamic_arrival.py     ← Function to add new patients mid-simulation
├── OS_MODULE/
│   ├── scheduling.py          ← Priority Scheduling & Round Robin implementations
│   └── aging.py               ← Aging mechanism to prevent patient starvation
└── README.md
```

---

## How to Run

**Requirements:** Python 3.8+ (no external libraries needed)

```bash
python main.py
```

This will execute the complete simulation:
1. Load 25 initial patients
2. Display original patient queue
3. Run Quick Sort with timing analysis
4. Execute Priority Scheduling algorithm
5. Execute Round Robin scheduling algorithm
6. Apply aging mechanism
7. Add a dynamic patient arrival
8. Re-sort the updated queue
9. Display final scheduling results
10. Interactive patient detail view

---

## Sample Output

```
========== LIFELINE HOSPITAL TRIAGE ENGINE ==========

Original Patient Queue:
========================================
PATIENT QUEUE
========================================
P1 | Rahul | Priority: 21
P2 | Asha | Priority: 12
P3 | Kiran | Priority: 20
...
========================================

========== DAA MODULE ==========

========== QUICK SORT ==========

QUICK SORT OUTPUT:
========================================
PATIENT QUEUE
========================================
P5 | Arjun | Priority: 24
P11 | Anil | Priority: 24
P16 | Ritika | Priority: 24
...
========================================
Quick Sort Time: 0.0001234567 seconds
Average Time Complexity: O(n log n)
Worst Time Complexity: O(n^2)

Final Sorted Queue Sent from DAA Module to OS Module:
========================================
PATIENT QUEUE
========================================
P5 | Arjun | Priority: 24
...
========================================

========== OS MODULE ==========

========== PRIORITY SCHEDULING ==========

Gantt Chart:
| P5 | P1 | P3 | P7 | P9 | P11 | P13 | P15 | P16 | P18 | P19 | P21 | P23 | P25 | P4 | P10 | P12 | P14 | P17 | P20 | P22 | P24 | P2 | P6 | P8 |
0    7    13   19   24   30    36    42    48    54    60    66    72    78    84   88   92   95   98   102  106  110  114  117  120  123

Patient Scheduling Table:
PID	Priority	Arrival	Burst	Waiting	Turnaround	Completion
P5	24		4	7	0	7	11
...
Average Waiting Time: 50.64
Average Turnaround Time: 56.64

========== ROUND ROBIN SCHEDULING ==========

Gantt Chart:
| P1 | P2 | P3 | P4 | P5 | P1 | P3 | P5 | P7 | ...
0    3    6    9    12   15   18   21   24   ...

Patient Scheduling Table:
PID	Arrival	Burst	Waiting	Turnaround	Completion
P1	0	6	12	18	18
...
Average Waiting Time: 54.88
Average Turnaround Time: 60.88

========== BONUS FEATURES ==========

========== AGING MECHANISM ==========

P1 waited 10 units => Priority increased from 21 to 23
P2 waited 9 units => Priority increased from 12 to 14
...

========== DYNAMIC PATIENT ARRIVAL ==========
New patient arrived: P26
Name: EmergencyCase
Priority Score: 28

Queue After Dynamic Arrival and Re-Sorting:
========================================
PATIENT QUEUE
========================================
P26 | EmergencyCase | Priority: 28
P5 | Arjun | Priority: 24
...
========================================

========== PATIENT DETAIL VIEW ==========

Enter Patient ID to view full details.
Enter Q to exit.

1. P1 | Rahul | Priority: 21
2. P2 | Asha | Priority: 12
...

Patient ID: P1

Patient ID       : P1
Name             : Rahul
Arrival Time     : 0 minutes
Heart Rate       : 130
Blood Pressure   : 90
Oxygen Level     : 85
Severity         : 9
Burst Time       : 6 minutes
Priority Score   : 21
Waiting Time     : 0 minutes
Turnaround Time  : 6 minutes
Completion Time  : 6 minutes
```

---

## Sample Patients

The simulation includes 25 initial patients with varying severity levels:

| ID | Name | Arrival | Heart Rate | Blood Pressure | Oxygen Level | Severity | Burst Time | Priority |
|---|---|---|---|---|---|---|---|---|
| P1 | Rahul | 0 | 130 | 90 | 85 | 9 | 6 | 21 |
| P2 | Asha | 1 | 95 | 120 | 97 | 4 | 3 | 12 |
| P3 | Kiran | 2 | 125 | 95 | 88 | 8 | 5 | 20 |
| P5 | Arjun | 4 | 140 | 85 | 80 | 10 | 7 | 24 |
| P11 | Anil | 10 | 145 | 88 | 82 | 10 | 8 | 24 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |

Plus **1 dynamic patient** (P26) that arrives mid-simulation.

---

## Key Design Decisions

**Why Quick Sort?** Quick Sort provides optimal O(n log n) average-case performance with minimal space overhead, making it ideal for real-time triage environments where speed is critical. The mid-point pivot strategy ensures good distribution even with varied patient priorities.

**Why non-preemptive Priority Scheduling?** In a real ER, interrupting a doctor mid-procedure is harmful. Non-preemptive priority reflects actual clinical workflows where patient continuity is critical.

**Why Round Robin as well?** It models scenarios with multiple treatment stations sharing workload fairly, ensuring no single high-priority patient monopolizes resources indefinitely.

**Why aging?** Pure priority scheduling starves low-priority patients indefinitely. The aging boost (after 5 time units) ensures everyone eventually receives treatment, mirroring real-world triage policies that prevent indefinite waiting.

**Why patient detail view?** Interactive patient querying allows medical staff to quickly access complete vitals and scheduling information for any patient in the system, improving situational awareness during high-volume admissions.

---

## Module Documentation

### Patient Class (`DAA_MODULE/patient.py`)

Each patient is represented with:
- **Basic Details:** Patient ID, Name, Arrival Time
- **Medical Vitals:** Heart Rate, Blood Pressure, Oxygen Level
- **Severity:** Symptom severity score
- **Treatment Time:** Burst time (minutes to treat)
- **Priority:** Dynamically calculated based on vitals
- **`display()`** method for detailed patient information output
- **`calculate_priority()`** method for vitals-based scoring

### Sorting Module (`DAA_MODULE/sorting.py`)

- **`quick_sort(patients)`** — O(n log n) quicksort in descending priority order with arrival time tiebreaker
- **`_has_higher_triage_order(patient, other_patient)`** — Comparison function for sorting logic
- **`run_quick_sort(patients)`** — Runs Quick Sort with timing measurement and complexity display
- **`display_patients(patients)`** — Pretty-prints the patient queue

### Scheduling Module (`OS_MODULE/scheduling.py`)

- **`priority_scheduling(patients)`** — Non-preemptive scheduling by priority
  - Produces Gantt chart, waiting times, turnaround times, and averages
  - Respects patient arrival times
  
- **`round_robin(patients, time_quantum)`** — Preemptive scheduling with time quantum
  - Each patient gets up to 3 minutes per turn
  - Re-queues if burst time remains
  - Produces identical output format for easy comparison

### Aging Module (`OS_MODULE/aging.py`)

- **`apply_aging(patients, current_time, threshold=5, boost=2)`** — Anti-starvation mechanism
  - Scans patient queue at simulation time `current_time`
  - Any patient waiting ≥ `threshold` gets priority boost of `+boost`
  - Prevents indefinite starvation of low-severity patients

### Dynamic Arrival Module (`DAA_MODULE/dynamic_arrival.py`)

- **`add_dynamic_patient(patients)`** — Simulates an emergency patient arriving mid-simulation
  - Creates a new Patient object (P26 by default)
  - Calculates priority
  - Appends to queue
  - Triggers automatic re-sorting for updated treatment order

---

## Simulation Flow

```
main.py (Entry Point)
  ├─> Load sample patients from DAA_MODULE/sample_data.py
  ├─> Display original queue
  ├─> DAA Module: Quick Sort
  │   ├─> Sort by priority (descending), with arrival time tiebreaker
  │   └─> Display timing results
  ├─> Display sorted queue
  ├─> OS Module: Priority Scheduling
  │   ├─> Generate Gantt chart
  │   └─> Calculate average wait & turnaround time
  ├─> OS Module: Round Robin Scheduling
  │   ├─> Generate Gantt chart with time quantum
  │   └─> Calculate average wait & turnaround time
  ├─> Bonus Features Section:
  │   ├─> Apply Aging mechanism
  │   ├─> Add dynamic patient arrival
  │   ├─> Re-sort with updated priorities
  │   ├─> Display updated queue
  │   ├─> Final Priority Scheduling
  │   └─> Interactive Patient Detail View
  └─> Exit
```

---

## Authors

Built for **Hackathon PS-01** — LifeLine: Hospital Emergency Triage Engine
