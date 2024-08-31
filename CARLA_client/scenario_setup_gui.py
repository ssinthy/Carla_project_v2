import tkinter as tk
from tkinter import ttk

# Initialize the main window
root = tk.Tk()
root.title("ScenarioInfoManager")
root.geometry("600x500")  # Set the window size

# Function to handle the Start Simulation button click
def start_simulation():
    print("Simulation Started")

# Function to handle the Set Up Scenario button click
def setup_scenario():
    print("Scenario Set Up")

# Define the options for each combobox
road_type_options = ["Motorway", "Expressway"]
ego_vehicle_position_options = ["Traffic Lane", "Approaching Intersection", "Approaching T-Junction"]
emv_position_options = ["Same Road", "Parallel Road", "Opposite Road", "Cross Road"]
emv_direction_options = ["Approaches from Behind", "As Lead Vehicle", "Approaches from Right Lane", "Approaches from Left Lane", "Approaches on Opposite Lane", 
                         "Approaches Intersection", "Approaches T-Junction"]
weather_options = ["Clear", "Cloudy", "Light Rain", "Moderate Rain", "Heavy Rain"]
time_of_day_options = ["Day time", "Night time"]

# Define a larger font
large_font = ("Helvetica", 14)

# Create and place the widgets
ttk.Label(root, text="Road Type", font=large_font).grid(row=0, column=0, padx=20, pady=10, sticky=tk.W)
road_type_cb = ttk.Combobox(root, values=road_type_options, state="readonly", font=large_font)
road_type_cb.set("Motorway")
road_type_cb.grid(row=0, column=1, padx=20, pady=10)

ttk.Label(root, text="Ego Vehicle Position", font=large_font).grid(row=1, column=0, padx=20, pady=10, sticky=tk.W)
ego_vehicle_position_cb = ttk.Combobox(root, values=ego_vehicle_position_options, state="readonly", font=large_font)
ego_vehicle_position_cb.set("Traffic Lane")
ego_vehicle_position_cb.grid(row=1, column=1, padx=20, pady=10)

ttk.Label(root, text="Emergency Vehicle Position", font=large_font).grid(row=2, column=0, padx=20, pady=10, sticky=tk.W)
emv_position_cb = ttk.Combobox(root, values=emv_position_options, state="readonly", font=large_font)
emv_position_cb.set("Same Road")
emv_position_cb.grid(row=2, column=1, padx=20, pady=10)

ttk.Label(root, text="EMV Travel Direction", font=large_font).grid(row=3, column=0, padx=20, pady=10, sticky=tk.W)
emv_direction_cb = ttk.Combobox(root, values=emv_direction_options, state="readonly", font=large_font)
emv_direction_cb.set("Approaches from Behind")
emv_direction_cb.grid(row=3, column=1, padx=20, pady=10)

ttk.Label(root, text="Weather Condition", font=large_font).grid(row=4, column=0, padx=20, pady=10, sticky=tk.W)
weather_cb = ttk.Combobox(root, values=weather_options, state="readonly", font=large_font)
weather_cb.set("Clear")
weather_cb.grid(row=4, column=1, padx=20, pady=10)

ttk.Label(root, text="Time of Day", font=large_font).grid(row=5, column=0, padx=20, pady=10, sticky=tk.W)
time_of_day_cb = ttk.Combobox(root, values=time_of_day_options, state="readonly", font=large_font)
time_of_day_cb.set("Day time")
time_of_day_cb.grid(row=5, column=1, padx=20, pady=10)

ttk.Label(root, text="Safety Distance (m)", font=large_font).grid(row=6, column=0, padx=20, pady=10, sticky=tk.W)
safety_distance_sb = tk.Spinbox(root, from_=0, to=100, increment=1, font=large_font)
safety_distance_sb.grid(row=6, column=1, padx=20, pady=10)

start_button = ttk.Button(root, text="Start Simulation", command=start_simulation, style='TButton')
start_button.grid(row=7, column=0, columnspan=2, pady=20, ipadx=10, ipady=5)

setup_button = ttk.Button(root, text="Set Up Scenario", command=setup_scenario, style='TButton')
setup_button.grid(row=8, column=0, columnspan=2, pady=10, ipadx=10, ipady=5)

# Start the main event loop
root.mainloop()
