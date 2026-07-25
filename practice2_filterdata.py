import pandas as pd

data = {

"Items"   :   ["Burger", "Showrma", "Biryani", "Cold Drinks"],
"Price"   :   [200, 250, 300, 150]

}

df = pd.DataFrame(data)

print(df[df["Price"]>150])