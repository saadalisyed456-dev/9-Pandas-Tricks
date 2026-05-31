import pandas as pd
df=pd.DataFrame({"A":[1,2,3]})
df=pd.assign({B=df.A*10})
df