
import pandas as pd
import numpy as np
from preprocessing import  columnDropTransformer


in_str = ["Teufel", "target_"]

df = pd.DataFrame({"Teufelchen": [1,2,3], "angle":[4,5,6], "target_1": [7,8,9],"target0": [10,11,12] })
df_expected = pd.DataFrame({"angle":[4,5,6], "target0": [10,11,12] })

resl = columnDropTransformer(in_str)
df_keys = resl.transform(df)
assert   df_keys.equals(df_expected)



