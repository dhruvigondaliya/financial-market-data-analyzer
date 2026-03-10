import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Financial Market Dashboard")

# Load data
data = pd.read_csv("market_data.csv", index_col=0, parse_dates=True)

st.subheader("Market Data")
st.write(data.tail())

# Line chart
st.subheader("Market Trends")
st.line_chart(data)

# Correlation
st.subheader("Correlation Matrix")

correlation = data.pct_change().corr()
st.write(correlation)

# Volatility
st.subheader("Market Volatility")

volatility = data.pct_change().std()
st.write(volatility)

st.subheader("Correlation Heatmap")

returns = data.pct_change()
corr = returns.corr()

fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)

st.pyplot(fig)

st.subheader("Market Risk Indicator")

volatility = data.pct_change().std().mean()

if volatility > 0.02:
    risk = "High Risk"
elif volatility > 0.01:
    risk = "Medium Risk"
else:
    risk = "Low Risk"

st.metric("Market Risk Level", risk)

st.subheader("Market Insight Summary")

# Calculate trends
sp500_trend = data["SP500"].iloc[-1] - data["SP500"].iloc[-30]
gold_trend = data["Gold"].iloc[-1] - data["Gold"].iloc[-30]
oil_trend = data["Oil"].iloc[-1] - data["Oil"].iloc[-30]

# Determine trend direction
def trend_text(value):
    if value > 0:
        return "increasing"
    else:
        return "decreasing"

sp500_direction = trend_text(sp500_trend)
gold_direction = trend_text(gold_trend)
oil_direction = trend_text(oil_trend)

# Calculate risk
volatility = data.pct_change().std().mean()

if volatility > 0.02:
    risk = "High"
elif volatility > 0.01:
    risk = "Medium"
else:
    risk = "Low"

# Generate insight text
insight = f"""
The S&P500 trend is {sp500_direction} over the last month.
Gold prices are {gold_direction}, while oil prices are {oil_direction}.
Overall market volatility suggests a **{risk} market risk level**.
"""

st.write(insight)