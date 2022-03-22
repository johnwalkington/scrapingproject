import pandas as pd
import os
import re

df = pd.read_csv(os.path.join("Data", "Data_without_duplicates_and_all_info.csv"))

df = df.sort_values(by=["Product"])
df = df.reset_index()[
    [
        "Product",
        "fuel",
        "odometer",
        "paint_color",
        "title_status",
        "transmission",
        "condition",
        "engine_displaement",
        "type",
        "VIN",
        "Price",
        "year",
        "City",
    ]
]


df["word_count"] = df.Product.str.count(" ") + 1

having_one_word = df[df["word_count"] == 1].index
df = df.drop(having_one_word)

df = df[
    [
        "Product",
        "fuel",
        "odometer",
        "paint_color",
        "title_status",
        "transmission",
        "condition",
        "engine_displaement",
        "type",
        "Price",
        "year",
        "City",
    ]
]

outpath2 = os.path.join("Data", "sorting.csv")
df.to_csv(outpath2)


df2 = pd.read_csv(os.path.join("Data", "city_and_brand.csv"))
df["Brand"] = df2["Brand"]

outpath3 = os.path.join("Data", "merging.csv")
df.to_csv(outpath3)

# removing product which has weird brand

counts = df["Brand"].value_counts()
df = df[~df["Brand"].isin(counts[counts < 10].index)]
df = df.reset_index()
df = df[
    [
        "Product",
        "fuel",
        "odometer",
        "paint_color",
        "title_status",
        "transmission",
        "condition",
        "engine_displaement",
        "type",
        "Price",
        "year",
        "City",
        "Brand",
    ]
]


outpath = os.path.join("Data", "new_final_clean.csv")
df.to_csv(outpath)
