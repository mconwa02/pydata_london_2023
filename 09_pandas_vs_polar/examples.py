import polars as pl

df = pl.DataFrame(
    {
        "A": [1, 2, 3, 4, 5],
        "fruits": ["banana", "banana", "apple", "apple", "banana"],
        "B": [5, 4, 3, 2, 1],
        "cars": ["beetle", "audi", "beetle", "beetle", "beetle"],
    }
)

print(df)
print(df.filter(pl.col("B") > 2))
print(df.filter(pl.col("B") > 2).groupby("cars").agg(pl.sum("A")))