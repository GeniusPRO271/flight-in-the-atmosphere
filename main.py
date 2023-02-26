import numpy as np
import matplotlib.pyplot as plt

# Constants for Boeing 727
g = 9.81  # m/s^2
rho = 0.4135  # kg/m^3
Cd = 0.034  # Drag coefficient
Cl = 0.45  # Lift coefficient
A = 153  # m^2
m = 72700  # kg
x0 = 0  # m
y0 = 0  # m
v0 = 210  # m/s
theta = np.pi / 4  # radians
dt = 0.1  # s
t_max = 3600  # s
v_max = 300  # m/s

# Initialize variables
x = x0
y = y0
vx = v0 * np.cos(theta)
vy = v0 * np.sin(theta)

# Arrays to store data
ts = np.arange(0, t_max, dt)
xs = []
ys = []
vxs = []
vys = []

# Simulation loop
for i, t in enumerate(ts):
    # Calculate forces
    F_gravity = m * g
    v = np.sqrt(vx**2 + vy**2)
    if v > v_max:
        v = v_max
    F_air = -0.5 * rho * v**2 * Cd * A
    F_lift = 0.5 * rho * v**2 * Cl * A
    F_net = F_lift + F_air - F_gravity
    a = F_net / m

    # Update velocity and position
    vx = vx + a * np.cos(theta) * dt
    vy = vy + a * np.sin(theta) * dt
    x = x + vx * dt
    y = y + vy * dt

    # Store data
    xs.append(x)
    ys.append(y)
    vxs.append(vx)
    vys.append(vy)

    # Check if altitude is below zero
    if y < 0:
        break

# Convert to numpy arrays
xs = np.array(xs)
ys = np.array(ys)
vxs = np.array(vxs)
vys = np.array(vys)

# Plot data
fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(8, 10))
ax[0].plot(ts[:len(xs)], xs)
ax[0].set_xlabel('Time (s)')
ax[0].set_ylabel('Horizontal position (m)')
ax[0].grid()

ax[1].plot(ts[:len(ys)], ys)
ax[1].set_xlabel('Time (s)')
ax[1].set_ylabel('Vertical position (m)')
ax[1].grid()

plt.show()
