import quandl
import pandas as pd
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import numpy as np
import numpy
import math
from scipy.stats import scoreatpercentile
from scipy.stats.mstats import mode, gmean, hmean

#import the Shiller dataset, convert to csv, and read csv for analysis:
shiller = quandl.get("YALE/SPCOMP", authtoken="_uhAD1-g9JdY2teUwiAb", start_date="2000-01-31", end_date="2018-03-30")
shiller.to_csv('shiller.csv')
df2 = pd.read_csv('shiller.csv')

#Extract critical vectors for stock analysis:
x = df2['Year'].values
y = df2['Cyclically Adjusted PE Ratio'].values

#Now for some data visualization:
plt.plot(x, y, c = 'green')                                     # Plot
axes = plt.gca()                                                # Define axes
plt.ylim(8, 50)                                                 # Set y axis limits
plt.gcf().autofmt_xdate()                                       # beautify the x-labels

# Adjust axis scales
axes.set_yticks(axes.get_yticks()[::2])
axes.set_xticks(axes.get_xticks()[::15])

#Label graph, and show:
plt.title('CAPE: 2000 - 2018')
plt.show()

#Provide summary stats to benchmark index selection:
print("Summary Stats (CAPE)")
print("min", numpy.min(y))
print("max", numpy.max(y))
print("std", numpy.std(y))
print("mean", numpy.mean(y))
print("median", numpy.median(y))

#Show Histogram of CAPE for past 18 Years:
plt.hist(y, bins='auto', orientation='vertical')
plt.title('CAPE Histogram (2000 - 2018)')
plt.show()

#Onto to the Smart BETA selection process:

#import the stock dataset, convert to csv, and read csv for analysis:
stocks = quandl.get_table("ZACKS/CP", paginate=True)
stocks.to_csv('stocks.csv')
df1 = pd.read_csv('stocks.csv')

company = df1['ticker'].values
pe = df1['pe_ratio_12m'].values               #Focus on TTM P/E for robustness

#More data visualization:
plt.hist(pe, bins='auto', orientation='vertical')
plt.title('P/E Distribution (TTM) - Skewed')
plt.show()

#Derive summary data to compare against CAPE analysis:
print("Summary Stats (P/E)")
print("p/e median", numpy.median(pe))
print("p/e min", numpy.min(pe))
print("p/e max", numpy.max(pe))
print("p/e std", numpy.std(pe))
print("p/e mean", numpy.mean(pe))

#Define the "value" bands. Adjust st.dev. range in proportion to dateset size:
beta_band = int(1*numpy.std(pe) + numpy.mean(pe))
alpha_band = int(numpy.mean(pe) - 1*numpy.std(pe))

print("sell any stock with P/E above", beta_band)
print("buy any stock with P/E below", alpha_band)

min = int(numpy.min(pe))
max = int(numpy.max(pe))

#Finally select members for the long/short for the Smart BETA ETF/Index:
for pe in range(min, alpha_band):
    print("buy these", company)
for pe in range(beta_band, max):
    print("sell these", company)

#End
