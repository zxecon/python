- mean value by group (python vs. stata)

python:
```python
import numpy as np
import pandas as pd
from pandas.io.stata import StataReader

df = pd.read_stata('sample.dta')
df.groupby("finyear").mean()["numdiv"]
df["mdiv"] = df.groupby("year").mean()["numdiv"]
```

stata:
```stata
use "sample.dta"
bys year: egen mdiv = mean(div)
```
