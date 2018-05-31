import matplotlib as plt
import pandas as pd
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import numpy as np
from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
from pandas.plotting import autocorrelation_plot
from statsmodels.tsa.arima_model import ARIMA
from pandas import DataFrame, Series
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.stattools import adfuller

peso = read_csv('peso.csv', header=0, parse_dates=[0], index_col=0, squeeze=True)
print(peso.head())
peso.plot()
plt.title('MXN Time Series')
pyplot.show()

peso_ = read_csv('peso.csv', header=0, parse_dates=[0], index_col=0, squeeze=True)
autocorrelation_plot(peso_)
plt.title('MXN Autocorrelation')
pyplot.show()

cad = read_csv('cad.csv', header=0, parse_dates=[0], index_col=0, squeeze=True)
print(cad.head())
cad.plot()
plt.title('CAD Time Series')
pyplot.show()

cad_ = read_csv('peso.csv', header=0, parse_dates=[0], index_col=0, squeeze=True)
autocorrelation_plot(cad_)
plt.title('CAD Autocorrelation')
pyplot.show()

print('Peso ARIMA Analysis')
series = read_csv('peso.csv', header=0, parse_dates=[0], index_col=0, squeeze=True)
# fit model
model = ARIMA(series, order=(1,1,0))
model_fit = model.fit(disp=0)
print(model_fit.summary())
# plot residual errors
residuals = DataFrame(model_fit.resid)
residuals.plot()
plt.title('MXN Residuals')
pyplot.show()
residuals.plot(kind='kde')
plt.title('MXN Residuals')
pyplot.show()
print(residuals.describe())


#Cointegration
print(" ")
print("Forcasting MXN")

series = read_csv('peso.csv', header=0, parse_dates=[0], index_col=0, squeeze=True)
X = series.values
size = int(len(X) * 0.66)
train, test = X[0:size], X[size:len(X)]
history = [x for x in train]
predictions = list()
for t in range(len(test)):
	model = ARIMA(history, order=(1,1,0))
	model_fit = model.fit(disp=0)
	output = model_fit.forecast()
	yhat = output[0]
	predictions.append(yhat)
	obs = test[t]
	history.append(obs)
	print('predicted=%f, expected=%f' % (yhat, obs))
error = mean_squared_error(test, predictions)
print('Test MSE: %.3f' % error)
# plot
pyplot.plot(test)
pyplot.plot(predictions, color='red')
plt.title('MXN Forecast - predictions red')
pyplot.show()

print(" ")
print("Forcasting CAD")

series = read_csv('cad.csv', header=0, parse_dates=[0], index_col=0, squeeze=True)
X = series.values
size = int(len(X) * 0.66)
train, test = X[0:size], X[size:len(X)]
history = [x for x in train]
predictions = list()
for t in range(len(test)):
	model = ARIMA(history, order=(1,1,0))
	model_fit = model.fit(disp=0)
	output = model_fit.forecast()
	yhat = output[0]
	predictions.append(yhat)
	obs = test[t]
	history.append(obs)
	print('predicted=%f, expected=%f' % (yhat, obs))
error = mean_squared_error(test, predictions)
print('Test MSE: %.3f' % error)
# plot
pyplot.plot(test)
pyplot.plot(predictions, color='orange')
plt.title('CAD Forecast - predictions orange')
pyplot.show()


print("Now for some  Augmented Dickey-Fuller (ADF) testing")
series = Series.from_csv('fx.csv', header=0)
X = series.values
result = adfuller(X)
print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])
print('Critical Values:')
for key, value in result[4].items():
	print('\t%s: %.3f' % (key, value))
print("Since we can't reject the null, we non-stationary series")
print("Series aren't cointegrated")
