from pandas_datareader.data import DataReader
from datetime import date
import matplotlib.pyplot as plt

def get_finance_data(stock_name, data_source, start, end=None):
	"""Returns a DataReader with the financial data for the specfied stock name.

	Args:
		stock_name: Name of the stock.
		data_source: Where to get data from.
		start: First day of data
		end: Last day of day.

	"""
	return DataReader(stock_name, data_source, start, end)
		

# date range for financial data
start = date(1990	, 1, 1) 
end = date(2018, 4, 29) 


# 10-year Treasury rate
series_code = "DGS10"

# where we are getting data from
data_source = "fred"

# get data for 10-year Treasury rate
data = get_finance_data(series_code, data_source, start)

print "=========== Fred 10-year Treasury Rate ==========="
print data.info()
print "================================="


# Chart title
series_name = "10-year Treasury"
data = data.rename(columns={series_code: series_name})

# Plot the 10-year Treasury interest rate
data.plot(title=series_name)
plt.show()
