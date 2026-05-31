import pandas as pd
df=pd.DataFrame({
    "name":["Alice","Bob","Charlie",],
    "age":[25,34,26,]
})

df.query("age > 25")