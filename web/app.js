const TIME_UNIT = "minutes";

const patients = [
  ["P1", "Rahul", 0, 130, 90, 85, 9, 6],
  ["P2", "Asha", 1, 95, 120, 97, 4, 3],
  ["P3", "Kiran", 2, 125, 95, 88, 8, 5],
  ["P4", "Meena", 3, 110, 105, 92, 5, 4],
  ["P5", "Arjun", 4, 140, 85, 80, 10, 7],
  ["P6", "Sneha", 5, 100, 115, 95, 3, 2],
  ["P7", "Vikram", 6, 128, 98, 89, 7, 6],
  ["P8", "Divya", 7, 90, 110, 99, 2, 3],
  ["P9", "Rohan", 8, 135, 92, 84, 9, 5],
  ["P10", "Priya", 9, 118, 108, 93, 4, 4],
  ["P11", "Anil", 10, 145, 88, 82, 10, 8],
  ["P12", "Kavya", 11, 105, 112, 96, 5, 3],
  ["P13", "Suresh", 12, 122, 99, 87, 8, 6],
  ["P14", "Neha", 13, 98, 118, 98, 3, 2],
  ["P15", "Manoj", 14, 138, 91, 83, 9, 7],
  ["P16", "Ritika", 15, 150, 86, 81, 10, 8],
  ["P17", "Deepak", 16, 102, 109, 94, 5, 3],
  ["P18", "Nisha", 17, 127, 97, 88, 8, 5],
  ["P19", "Varun", 18, 132, 93, 85, 9, 6],
  ["P20", "Pooja", 19, 108, 114, 97, 4, 4],
  ["P21", "Ajay", 20, 142, 89, 82, 10, 7],
  ["P22", "Shreya", 21, 99, 117, 96, 3, 2],
  ["P23", "Harish", 22, 124, 96, 89, 7, 5],
  ["P24", "Lavanya", 23, 111, 103, 91, 6, 4],
  ["P25", "Tarun", 24, 136, 90, 84, 9, 6],
].map(([pid, name, arrivalTime, heartRate, bloodPressure, oxygenLevel, severity, burstTime]) => {
  const patient = {
    pid,
    name,
    arrivalTime,
    heartRate,
    bloodPressure,
    oxygenLevel,
    severity,
    burstTime,
  };
  patient.priority = calculatePriority(patient);
  return patient;
});

let quickSorted = [];
let insertionSorted = [];
let scheduledPatients = [];
let selectedPatientId = "P5";

function calculatePriority(patient) {
  let score = patient.severity;
  if (patient.oxygenLevel < 90) score += 5;
  if (patient.heartRate > 120) score += 3;
  if (patient.bloodPressure < 100) score += 2;
  return score;
}

function hasHigherTriageOrder(patient, otherPatient) {
  if (patient.priority !== otherPatient.priority) {
    return patient.priority > otherPatient.priority;
  }
  return patient.arrivalTime < otherPatient.arrivalTime;
}

function quickSort(patientList) {
  if (patientList.length <= 1) return [...patientList];

  const pivot = patientList[Math.floor(patientList.length / 2)];
  const higherPriority = [];
  const samePriority = [];
  const lowerPriority = [];

  patientList.forEach((patient) => {
    if (hasHigherTriageOrder(patient, pivot)) {
      higherPriority.push(patient);
    } else if (hasHigherTriageOrder(pivot, patient)) {
      lowerPriority.push(patient);
    } else {
      samePriority.push(patient);
    }
  });

  return [...quickSort(higherPriority), ...samePriority, ...quickSort(lowerPriority)];
}

function insertionSort(patientList) {
  const sortedPatients = [...patientList];

  for (let i = 1; i < sortedPatients.length; i += 1) {
    const currentPatient = sortedPatients[i];
    let j = i - 1;

    while (j >= 0 && hasHigherTriageOrder(currentPatient, sortedPatients[j])) {
      sortedPatients[j + 1] = sortedPatients[j];
      j -= 1;
    }

    sortedPatients[j + 1] = currentPatient;
  }

  return sortedPatients;
}

