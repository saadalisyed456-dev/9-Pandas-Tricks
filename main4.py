import pandas as pd
df = pd.DataFrame({"score": [50, 90, 80, 95,]})
df.nlargest(2, "score")