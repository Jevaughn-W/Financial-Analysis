# Importing yfinance library
import yfinance as yf


tesla = yf.Ticker('TSLA')

# Pull stock prices for 1 month
prices = tesla.history(period="1mo")

# Function to calculate the price per share of a stack
def price_per_share(stock):
  revenue = stock.info['totalRevenue']
  stock_volume = stock.info["sharesOutstanding"]
  return revenue / stock_volume

# Function to calculate price to earnings ratio
def price_to_earnings(stock):
  price = stock.info["regularMarketPreviousClose"]
  eps = stock.info["forwardEps"]
  return price / eps


print('This is tesla\'s pe ratio', price_to_earnings(tesla))
print('This is tesla\'s intrisic price', price_to_earnings(tesla) * price_per_share(tesla))