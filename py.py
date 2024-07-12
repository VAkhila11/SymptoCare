import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Initialize plot
fig, ax = plt.subplots(figsize=(18, 15))

# Function to create labeled boxes
def create_box(ax, text, xy, width=3, height=1.5, box_color="lightblue"):
    box = patches.FancyBboxPatch(xy, width, height, boxstyle="round,pad=0.3", linewidth=1, edgecolor='black', facecolor=box_color)
    ax.add_patch(box)
    ax.text(xy[0] + width / 2, xy[1] + height / 2, text, ha='center', va='center', fontsize=10)

# Define box positions for flowchart
positions_flowchart = {
    "Client Layer": (0, 14),
    "Web Application": (1, 12),
    "Mobile Application": (1, 10),
    "API Gateway": (5, 11),
    "Application Layer": (8, 11),
    "Auth & Auth Service": (8, 9),
    "Patient Management Service": (8, 7),
    "Doctor Management Service": (8, 5),
    "Appointment Scheduling Service": (8, 3),
    "Symptom Checker Service": (8, 1),
    "Notification Service": (8, -1),
    "Reporting and Analytics Service": (8, -3),
    "Integration Service": (8, -5),
    "Data Layer": (11, 11),
    "Database": (11, 9),
    "Data Warehouse": (11, 7),
    "Cache": (11, 5),
    "Blob Storage": (11, 3),
    "Infrastructure Layer": (14, 11),
    "Servers": (14, 9),
    "Load Balancer": (14, 7),
    "CI/CD Pipeline": (14, 5),
    "Monitoring and Logging": (14, 3)
}

# Create all boxes
for text, pos in positions_flowchart.items():
    create_box(ax, text, pos)

# Add arrows to indicate data flow
arrows_flowchart = [
    ((2, 14), (2, 12.75)), ((2, 12.75), (2, 12)), # Client to Web
    ((2, 12), (2, 10.75)), ((2, 10.75), (2, 10)), # Web to Mobile
    ((2, 11), (5, 11)), # Mobile to API Gateway
    ((6.5, 11), (8, 11)), # API Gateway to Application Layer
    ((9.5, 11), (11, 11)), ((11, 11), (12.5, 11)), # Application Layer to Data Layer
    ((12.5, 11), (14, 11)), # Data Layer to Infrastructure Layer
    ((11.5, 9), (13, 9)), # Data Layer to Database
    ((11.5, 7), (13, 7)), # Data Layer to Data Warehouse
    ((11.5, 5), (13, 5)), # Data Layer to Cache
    ((11.5, 3), (13, 3)), # Data Layer to Blob Storage
    ((15, 11), (15, 9.75)), ((15, 9.75), (15, 9)), # Infrastructure to Servers
    ((15, 9), (15, 7.75)), ((15, 7.75), (15, 7)), # Infrastructure to Load Balancer
    ((15, 7), (15, 5.75)), ((15, 5.75), (15, 5)), # Infrastructure to CI/CD
    ((15, 5), (15, 3.75)), ((15, 3.75), (15, 3)), # Infrastructure to Monitoring
    ((9.5, 9), (8, 9)), # Application Layer to Auth
    ((9.5, 7), (8, 7)), # Application Layer to Patient Management
    ((9.5, 5), (8, 5)), # Application Layer to Doctor Management
    ((9.5, 3), (8, 3)), # Application Layer to Appointment Scheduling
    ((9.5, 1), (8, 1)), # Application Layer to Symptom Checker
    ((9.5, -1), (8, -1)), # Application Layer to Notification
    ((9.5, -3), (8, -3)), # Application Layer to Reporting
    ((9.5, -5), (8, -5)), # Application Layer to Integration
]

# Draw all arrows
for arrow in arrows_flowchart:
    ax.annotate('', xy=arrow[1], xytext=arrow[0], arrowprops=dict(arrowstyle="->", color='black'))

# Set plot limits and hide axes
ax.set_xlim(-1, 17)
ax.set_ylim(-7, 16)
ax.axis('off')

# Show plot
plt.title("Flowchart of Symtocare Internal Architecture", fontsize=16)
plt.show()
