import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ---- USER INPUT ----
speed = float(input("Enter speed (e.g., 1.0): "))
amplitude = float(input("Enter vertical amplitude (e.g., 2.0): "))
radius = float(input("Enter circle radius (e.g., 0.5): "))

# ---- SETUP ----
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

circle = plt.Circle((0, 5), radius, color='blue')
ax.add_patch(circle)

# ---- ANIMATION ----
def update(frame):
    x = frame * speed
    y = 5 + amplitude * np.sin(frame)
    circle.center = (x % 10, y)  # wrap around screen
    return circle,

ani = FuncAnimation(
    fig,
    update,
    frames=np.linspace(0, 10, 100),
    interval=50,
    blit=True
)

plt.show()