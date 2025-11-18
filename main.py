# Data analysis for stock prices - goal: learn the signs of a recession through stock patters
# Definitions: recession = 2 consecutive quarters of negative GDP growth
#              GDP = Gross Domestic Product
# Questions to explore:
# 1. How do stock prices behave before and during recessions? What are their patterns? 
# 2. How's recessions compared to stable economic periods?

# I'll be studying the patterns of the Great Recession (Dec 2007 - June 2009) and the 2001 Recession (Mar 2001 - Nov 2001)
# I'll not study the latest recession (the Covid-19 recession) since it was a unique recession (lasted only 2 months)
# I'll be using a period in the time of the Great Moderation (Aug 2004 - Dec 2006) as a stable economic period for comparison

import os
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

print('Data Analysis - Recession and Stocks Behavior')

# Load data from each recession period and the quarter before
INPUT_CSV = 'data_analysis/archive/stocks/COKE.csv' # path to CSV file 

# Date ranges
gr_start_date = dt.datetime(2007, 12, 1) # Great Recession
gr_end_date = dt.datetime(2009, 6, 30)

gr_before_start_date = dt.datetime(2007, 3, 1)
gr_before_end_date = dt.datetime(2007, 11, 30)

r2001_start_date = dt.datetime(2001, 3, 1)  # 2001 Recession
r2001_end_date = dt.datetime(2001, 11, 30)

r2001_before_start_date = dt.datetime(2000, 6, 1)
r2001_before_end_date = dt.datetime(2001, 2, 28)

gm_start_date = dt.datetime(2004, 5, 1) # Great Moderation
gm_end_date = dt.datetime(2006, 12, 31)

def load_data(csv_path=INPUT_CSV):
    if os.path.exists(csv_path):
        print('Loading CSV:', csv_path)
        df = pd.read_csv(csv_path, parse_dates=True)
        if 'Date' in df.columns:
            df['Date'] = pd.to_datetime(df['Date'])
            df = df.sort_values('Date').reset_index(drop=True)
            df.set_index('Date', inplace=True)
        return df
    else:
       print(f"No CSV found at {csv_path}.")

df = load_data()
print(df.shape)
print("Great Recession - Data Set") 
print(df[gr_start_date : gr_end_date])

# print("2001 Recession") 
# print(df[r2001_start_date : r2001_end_date])

def analyze_period(recession_title, df, start_date, end_date):
    data = df[start_date : end_date]
    data = data[data['Close'].notna()] # Filtering for valid Close values
    
    # Average High, Low, and Close Prices
    avg_close = data['Close'].mean()
    avg_high = data['High'].mean()
    avg_low = data['Low'].mean()
    trading_days = len(data)
    
    print(f"\n{recession_title} Analysis:")
    print(f"  Trading days: {trading_days}")
    print(f"  Avg Close: ${avg_close:.2f}")
    print(f"  Avg High: ${avg_high:.2f}")
    print(f"  Avg Low: ${avg_low:.2f}")

analyze_period("Great Recession - Before", df, gr_before_start_date, gr_before_end_date)
analyze_period("Great Recession", df, gr_start_date, gr_end_date)

analyze_period("2001 Recession - Before", df, r2001_before_start_date, r2001_before_end_date)
analyze_period("2001 Recession", df, r2001_start_date, r2001_end_date)

analyze_period("Great Moderation", df, gm_start_date, gm_end_date)

# Stretch Challenge: Data Visualization (focused on closing prices since they reflect overall stock performance)
def graphs(recession_title, df, start_date, end_date):
    data = df[start_date : end_date]
    series = data['Close']

    plt.figure(figsize=(10,5))
    plt.plot(series.index, series.values)
    plt.title(f" {recession_title} - Close Price")
    plt.xlabel("Date")
    plt.ylabel("Close $")
    plt.grid(True)
    plt.show()

graphs("Great Recession (Before)", df, gr_before_start_date, gr_before_end_date)
graphs("Great Recession", df, gr_start_date, gr_end_date)

graphs("2001 Recession (Before)", df, r2001_before_start_date, r2001_before_end_date)
graphs("2001 Recession", df, r2001_start_date, r2001_end_date)

graphs("Great Moderation", df, gm_start_date, gm_end_date)

# Future work/working ideas
# Making sure that all files are combined into one CSV for easier analysis across multiple stocks while keeping the integrity of each stock's data
import glob
# Combine all the CSV files
def combine_csv():
    path = "data_analysis/archive/stocks/*.csv"
    files = glob.glob(path)
    dfs = []
    for f in files:
        df = pd.read_csv(f)
        df['Symbol'] = os.path.basename(f)
        dfs.append(df)
    combined = pd.concat(dfs, ignore_index=True)
    combined.to_csv("all_stocks_data.csv", index=False)
    return combined
# combine_csv()