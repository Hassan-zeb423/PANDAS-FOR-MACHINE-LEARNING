import pandas as pd 

data = {
    "Products" : ["Laptop", "Mobile", "Tablet", "Moniter", "Hard Disk"],
    "Price"    : [50000, 25000, 18000, 15000, 10000],
    "Stock"    : [23,45,67,23,56]
}

df = pd.DataFrame(data)
print("All dataframe")
print(df)
print("=====================")
# Print the third row
print("=====================")
print("only third row ,pname,pprice,pstock")
print(df.iloc[2])

# print only those product with price greater than 15000

print("=====================")
print("Products_Price >= 1500")
print(df[df["Price"]>=15000])
print("=====================")
print("Sorting dataframe in ascending order")
print(df.sort_values("Price"))