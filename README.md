# Report: Simulating Flight of a Boeing 727 Aeroplane

### Introduction

The purpose of this report is to describe and evaluate a Python code that simulates the flight of a Boeing 727 aeroplane. The code takes into account important physical factors that affect the flight of an aeroplane, such as air resistance and lift, and plots the resulting horizontal and vertical positions over time.

### Methodology

The simulation uses a loop to update the velocity and position of the aeroplane over small time intervals (dt) until the altitude of the aeroplane reaches zero (i.e., it lands). The simulation also limits the maximum velocity of the aeroplane to prevent it from exceeding v_max. The code uses the numpy and matplotlib libraries for numerical calculations and plotting, respectively.

### Results

The simulation provides a basic model of the flight of a Boeing 727 aeroplane, taking into account important physical factors such as air resistance, lift, and gravitational force. The plotted horizontal and vertical positions show the trajectory of the aeroplane as it takes off, reaches a maximum altitude, and lands. However, the simulation is simplistic and does not account for various other factors that can affect the flight of an aeroplane, such as turbulence, weather conditions, and engine performance. Therefore, the simulation should only be used for educational or illustrative purposes and not for actual flight simulations.

### Conclusion

In conclusion, the Python code for simulating the flight of a Boeing 727 aeroplane provides a useful tool for understanding the basic physics of flight and the factors that affect it. However, the simulation is limited in its scope and should not be relied upon for actual flight simulations. Further research and development are necessary to create more accurate and realistic simulations that take into account all the relevant factors affecting flight.

## Installation
#### 1.  Clone and Install
```bash
  # Clone the repo
  git clone https://github.com/GeniusPRO271/Flight-in-the-atmosphere
  
  # Navigate to clonned folder and Install dependencies
  pip install numpy 
  pip install matplotlib
  
  # Run it
  python3 main.py
  
```
