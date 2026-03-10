import pandas as pd
import matplotlib.pyplot as plt

print("Loading market data...")

# Load dataset
data = pd.read_csv("market_data.csv", index_col=0, parse_dates=True)

# Calculate daily returns
returns = data.pct_change()

# Calculate volatility
volatility = returns.std()

print("\nMarket Volatility:")
print(volatility)

# Moving average
data["SP500_MA50"] = data["SP500"].rolling(window=50).mean()

# Correlation
correlation = returns.corr()

print("\nCorrelation Matrix:")
print(correlation)

# SAVE correlation matrix BEFORE plotting
correlation.to_csv("correlation_matrix.csv")

print("Correlation matrix saved!")

# Plot price trends
data[["SP500","Gold","Oil"]].plot(figsize=(10,6))
plt.title("Market Price Trends")
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()

# Plot moving average
data[["SP500","SP500_MA50"]].plot(figsize=(10,6))
plt.title("S&P500 Moving Average")
plt.show()

print("Analysis complete!")