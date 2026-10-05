def add_candle_features(df):
    df = df.copy()

    # Size of the candle body
    df["Body"] = abs(df["Close"] - df["Open"])

    # Total candle range
    df["Range"] = df["High"] - df["Low"]

    # Upper wick
    df["Upper_Wick"] = (
        df["High"] - df[["Open", "Close"]].max(axis=1)
    )

    # Lower wick
    df["Lower_Wick"] = (
        df[["Open", "Close"]].min(axis=1) - df["Low"]
    )

    # Is the candle bullish?
    df["Bullish"] = (df["Close"] > df["Open"]).astype(int)

    # Is the candle bearish?
    df["Bearish"] = (df["Close"] < df["Open"]).astype(int)

    return df