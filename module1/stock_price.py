# Install yfinance package.

# Import yfinance
import yfinance as yf
# Plot the close prices
import matplotlib.pyplot as plt

# Get the data for the stock Apple by specifying the stock ticker, start date, and end date
data = yf.download(f'{input("Enter a stock symbol to retrieve history since 2018: ")}',
                   '2018-01-01',  # Initial date
                   '2021-08-22')  # End date

data.Close.plot()
plt.show()
