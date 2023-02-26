import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Constants for Boeing 727
g = 9.81  # m/s^2
rho = 1.2  # kg/m^3
Cd_baseball = 0.47
Cd_basketball = 0.44
Cd_football = 0.45
Cl_baseball = 0.18
Cl_basketball = 0.1
Cl_football = 0.13
A_baseball = 0.0034  # m^2
A_basketball = 0.0248  # m^2
A_football = 0.0387  # m^2
m_baseball = 0.145  # kg
m_basketball = 0.62  # kg
m_football = 0.425  # kg
v0_baseball = 44.7  # m/s
v0_basketball = 22.2  # m/s
v0_football = 24.6  # m/s
theta = np.pi / 4  # radians
#dt = 0.1  # s
#dt = 0.01  # s
dt = 0.001  # s
#dt = 0.0001  # s
t_max = 20  # s
v_max = 500

# Initialize variables
x_baseball = 0
y_baseball = 0
vx_baseball = v0_baseball * np.cos(theta)
vy_baseball = v0_baseball * np.sin(theta)

x_basketball = 0
y_basketball = 0
vx_basketball = v0_basketball * np.cos(theta)
vy_basketball = v0_basketball * np.sin(theta)

x_football = 0
y_football = 0
vx_football = v0_football * np.cos(theta)
vy_football = v0_football * np.sin(theta)

# Arrays to store data
ts = np.arange(0, t_max, dt)
xs_baseball = []
ys_baseball = []
vxs_baseball = []
vys_baseball = []

xs_basketball = []
ys_basketball = []
vxs_basketball = []
vys_basketball = []

xs_football = []
ys_football = []
vxs_football = []
vys_football = []

# Simulation loop
for i, t in enumerate(ts):

    # Check if altitude is below zero
    if y_baseball >= 0:
        # Calculate baseball forces
        F_gravity_baseball = m_baseball * g
        v_baseball = np.sqrt(vx_baseball**2 + vy_baseball**2)
        if v_baseball > v_max:
            v_baseball = v_max
        F_air_baseball = -0.5 * rho * v_baseball**2 * Cd_baseball * A_baseball
        F_lift_baseball = 0.5 * rho * v_baseball ** 2 * Cl_baseball * A_baseball
        F_net_baseball = F_lift_baseball + F_air_baseball - F_gravity_baseball
        a_baseball = F_net_baseball / m_baseball

        # Update velocity and position
        vx_baseball = vx_baseball + a_baseball * np.cos(theta) * dt
        vy_baseball = vy_baseball + a_baseball * np.sin(theta) * dt
        x_baseball = x_baseball + vx_baseball * dt
        y_baseball = y_baseball + vy_baseball * dt

        # Store data
        xs_baseball.append(x_baseball)
        ys_baseball.append(y_baseball)
        vxs_baseball.append(vx_baseball)
        vys_baseball.append(vy_baseball)
    # Check if altitude is below zero
    if y_basketball >= 0:
        # Calculate basketball forces
        F_gravity_basketball = m_basketball * g
        v_basketball = np.sqrt(vx_basketball ** 2 + vy_basketball ** 2)
        if v_basketball > v_max:
            v_basketball = v_max
        F_air_basketball = -0.5 * rho * v_basketball ** 2 * Cd_basketball * A_basketball
        F_lift_basketball = 0.5 * rho * v_basketball ** 2 * Cl_basketball * A_basketball
        F_net_basketball = F_lift_basketball + F_air_basketball - F_gravity_basketball
        a_basketball = F_net_basketball / m_basketball

        # Update velocity and position
        vx_basketball = vx_basketball + a_basketball * np.cos(theta) * dt
        vy_basketball = vy_basketball + a_basketball * np.sin(theta) * dt
        x_basketball = x_basketball + vx_basketball * dt
        y_basketball = y_basketball + vy_basketball * dt

        # Store data
        xs_basketball.append(x_basketball)
        ys_basketball.append(y_basketball)
        vxs_basketball.append(vx_basketball)
        vys_basketball.append(vy_basketball)
    # Check if altitude is below zero
    if y_football >= 0:
        # Calculate basketball forces
        F_gravity_football = m_football * g
        v_football = np.sqrt(vx_football ** 2 + vy_football ** 2)
        if v_football > v_max:
            v_football = v_max
        F_air_football = -0.5 * rho * v_football ** 2 * Cd_football * A_football
        F_lift_football = 0.5 * rho * v_football ** 2 * Cl_football * A_football
        F_net_football = F_lift_football + F_air_football - F_gravity_football
        a_football = F_net_football / m_football

        # Update velocity and position
        vx_football = vx_football + a_football * np.cos(theta) * dt
        vy_football = vy_football + a_football * np.sin(theta) * dt
        x_football = x_football + vx_football * dt
        y_football = y_football + vy_football * dt

        # Store data
        xs_football.append(x_football)
        ys_football.append(y_football)
        vxs_football.append(vx_football)
        vys_football.append(vy_football)

    if y_baseball < 0 and y_football < 0 and y_basketball < 0:
        break

# Convert to numpy arrays
xs_baseball = np.array(xs_baseball)
ys_baseball = np.array(ys_baseball)
vxs_baseball = np.array(vxs_baseball)
vys_baseball = np.array(vys_baseball)

xs_basketball = np.array(xs_basketball)
ys_basketball = np.array(ys_basketball)
vxs_basketball = np.array(vxs_basketball)
vys_basketball = np.array(vys_basketball)

xs_football = np.array(xs_football)
ys_football = np.array(ys_football)
vxs_football = np.array(vxs_football)
vys_football = np.array(vys_football)

# Plot data
fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(8, 10))
ax[0].plot(ts[:len(xs_basketball)], xs_basketball, label='Basketball')
ax[0].plot(ts[:len(xs_baseball)], xs_baseball, label='Baseball')
ax[0].plot(ts[:len(xs_football)], xs_football, label='Football')
ax[0].set_xlabel('Time (s)')
ax[0].set_ylabel('Height (m)')
ax[0].grid()
ax[0].legend()

ax[1].plot(ts[:len(ys_basketball)], ys_basketball, label="Basketball")
ax[1].plot(ts[:len(ys_baseball)], ys_baseball, label="Baseball")
ax[1].plot(ts[:len(ys_football)], ys_football, label="Football")
ax[1].set_xlabel('Time (s)')
ax[1].set_ylabel('Distance (m)')
ax[1].grid()
ax[1].legend()

# Create separate tables for each object
basketball_data = {
    'Time (s)': ts[:len(xs_basketball)],
    'Basketball Height (m)': xs_basketball,
    'Basketball Distance (m)': ys_basketball
}
baseball_data = {
    'Time (s)': ts[:len(xs_baseball)],
    'Baseball Height (m)': xs_baseball,
    'Baseball Distance (m)': ys_baseball
}
football_data = {
    'Time (s)': ts[:len(xs_football)],
    'Football Height (m)': xs_football,
    'Football Distance (m)': ys_football
}

# Create dataframes for each object
basketball_df = pd.DataFrame(basketball_data)
baseball_df = pd.DataFrame(baseball_data)
football_df = pd.DataFrame(football_data)

# Transpose the dataframes
basketball_df = basketball_df.transpose()
baseball_df = baseball_df.transpose()
football_df = football_df.transpose()

# Export to an Excel file with each dataframe in a separate sheet
with pd.ExcelWriter('sports_data.xlsx') as writer:
    basketball_df.to_excel(writer, sheet_name='Basketball')
    baseball_df.to_excel(writer, sheet_name='Baseball')
    football_df.to_excel(writer, sheet_name='Football')

plt.show()

