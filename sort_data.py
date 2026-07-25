# Sort products by pricing in acending order

import pandas as pd 

data = {

    "Products"  : ["Laptop", "Mobile", "Tablet", "Monitor"],
    "Price"     : [50000, 25000, 18000, 15000],
    "Stock"     : [15, 25, 18, 8]

}

df = pd.DataFrame(data)

print(df.sort_values("Price"))