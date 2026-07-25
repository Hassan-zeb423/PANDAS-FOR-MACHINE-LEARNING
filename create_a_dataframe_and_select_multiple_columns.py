import pandas as pd

data = {
    "Product" : ["Laptop", "Mobile", "Tablet", "Monitor"],
    "Price"   : [50000, 25000, 18000, 12000],
    "Stock"   : [10,25,15,8]
}

df = pd.DataFrame(data)

print(df[["Product", "Price", "Stock"]])