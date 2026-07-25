import pandas as pd 

data = {
    "Product" : ["Laptop", "Mobile", "Tablet", "Monitor"],
    "Price"   : [50000, 25000, 18000, 15000],
    "Stock"   : [25,18,45,67]
}

df = pd.DataFrame(data)

print(df[["Product", "Stock"]])