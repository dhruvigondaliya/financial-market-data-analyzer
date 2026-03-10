import yfinance as yf
import pandas as pd

print("Downloading financial data...")

# Download financial data
sp500 = yf.download("^GSPC", period="1y")
gold = yf.download("GC=F", period="1y")
oil = yf.download("CL=F", period="1y")

# Extract closing prices
sp500_close = sp500["Close"]
gold_close = gold["Close"]
oil_close = oil["Close"]

# Combine into one dataframe
data = pd.concat([sp500_close, gold_close, oil_close], axis=1)

# Rename columns
data.columns = ["SP500", "Gold", "Oil"]

# Remove missing values
data = data.dropna()

# Save to CSV
data.to_csv("market_data.csv")

print("Data downloaded successfully!")
print(data.head())