function calculateSchedule(patientList) {
  let currentTime = 0;

  return patientList.map((patient) => {
    const scheduled = { ...patient };

    if (currentTime < scheduled.arrivalTime) {
      currentTime = scheduled.arrivalTime;
    }

    const startTime = currentTime;
    const completionTime = startTime + scheduled.burstTime;

    scheduled.waitingTime = startTime - scheduled.arrivalTime;
    scheduled.turnaroundTime = completionTime - scheduled.arrivalTime;
    scheduled.completionTime = completionTime;

    currentTime = completionTime;
    return scheduled;
  });
}

function runAlgorithms() {
  const quickStart = performance.now();
  quickSorted = quickSort(patients);
  const quickTime = performance.now() - quickStart;

  const insertionStart = performance.now();
  insertionSorted = insertionSort(patients);
  const insertionTime = performance.now() - insertionStart;

  scheduledPatients = calculateSchedule(quickSorted);

  document.getElementById("quickTime").textContent = `${quickTime.toFixed(4)} ms`;
  document.getElementById("insertionTime").textContent = `${insertionTime.toFixed(4)} ms`;
}

function statusFor(patient) {
  if (patient.priority >= 18) return ["Critical", "status-critical"];
  if (patient.priority >= 7) return ["Urgent", "status-urgent"];
  return ["Stable", "status-stable"];
}

function renderPatientRows(targetId, patientList, includeVitals = false) {
  const target = document.getElementById(targetId);
  target.innerHTML = "";

  patientList.forEach((patient) => {
    const [statusText, statusClass] = statusFor(patient);
    const row = document.createElement("tr");
    row.dataset.pid = patient.pid;

    row.innerHTML = includeVitals
      ? `
        <td><span class="pid-pill">${patient.pid}</span></td>
        <td>${patient.name}</td>
        <td>${patient.priority}</td>
        <td>${patient.arrivalTime} ${TIME_UNIT}</td>
        <td>HR ${patient.heartRate} / O2 ${patient.oxygenLevel}%</td>
        <td><span class="status-pill ${statusClass}">${statusText}</span></td>
      `
      : `
        <td><span class="pid-pill">${patient.pid}</span></td>
        <td>${patient.name}</td>
        <td>${patient.priority}</td>
        <td>${patient.arrivalTime} ${TIME_UNIT}</td>
      `;

    row.addEventListener("click", () => showPatientDetails(patient.pid));
    target.appendChild(row);
  });
}

function renderScheduleRows() {
  const target = document.getElementById("scheduleRows");
  target.innerHTML = "";

  scheduledPatients.forEach((patient) => {
    const row = document.createElement("tr");
    row.dataset.pid = patient.pid;
    row.innerHTML = `
      <td><span class="pid-pill">${patient.pid}</span></td>
      <td>${patient.name}</td>
      <td>${patient.priority}</td>
      <td>${patient.arrivalTime}</td>
      <td>${patient.burstTime}</td>
      <td>${patient.waitingTime}</td>
      <td>${patient.turnaroundTime}</td>
      <td>${patient.completionTime}</td>
    `;
    row.addEventListener("click", () => showPatientDetails(patient.pid));
    target.appendChild(row);
  });
}

function renderTimeline() {
  const target = document.getElementById("scheduleTimeline");
  target.innerHTML = scheduledPatients
    .map((patient) => `
      <button class="timeline-item" type="button" data-pid="${patient.pid}">
        <strong>${patient.pid}</strong>
        <span>${patient.completionTime} min</span>
      </button>
    `)
    .join("");

  target.querySelectorAll(".timeline-item").forEach((item) => {
    item.addEventListener("click", () => showPatientDetails(item.dataset.pid));
  });
}

function renderMetrics() {
  const totalWaiting = scheduledPatients.reduce((sum, patient) => sum + patient.waitingTime, 0);
  const totalTurnaround = scheduledPatients.reduce((sum, patient) => sum + patient.turnaroundTime, 0);
  const highestPriority = Math.max(...patients.map((patient) => patient.priority));

  document.getElementById("totalPatients").textContent = patients.length;
  document.getElementById("highestPriority").textContent = highestPriority;
  document.getElementById("avgWaiting").textContent =
    `${(totalWaiting / scheduledPatients.length).toFixed(2)} min`;
  document.getElementById("avgTurnaround").textContent =
    `${(totalTurnaround / scheduledPatients.length).toFixed(2)} min`;
}

