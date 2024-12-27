from scipy.fft import fft, fftfreq

# Perform FFT
n = len(noisy_signal)
fft_signal = fft(noisy_signal)
frequencies = fftfreq(n, d=(time[1] - time[0]))

# Plot FFT results
plt.figure(figsize=(10, 6))
plt.plot(frequencies[:n // 2], np.abs(fft_signal)[:n // 2])
plt.title("Frequency Spectrum of the Radar Signal")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()
