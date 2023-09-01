
import pandas as pd
import numpy as np
from preprocessing import  columnDropTransformer


in_str = ["Teufel", "target_"]

df = pd.DataFrame({"Teufelchen": [1,2,3], "angle":[4,5,6], "target_1": [7,8,9],"target0": [10,11,12] })
df_expected = pd.DataFrame({"angle":[4,5,6], "target0": [10,11,12] })

resl = columnDropTransformer(in_str)
df_keys = resl.transform(df)
assert   df_keys.equals(df_expected)


# for testing good video 
# https://www.google.com/search?q=pytest+assert+example&client=safari&sca_esv=561856720&rls=en&biw=1694&bih=845&tbm=vid&sxsrf=AB5stBgPkhbZBTKlU1iDyfon_OIPL27MLA%3A1693552461860&ei=TY_xZLKXNN6oi-gPmc2RiA4&ved=0ahUKEwjy8ZbH7oiBAxVe1AIHHZlmBOEQ4dUDCAw&uact=5&oq=pytest+assert+example&gs_lp=Eg1nd3Mtd2l6LXZpZGVvIhVweXRlc3QgYXNzZXJ0IGV4YW1wbGUyCBAAGIAEGMsBMgYQABgWGB5IgBVQrQNY3RNwAHgAkAEAmAFLoAHeBKoBATm4AQPIAQD4AQHCAgQQIxgnwgIKEAAYgAQYFBiHAsICBRAAGIAEiAYB&sclient=gws-wiz-video#fpstate=ive&vld=cid:2b6e92d3,vid:J3tQDIikdEo