function normalizePatientId(value) {
  const patientId = value.trim().toUpperCase().replace(/\s/g, "");
  if (/^\d+$/.test(patientId)) return `P${patientId}`;
  return patientId;
}

function findPatient(patientId) {
  const normalizedId = normalizePatientId(patientId);
  return scheduledPatients.find((patient) => patient.pid === normalizedId);
}

function showPatientDetails(patientId) {
  const patient = findPatient(patientId);
  const card = document.getElementById("patientCard");
  const grid = document.getElementById("detailGrid");
  const hint = document.getElementById("detailHint");

  if (!patient) {
    selectedPatientId = "";
    card.innerHTML = `
      <div class="patient-avatar">ID</div>
      <h3>No patient found</h3>
      <p>Use a valid Patient ID such as P1, P5, or P25.</p>
    `;
    grid.innerHTML = "";
    hint.textContent = "No matching patient ID.";
    highlightSelectedPatient();
    switchTab("details");
    return;
  }

  selectedPatientId = patient.pid;
  const [statusText, statusClass] = statusFor(patient);
  card.innerHTML = `
    <div class="patient-avatar">${patient.pid.replace("P", "")}</div>
    <h3>${patient.name}</h3>
    <p>${patient.pid} <span class="status-pill ${statusClass}">${statusText}</span></p>
    <div class="vital-strip">
      <div class="vital-item"><span>Heart Rate</span><strong>${patient.heartRate}</strong></div>
      <div class="vital-item"><span>Blood Pressure</span><strong>${patient.bloodPressure}</strong></div>
      <div class="vital-item"><span>Oxygen Level</span><strong>${patient.oxygenLevel}%</strong></div>
      <div class="vital-item"><span>Severity</span><strong>${patient.severity}</strong></div>
    </div>
  `;

  const details = [
    ["Priority Score", patient.priority],
    ["Arrival Time", `${patient.arrivalTime} ${TIME_UNIT}`],
    ["Burst Time", `${patient.burstTime} ${TIME_UNIT}`],
    ["Waiting Time", `${patient.waitingTime} ${TIME_UNIT}`],
    ["Turnaround Time", `${patient.turnaroundTime} ${TIME_UNIT}`],
    ["Completion Time", `${patient.completionTime} ${TIME_UNIT}`],
  ];

  grid.innerHTML = details
    .map(([label, value]) => `
      <div class="detail-item">
        <span>${label}</span>
        <strong>${value}</strong>
      </div>
    `)
    .join("");

  document.getElementById("patientSearch").value = patient.pid;
  hint.textContent = "Complete scheduling details for the selected patient.";
  highlightSelectedPatient();
  switchTab("details");
}

function highlightSelectedPatient() {
  document.querySelectorAll("[data-pid]").forEach((element) => {
    element.classList.toggle("selected", element.dataset.pid === selectedPatientId);
  });
}

function switchTab(tabId) {
  document.querySelectorAll(".tab-panel").forEach((panel) => {
    panel.classList.toggle("active", panel.id === tabId);
  });

  document.querySelectorAll(".nav-tab").forEach((tab) => {
    tab.classList.toggle("active", tab.dataset.tab === tabId);
  });
}

function bindEvents() {
  document.querySelectorAll(".nav-tab").forEach((tab) => {
    tab.addEventListener("click", () => switchTab(tab.dataset.tab));
  });

  document.getElementById("searchButton").addEventListener("click", () => {
    showPatientDetails(document.getElementById("patientSearch").value);
  });

  document.getElementById("patientSearch").addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
      showPatientDetails(event.target.value);
    }
  });
}

function render() {
  runAlgorithms();
  renderMetrics();
  renderPatientRows("overviewRows", scheduledPatients, true);
  renderPatientRows("quickRows", quickSorted);
  renderPatientRows("insertionRows", insertionSorted);
  renderScheduleRows();
  renderTimeline();
  showPatientDetails("P5");
  switchTab("overview");
}

bindEvents();
render();
