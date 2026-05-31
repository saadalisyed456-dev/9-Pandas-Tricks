import pandas as pd
df=pd.DataFrame({"A":[1,1,2,2,3],"B":[10,10,20,30,30,40]})
df.drop_duplicates()