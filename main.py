# Importing yfinance library
import yfinance as yf


tesla = yf.Ticker('TSLA')

# Pull stock prices for 1 month
prices = tesla.history(period="1mo")

#function to calculate the price per share of a stack
def price_per_share(stock):
  revenue = stock.info['totalRevenue']
  stock_volume = stock.info["sharesOutstanding"]
  return revenue / stock_volume


print('This is the price per share', price_per_share(tesla))