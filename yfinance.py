#Download historical finance data from Yahoo!finance
#read more: https://pypi.org/project/yfinance/

import yfinance as yf
df = yf.download("GOOGL" , start = "1995-01-01" , interval = '1d')
df
