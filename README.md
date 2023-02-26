# Report: Flight in the atmosphere

### Introduction

Projectile flight is a type of motion in which an object is thrown or launched into the air and moves along a curved path under the influence of gravity. In this code, we are simulating the flight of three different types of balls: baseball, basketball, and football. We will investigate the trajectories of the balls and compare their behaviors.

### Methodology

The simulation was carried out using Python. The initial velocity and angle were set to be the same for all three objects. The constants and variables for each object were defined based on their physical properties. The simulation was run for a maximum time of 20 seconds with different time intervals (dt) of 0.1 s, 0.01 s, 0.001 s, and 0.0001 s to observe the effect of time intervals on the trajectory of the objects. The position and velocity of each object were stored in arrays, and the trajectory was plotted using matplotlib.

### Results

#### The trajectory of each object is plotted in the figure below for dt = 0.1 s.
![flight_sim_dt=0,1](https://user-images.githubusercontent.com/74122038/221430503-9037bfc6-85fa-49ca-aa15-37cf4a40b573.png)
#### The trajectory of each object is plotted in the figure below for dt = 0.01 s.
![flight_sim_dt=0,01](https://user-images.githubusercontent.com/74122038/221430514-d9caf3ea-e340-4a08-affa-d87c5c43348a.png)
#### The trajectory of each object is plotted in the figure below for dt = 0.001 s.
![flight_sim_d=0,001](https://user-images.githubusercontent.com/74122038/221430520-b8ed17f5-92ac-4d72-b835-dc177f8ca69a.png)
#### The trajectory of each object is plotted in the figure below for dt = 0.0001 s.
![flight_sim_0 0001](https://user-images.githubusercontent.com/74122038/221430524-3c50fa36-46eb-4b90-b4e4-8f138a9d501b.png)

From the figure, we can observe that the baseball has the highest peak and travels the farthest distance, followed by the football and then the basketball. This is because the baseball has the smallest cross-sectional area, and therefore experiences the least air resistance. The football has the largest cross-sectional area, resulting in the highest air resistance, and the basketball is between the baseball and football.

The effect of the time interval (dt) on the trajectory is also observed. As the time interval becomes smaller, the trajectory becomes more precise and closer to the actual trajectory. However, the simulation also takes longer to run as the time interval becomes smaller.


### Conclusion

In conclusion, the simulation of projectile motion of a baseball, basketball, and football shows that the physical properties of the objects, such as cross-sectional area, affect the trajectory of the object. The simulation also demonstrates that a smaller time interval results in a more precise trajectory, although it increases the computation time.

## Installation
#### 1.  Clone and Install
```bash
  # Clone the repo
  git clone https://github.com/GeniusPRO271/Flight-in-the-atmosphere
  
  # Navigate to clonned folder and Install dependencies
  pip install numpy 
  pip install pandas
  pip install matplotlib
  
  # Run it
  python3 main.py
  
```
