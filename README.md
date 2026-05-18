# LifeLine — Hospital Emergency Triage Engine

> **Hackathon PS-01** | Domain: Healthcare | Difficulty: Beginner–Intermediate  
> DAA: Sorting & Efficiency Analysis | OS: Process Scheduling

---

## Problem Statement

City General Hospital's ER receives dozens of patients simultaneously during peak hours. Manual triage by nurses is slow and error-prone, costing critical minutes. **LifeLine** is an automated triage engine that scores patients based on vitals, sorts them using efficient algorithms, and simulates doctor allocation using CPU scheduling strategies — showing at every step who is being treated, who is waiting, and estimated wait times.

---

## Concepts Implemented

### DAA — Design & Analysis of Algorithms
| Algorithm | Time Complexity | Space Complexity | Used When |
|---|---|---|---|
| Selection Sort | O(n²) | O(1) | Small batches (≤ 10 patients) |
| Merge Sort | O(n log n) | O(n) | Large queues (> 10 patients) |

- Both algorithms run on the same input and produce a side-by-side performance comparison (actual comparisons made, time in µs, theoretical vs actual)
- A **smart dispatcher** automatically picks the right algorithm based on queue size

### OS — Operating Systems
| Scheduler | Type | Analogy |
|---|---|---|
| Priority Scheduling | Non-preemptive | Highest priority patient treated first to completion |
| Round Robin | Preemptive | Each patient gets a fixed time quantum (8 min), then re-queued |

- Each patient is modelled as a **process** with burst time (treatment duration) and arrival time
- Both schedulers produce a **Gantt chart**, per-patient **waiting time**, **turnaround time**, and averages

### Bonus Features
- **Aging mechanism** — patients waiting beyond a threshold (10 min) automatically receive a priority score bump (+15), preventing starvation of low-priority patients
- **Dynamic arrivals** — new patients arrive mid-simulation; the queue instantly re-sorts and the new order is displayed

---

## Priority Scoring

Each patient is scored automatically from their vitals and reported symptoms:

| Vital | Condition | Score Added |
|---|---|---|
| Heart Rate | < 40 or > 160 bpm | +45 |
| Heart Rate | < 60 or > 120 bpm | +15 |
| SpO2 | < 85% | +60 |
| SpO2 | 85–89% | +45 |
| SpO2 | 90–93% | +25 |
| Systolic BP | < 70 or > 200 mmHg | +50 |
| Systolic BP | < 90 or > 160 mmHg | +20 |
| Age | ≥ 70 years | +10 |
| Symptoms | cardiac arrest, stroke, unconscious… | +5 to +100 |

**Severity tiers:** CRITICAL (≥ 150) → SERIOUS (≥ 100) → MODERATE (≥ 60) → MINOR

---

## Project Structure

```
lifeline/
└── lifeline.py      ← single file, fully self-contained
```

All logic — patient model, triage scoring, sorting algorithms, scheduling, aging, dynamic arrivals, and output formatting — lives in one file for easy review and demo.

---

## How to Run

**Requirements:** Python 3.8+ (no external libraries needed)

```bash
python lifeline.py
```

That's it. The full simulation runs and prints to console.

---

## Sample Output

```
████████████████████████████████████████████████████████████
  LIFELINE — HOSPITAL EMERGENCY TRIAGE ENGINE
  DAA: Selection Sort + Merge Sort
  OS : Priority Scheduling + Round Robin
████████████████████████████████████████████████████████████

  15 patients loaded. Raw arrival order:
──────────────────────────────────────────────────────────────
  [P01] Ravi Kumar      HR= 38 BP= 65 SpO2=81%  score=345.0
  [P02] Meena Sharma    HR=158 BP=195 SpO2=87%  score=255.0
  ...

══════════════════════════════════════════════════════════════
  DAA — SORTING ALGORITHM COMPARISON
══════════════════════════════════════════════════════════════
  Metric                       Selection Sort     Merge Sort
──────────────────────────────────────────────────────────────
  Time Complexity                       O(n²)     O(n log n)
  Space Complexity                       O(1)           O(n)
  Theoretical comparisons                 105             59
  Actual comparisons                      105             28
  Time taken (µs)                       358.0         1161.1

  SORTED TRIAGE QUEUE:
  1   P01  Ravi Kumar      345.0   CRITICAL  cardiac arrest, unconscious
  2   P02  Meena Sharma    255.0   CRITICAL  stroke, severe bleeding
  ...

══════════════════════════════════════════════════════════════
  OS — PRIORITY SCHEDULING  (with Aging + Dynamic Arrivals)
══════════════════════════════════════════════════════════════

  ▶ t=  0– 30 | [P01] Ravi Kumar    score=345.0  wait=0min  TAT=30min

  🚨 LATE ARRIVAL at t=30: [P16] Nalini Srinivas  score=230.0
     Queue re-sorted. New front: [P02] Meena Sharma

  ⏫ AGING  [P13] Anand K. waited 20min → score bumped to 40.0
  ...

  GANTT CHART:
  |   P01   |   P02   |   P16   |   P03   | ...
   0         30        58        83        108 ...

  STATS — PRIORITY SCHEDULING
  Patient                  Wait   Turnaround
────────────────────────────────────────────
  Ravi Kumar                 0m         30m
  Meena Sharma              28m         56m
  ...
  AVERAGE                168.4m      185.7m
```

---

## Sample Patients

The simulation includes 15 initial patients covering all severity tiers, plus 2 late-arriving patients who inject mid-simulation:

| ID | Name | Severity | Key Vitals | Arrives |
|---|---|---|---|---|
| P01 | Ravi Kumar | CRITICAL | HR=38, SpO2=81%, BP=65 | t=0 |
| P02 | Meena Sharma | CRITICAL | HR=158, SpO2=87%, BP=195 | t=2 |
| P03 | Arjun Patel | CRITICAL | HR=145, SpO2=86% | t=3 |
| P07 | Deepak Menon | CRITICAL | HR=42, unconscious | t=6 |
| P06 | Kavitha Nair | CRITICAL | SpO2=92%, elderly | t=5 |
| P05 | Vikram Singh | SERIOUS | HR=130, chest pain | t=4 |
| P09 | Suresh Rao | SERIOUS | BP=150, high fever | t=7 |
| P08 | Anjali Iyer | MODERATE | fracture | t=5 |
| P15 | Harish V. | MINOR | mild fever | t=13 |
| P16 *(late)* | Nalini Srinivas | CRITICAL | stroke | **t=15** |
| P17 *(late)* | Revathi Sharma | CRITICAL | cardiac arrest | **t=22** |

---

## Key Design Decisions

**Why Selection Sort for small batches?** When n ≤ 10, the overhead of recursive calls in Merge Sort outweighs its theoretical advantage. Selection Sort's simplicity and O(1) space make it faster in practice for small emergency batches.

**Why non-preemptive Priority Scheduling?** In a real ER, interrupting a doctor mid-procedure to switch patients causes more harm than good. Non-preemptive priority reflects real clinical workflow.

**Why Round Robin as a complement?** RR models a scenario with multiple doctors (CPUs) sharing load fairly, ensuring no single patient monopolises all medical attention indefinitely.

**Why aging?** Pure priority scheduling starves low-priority patients indefinitely. The aging bump ensures everyone eventually gets treated, mirroring real-world triage policy where wait time itself becomes a clinical factor.

---

## Authors

Built for Hackathon PS-01 — LifeLine: Hospital Emergency Triage Engine
