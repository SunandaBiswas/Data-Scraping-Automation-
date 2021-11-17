import yfinance as yf
df = yf.download("GOOGL" , start = "1995-01-01" , interval = '1d')
df
