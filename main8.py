import pandas as pd
df = pd.DataFrame({
    "name": ["A", "B", "C"],
    "score": [50, 90, 75]
})
df.style.highlight_max("score")