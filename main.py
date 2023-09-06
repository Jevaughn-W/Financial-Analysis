# Importing yfinance library
import yfinance as yf
import matplotlib.pyplot as plt


tesla = yf.Ticker('TSLA')

# Pull stock prices for 1 month
prices = tesla.history(period="1mo")

# Function to calculate the price per share of a stack
def earnings_per_share(stock):
  profit = stock.info['grossProfits']
  stock_volume = stock.info["sharesOutstanding"]
  return profit / stock_volume

# Function to calculate price to earnings ratio
def price_to_earnings(stock):
  price = stock.info["regularMarketPreviousClose"]
  eps = stock.info["forwardEps"]
  return price / eps


# print('This is tesla\'s pe ratio', price_to_earnings(tesla))
# print('This is tesla\'s earnings per share', earnings_per_share(tesla))
# print('This is tesla\'s intrisic price', price_to_earnings(tesla) * earnings_per_share(tesla))


## Sample code of how to construct a table in python
tesla = yf.Ticker("TSLA")
data = tesla.history(period="1y")


plt.figure(figsize=(12, 6))  # Adjust the figure size as needed
plt.plot(data.index, data["Close"], label="Stock Price")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.title("Tesla Stock Price Over Time")
plt.legend()
plt.grid(True)
plt.show()
