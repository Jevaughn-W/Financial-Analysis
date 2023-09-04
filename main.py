# Importing yfinance library
import yfinance as yf



tesla = yf.Ticker('TSLA')

print (tesla.price)