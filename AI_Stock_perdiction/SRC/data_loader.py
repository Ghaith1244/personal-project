import pandas as pd
from features import add_candle_features
# Path to the stock dataset
file_path = "data/SP500_Historical_Data.csv"

# Load the dataset
df = pd.read_csv(file_path)

# Show the first 5 rows
print("First 5 rows:")
print(df.head())

# Show all column names
print("\nColumns:")
print(df.columns)

# Show the size of the dataset
print("\nDataset size:")
print(df.shape)

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate rows:")
print(df.duplicated().sum())

# Check data types
print("\nData types:")
print(df.dtypes)

# Check number of stocks
print("\nNumber of stocks:")
print(df["Ticker"].nunique())

# Convert Date from text to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Stocks we want to use
selected_tickers = ["AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "TSLA"]

# Select these stocks
stocks = df[df["Ticker"].isin(selected_tickers)].copy()

# Sort by stock and date
stocks = stocks.sort_values(["Ticker", "Date"])

print("\nSelected stocks:")
print(stocks["Ticker"].unique())

print("\nNumber of trading days per stock:")
print(stocks.groupby("Ticker").size())

print("\nFirst rows:")
print(stocks.head())

print("\nDate range per stock:")
print(
    stocks.groupby("Ticker")["Date"]
    .agg(["min", "max"])
)
# Add candlestick features
stocks = add_candle_features(stocks)

print("\nCandlestick features:")

columns = [
    "Ticker",
    "Date",
    "Open",
    "High",
    "Low",
    "Close",
    "Body",
    "Range",
    "Upper_Wick",
    "Lower_Wick",
    "Bullish",
    "Bearish"
]

print(stocks[columns].head(10).to_string(index=False))