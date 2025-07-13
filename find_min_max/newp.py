# import pandas as pd
# # mydict={
# #     "car ": ["swift","bmw","thar"],
# #     "qulity":[1,2,3] 
# # }
# # myvar=ps.DataFrame(mydict)
# # print(myvar)
# newpp=pd.read_json("newjson.json")
# print(newpp.to_string)
import  pandas as pd
import matplotlib as plt
df =pd.read_csv("data.csv")
df.plot