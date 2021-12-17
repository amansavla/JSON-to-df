from urllib.request import urlopen
import json
import pandas as pd



url = "https://s3.amazonaws.com/open-to-cors/assignment.json"

response = urlopen(url)
data_json = json.loads(response.read())
data=pd.read_json(url)

#print(data)
df=pd.DataFrame()
df2=pd.json_normalize(data["products"])
print(df2.sort_values('popularity',ascending=True))
