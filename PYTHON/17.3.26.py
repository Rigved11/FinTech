import pandas as pd

data = {
    "hours": [1,2,3,4,5,6],
    "result": [0,0,0,1,1,1]
}

df = pd.DataFrame(data)

print(df)

print(df.head(3))

print(df.shape)

X = df[["hours"]]
y = df["result"]

print("Features:")
print(X)

print("Labels:")
print(y)