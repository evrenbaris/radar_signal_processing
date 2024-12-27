# Simple Kalman Filter Implementation
def simple_kalman_filter(signal, process_variance=1e-5, measurement_variance=0.1**2):
    estimate = 0
    estimate_variance = 1.0
    estimates = []
    
    for measurement in signal:
        # Prediction step
        estimate_variance += process_variance
        
        # Update step
        kalman_gain = estimate_variance / (estimate_variance + measurement_variance)
        estimate = estimate + kalman_gain * (measurement - estimate)
        estimate_variance = (1 - kalman_gain) * estimate_variance
        
        estimates.append(estimate)
    
    return np.array(estimates)

# Apply the simple Kalman filter
filtered_signal = simple_kalman_filter(noisy_signal)

# Plot filtered signal
plt.figure(figsize=(10, 6))
plt.plot(time, noisy_signal, label="Noisy Signal", alpha=0.7)
plt.plot(time, filtered_signal, label="Filtered Signal (Simple Kalman)", color="red")
plt.title("Radar Signal After Simple Kalman Filtering")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()
plt.show()
