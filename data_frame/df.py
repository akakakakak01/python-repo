import pandas as pd

dict = {
    "name": ["alex", "john", "bob"],
    "roll": [1,2,3],
    "age": [23,24,25]
}

print(dict.keys())
print(dict.values())

df = pd.DataFrame(dict)
print(df)