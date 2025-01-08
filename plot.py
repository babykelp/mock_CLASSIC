import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt
from matplotlib import dates as mdates

def plot_the_temp (datasets, year, sl):
    
    # Define the 'sl' variable (soil layer index)
    var = 'tsl'

    # Function to load and process the data
    def load_and_process(file, sl, year):
        ds = file
        temp_layer = ds[var].isel(layer=sl)
        if var == 'tsl':
            temp_layer = temp_layer - 273.15
        return temp_layer
        

    # Plotting
    fig, ax = plt.subplots(figsize=(5,3))

    for dataset in datasets:
        temperature = load_and_process(dataset, sl, year)
        time_m = pd.date_range(start = f"{year}-01-01", end = f'{year}-12-31', freq = 'ME')
        if year == 2019:
            temp_v = temperature.values.flatten()[0:12]
        elif year == 2020:
            temp_v = temperature.values.flatten()[12:24]
        else: temp_v = temperature.values.flatten()[24:36]
        ax.plot(time_m, temp_v)

    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m'))
    ax.set_xticks(ax.get_xticks())

    plt.tight_layout()
    plt.rcParams['svg.fonttype'] = 'none'
    # plt.savefig('thaw.svg')

    plt.show()