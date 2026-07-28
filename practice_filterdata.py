import pandas as pd 

data = {
    "Product"  : ["Bat", "Ball", "Wickets", "Pads", "Helmet"],
    "Price"    : [35000, 400, 500, 1500, 3000]
}

# only products with prce greater than 2000

df =  pd.DataFrame(data)

print(df[df["Price"]>2000])
