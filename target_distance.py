# Calculate target distances
distances = [(c * pulse_duration) / 2]  # Example for one target

# Display target distances
for i, d in enumerate(distances):
    print(f"Target {i + 1}: Distance = {d:.2f} meters")
