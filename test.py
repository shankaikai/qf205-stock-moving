import pandas as pd

df = pd.read_csv("./CSV/AAPL.csv")

y = df["Adj Close"]

thirdValue = y.iloc[2]

print(thirdValue)

