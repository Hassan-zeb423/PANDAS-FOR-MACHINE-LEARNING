import pandas as pd
data = {
    "Name"  : ["Hassan", "Saeedullah", "Sameer", "Imtiaz"],
    "Age"   : [19,21,22,20],
    "CGPA"  : [3.2,2.6,3.2,3.7],
    "City"  : ["Mardan", "Hangu", "Laki Marwat", "Barha"],
    "Hobby" : ["Cricket", "Ludo", "Football", "internet"],
}

df = pd.DataFrame(data)

print(df.loc[3])