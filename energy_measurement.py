# energy_measurement.py
# Program to calculate electrical energy consumption

print("=== Electrical Energy Measurement ===")

# Input values
power = float(input("Enter power consumed (W): "))
time = float(input("Enter operating time (hours): "))

# Calculate energy
energy_wh = power * time
energy_kwh = energy_wh / 1000

# Display results
print("\n--- Energy Consumption ---")
print(f"Power              = {power:.2f} W")
print(f"Operating Time     = {time:.2f} hours")
print(f"Energy Consumed    = {energy_wh:.2f} Wh")
print(f"Energy Consumed    = {energy_kwh:.3f} kWh")
