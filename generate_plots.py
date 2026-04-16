"""
Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations.
"""
import numpy as np
import matplotlib.pyplot as plt


def generate_data(seed):
    """
    Generate synthetic temperature sensor readings.

    Parameters
    ----------
    seed : int
        Random seed for reproducibility.

    Returns
    -------
    sensor_a : numpy.ndarray
    sensor_b : numpy.ndarray
    timestamps : numpy.ndarray
    """

    rng = np.random.default_rng(seed)

    sensor_a = rng.normal(loc=25.0, scale=3.0, size=200)
    sensor_b = rng.normal(loc=27.0, scale=4.5, size=200)
    timestamps = rng.uniform(low=0.0, high=10.0, size=200)

    return sensor_a, sensor_b, timestamps


def plot_scatter(sensor_a, sensor_b, timestamps):
    """
    Create scatter plot of sensor readings.
    """

    plt.figure(figsize=(8, 5))
    plt.scatter(timestamps, sensor_a, label="Sensor A")
    plt.scatter(timestamps, sensor_b, label="Sensor B")

    plt.xlabel("Time (s)")
    plt.ylabel("Temperature (°C)")
    plt.title("Sensor Readings vs Time")
    plt.legend()


def plot_histogram(sensor_a, sensor_b):
    """
    Create histogram of sensor distributions.
    """

    plt.figure(figsize=(8, 5))
    plt.hist(sensor_a, bins=30, alpha=0.5, label="Sensor A")
    plt.hist(sensor_b, bins=30, alpha=0.5, label="Sensor B")

    plt.xlabel("Temperature (°C)")
    plt.ylabel("Frequency")
    plt.title("Distribution of Sensor Readings")
    plt.legend()


def plot_box(sensor_a, sensor_b):
    """
    Create box plot comparing sensors.
    """

    plt.figure(figsize=(8, 5))
    plt.boxplot([sensor_a, sensor_b], tick_labels=["Sensor A", "Sensor B"])

    plt.ylabel("Temperature (°C)")
    plt.title("Comparison of Sensor Distributions")


def main():
    seed = 5678  # replace with your last 4 digits if needed

    sensor_a, sensor_b, timestamps = generate_data(seed)

    plot_scatter(sensor_a, sensor_b, timestamps)
    plot_histogram(sensor_a, sensor_b)
    plot_box(sensor_a, sensor_b)

    plt.savefig("sensor_analysis.png")
    plt.show()


if __name__ == "__main__":
    main()