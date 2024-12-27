import numpy as np
import matplotlib.pyplot as plt

# Constants
c = 3e8  # Speed of light (m/s)
frequency = 10e9  # Radar frequency (10 GHz)
pulse_duration = 1e-6  # Pulse duration (1 microsecond)

# Simulate a radar pulse
time = np.linspace(0, 5e-6, 1000)  # 5 microseconds
signal = np.sin(2 * np.pi * frequency * time)

# Add noise to the signal
noise = np.random.normal(0, 0.5, len(time))
noisy_signal = signal + noise

# Plot the radar pulse
plt.figure(figsize=(10, 6))
plt.plot(time, noisy_signal, label="Noisy Signal", alpha=0.7)
plt.plot(time, signal, label="Original Signal", linestyle="--", alpha=0.9)
plt.title("Radar Pulse with Noise")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()
plt.show()
