import matplotlib.pyplot as plt
from matplotlib.dates import date2num
from datetime import datetime
# Jeg har fått hjelp av KI til og lage skriptet 
# Define tasks and their start and end dates
tasks = [
    ("Forprosjektrapport", datetime(2025, 1, 27), datetime(2025, 3, 2)),
    ("Diskuter prosjektplan", datetime(2025, 1, 27), datetime(2025, 3, 2)),
    ("Identifiser utfordringer", datetime(2025, 3, 3), datetime(2025, 4, 13)),
    ("Design løsning", datetime(2025, 3, 3), datetime(2025, 4, 13)),
    ("Start implementering", datetime(2025, 3, 3), datetime(2025, 4, 13)),
    ("Evaluer fremdrift", datetime(2025, 4, 14), datetime(2025, 4, 20)),
    ("Testing og dokumentasjon", datetime(2025, 4, 21), datetime(2025, 5, 18)),
    ("Fullfør løsning", datetime(2025, 4, 21), datetime(2025, 5, 18)),
    ("Testing i simulert nettverk", datetime(2025, 4, 21), datetime(2025, 5, 18)),
    ("Dokumenter resultater", datetime(2025, 4, 21), datetime(2025, 5, 18)),
    ("Lever prosjektrapport", datetime(2025, 5, 19), datetime(2025, 5, 19))
]

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Create the Gantt chart
for i, (task, start, end) in enumerate(tasks):
    ax.barh(i, (date2num(end) - date2num(start)), left=date2num(start), height=0.5, align='center', color="skyblue")

# Add task names to the chart
ax.set_yticks(range(len(tasks)))
ax.set_yticklabels([task[0] for task in tasks])

# Format the x-axis with dates
ax.xaxis_date()
fig.autofmt_xdate()

# Labels and title
ax.set_xlabel("Dato")
ax.set_ylabel("Oppgaver")
ax.set_title("Gantt-diagram for OPC UA-prosjekt")

# Display the chart
plt.tight_layout()
plt.show()
