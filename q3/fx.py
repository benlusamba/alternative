# Importing Quandl data for analysis (using Pandas)

import quandl
import pandas as pd
import matplotlib.pyplot as plt
import csv
import random
import numpy as np

peso = quandl.get("BUNDESBANK/BBEX3_M_MXN_USD_CA_AB_A01", start_date="2000-03-31", authtoken="_uhAD1-g9JdY2teUwiAb")  # Import data using API call and applicable rules
cad = quandl.get("BUNDESBANK/BBEX3_M_CAD_USD_CA_AC_A01", start_date="2000-03-31", authtoken="_uhAD1-g9JdY2teUwiAb")

cad.to_csv('cad.csv')             # Export Data as .csv
peso.to_csv('peso.csv')
headers=['Date','Value','Value']

df1=pd.read_csv('fx.csv')

z=df1['Date'].values                                     # Define vectors spaces
x=df1['CAD'].values
y=df1['MXN'].values

plt.plot(z,x,y)
axes = plt.gca()                                         # Define axes
plt.title('MXN vs CAD')
axes = plt.gca()                                         # Define axes
plt.ylim(0, 30)                                          # Set y axis limits
#plt.ylim(plt.ylim()[::-1])                              # invert order of numbers on y axis

plt.gcf().autofmt_xdate()                                # beautify the x-labels

# Adjust axis scales
axes.set_yticks(axes.get_yticks()[::10])
axes.set_xticks(axes.get_xticks()[::8])

#Show plot
plt.show()
