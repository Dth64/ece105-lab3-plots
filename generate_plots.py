"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""
import numpy as np
import matplotlib.pyplot as plt


def generate_data(seed):
    """Generate synthetic temperature sensor readings.

    Parameters
    ----------
    seed : int
        Random number generator seed for reproducibility.

    Returns
    -------
    sensor_a : numpy.ndarray
        Temperature readings from sensor A in Celsius, shape (200,).
    sensor_b : numpy.ndarray
        Temperature readings from sensor B in Celsius, shape (200,).
    timestamps : numpy.ndarray
        Measurement timestamps in seconds, shape (200,).
    """
    rng = np.random.default_rng(seed)
    sensor_a = rng.normal(loc=25.0, scale=3.0, size=200)
    sensor_b = rng.normal(loc=27.0, scale=4.5, size=200)
    timestamps = rng.uniform(low=0.0, high=10.0, size=200)
    return sensor_a, sensor_b, timestamps


def plot_scatter(sensor_a, sensor_b, timestamps, ax):
    """Create scatter plot of sensor readings vs time.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Temperature readings from sensor A in Celsius, shape (200,).
    sensor_b : numpy.ndarray
        Temperature readings from sensor B in Celsius, shape (200,).
    timestamps : numpy.ndarray
        Measurement timestamps in seconds, shape (200,).
    ax : matplotlib.axes.Axes
        Axes object to draw the scatter plot on.

    Returns
    -------
    None
    """
    ax.scatter(timestamps, sensor_a, label="Sensor A", color="blue")
    ax.scatter(timestamps, sensor_b, label="Sensor B", color="orange")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Temperature (deg C)")
    ax.set_title("Sensor Readings vs Time")
    ax.legend()


def plot_histogram(sensor_a, sensor_b, ax):
    """Create overlaid histogram of sensor temperature distributions.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Temperature readings from sensor A in Celsius, shape (200,).
    sensor_b : numpy.ndarray
        Temperature readings from sensor B in Celsius, shape (200,).
    ax : matplotlib.axes.Axes
        Axes object to draw the histogram on.

    Returns
    -------
    None
    """
    ax.hist(sensor_a, bins=30, alpha=0.5, label="Sensor A")
    ax.hist(sensor_b, bins=30, alpha=0.5, label="Sensor B")
    ax.axvline(sensor_a.mean(), color="blue", linestyle="--")
    ax.axvline(sensor_b.mean(), color="orange", linestyle="--")
    ax.set_xlabel("Temperature (deg C)")
    ax.set_ylabel("Frequency")
    ax.set_title("Distribution of Sensor Readings")
    ax.legend()


def plot_boxplot(sensor_a, sensor_b, ax):
    """Create side-by-side box plot comparing sensor distributions.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Temperature readings from sensor A in Celsius, shape (200,).
    sensor_b : numpy.ndarray
        Temperature readings from sensor B in Celsius, shape (200,).
    ax : matplotlib.axes.Axes
        Axes object to draw the box plot on.

    Returns
    -------
    None
    """
    ax.boxplot([sensor_a, sensor_b], tick_labels=["Sensor A", "Sensor B"])
    overall_mean = np.concatenate([sensor_a, sensor_b]).mean()
    ax.axhline(overall_mean, color="red", linestyle="--", label="Overall mean")
    ax.set_ylabel("Temperature (deg C)")
    ax.set_title("Comparison of Sensor Distributions")
    ax.legend()


def main():
    """Generate sensor data, create plots, and save as sensor_analysis.png.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    seed = 5678

    # generate synthetic sensor data
    sensor_a, sensor_b, timestamps = generate_data(seed)

    # create a 2x2 subplot figure
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # draw each plot on its own axes
    plot_scatter(sensor_a, sensor_b, timestamps, axes[0, 0])
    plot_histogram(sensor_a, sensor_b, axes[0, 1])
    plot_boxplot(sensor_a, sensor_b, axes[1, 0])

    # hide the unused fourth subplot
    axes[1, 1].set_visible(False)

    plt.tight_layout()
    plt.savefig("sensor_analysis.png", dpi=150, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    main()
