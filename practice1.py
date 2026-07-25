# Display only the price column

import pandas as pd 

data =  {
    "Products"  : ["Motercylce", "Car", "Truck", "Tractor"],
    "Prices"    : [125000, 1000000, 50000000, 600000000]
}

df = pd.DataFrame(data)

print(df["Prices"])