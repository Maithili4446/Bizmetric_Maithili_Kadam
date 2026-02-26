import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Download Bitcoin data
btc = yf.download("BTC-USD", start="2023-01-01", end="2024-01-01")

# If columns are multi-index, flatten them
if isinstance(btc.columns, pd.MultiIndex):
    btc.columns = btc.columns.get_level_values(0)

# Ensure Close column is 1D
close_prices = btc["Close"].astype(float)

# Calculate Moving Averages
btc["MA20"] = close_prices.rolling(window=20).mean()
btc["MA50"] = close_prices.rolling(window=50).mean()

# Dark theme
plt.style.use("dark_background")

plt.figure(figsize=(14,7))

# Plot Closing Price
plt.plot(btc.index, close_prices, linewidth=2, label="Closing Price")

# Fill area safely
plt.fill_between(btc.index, close_prices.values, alpha=0.2)

# Plot Moving Averages
plt.plot(btc.index, btc["MA20"], linestyle="--", label="20-Day MA")
plt.plot(btc.index, btc["MA50"], linestyle="--", label="50-Day MA")

# Highlight Highest
max_price = close_prices.max()
max_date = close_prices.idxmax()
plt.scatter(max_date, max_price, s=100)
plt.text(max_date, max_price, f" High: {round(max_price,2)}")

# Highlight Lowest
min_price = close_prices.min()
min_date = close_prices.idxmin()
plt.scatter(min_date, min_price, s=100)
plt.text(min_date, min_price, f" Low: {round(min_price,2)}")

plt.title("Bitcoin (BTC-USD) Price Trend - 2023", fontsize=18)
plt.xlabel("Date")
plt.ylabel("Price in USD")

plt.grid(True, linestyle="--", alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()