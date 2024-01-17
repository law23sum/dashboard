import csv
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def get_data(path):
    """Extract dates and high temperatures."""
    lines = path.read_text().splitlines()
    reader = csv.reader(lines)
    header_row = next(reader)

    dates, highs = [], []
    for row in reader:
        try:
            high = int(row[2])
            highs.append(high)
            current_date = datetime.strptime(row[1], '%Y-%m-%d')
            dates.append(current_date)
        except ValueError:
            print(row)

    return dates, highs


def get_averages(temps, timespan):
    # Calc moving averages over the entire dataset.
    avgs = []
    for index in range(timespan, len(temps)):
        temps_slice = temps[index - timespan:index]
        mean = np.mean(temps_slice)
        avgs.append(mean)

    return avgs


def plot_data(dates, temps, title="",
              filename="output/high_temps.png"):
    """Plot daily temperature data."""
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots(figsize=(20, 6))

    ax.plot(dates, temps, color='red', alpha=0.6)

    # Format plot.
    ax.set_title(title, fontsize=24)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize=16)
    ax.tick_params(labelsize=16)

    plt.savefig(filename, bbox_inches="tight")


# Extract data.
path = Path('wx_data/sitka_highs_1944_2012.csv')
dates, highs = get_data(path)
print(f"\nFound {len(highs):,} data points.")

for num_years in [1, 3, 5, 10, 30]:
    # Analyze data.
    timespan = num_years * 365
    highs_array = np.array(highs)
    avgs = get_averages(highs_array, timespan=timespan)

    # Plot the data.
    if timespan <= 365:
        title = f"{timespan}-day Moving Average Temperature"
    else:
        title = f"{int(timespan / 365)}-year Moving Average Temperature"

    relevant_dates = dates[timespan:]
    filename = f"output/high_temps_{num_years}_year_moving_average.png"
    plot_data(relevant_dates, avgs, title, filename=filename)

    print(f"  Generated plot: {filename}")
