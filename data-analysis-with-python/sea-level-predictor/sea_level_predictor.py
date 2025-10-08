import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    result = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_range = range(df['Year'].min(), 2051, 1)
    y_range = [result.slope * yr + result.intercept for yr in x_range]
    plt.plot(x_range, y_range)

    # Create second line of best fit
    df_c = df[df['Year'] >= 2000]
    result = linregress(df_c['Year'], df_c['CSIRO Adjusted Sea Level'])
    x_range = range(df_c['Year'].min(), 2051, 1)
    y_range = [result.slope * yr + result.intercept for yr in x_range]
    plt.plot(x_range, y_range)

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()