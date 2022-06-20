# import pandas as pd
# import io
# import requests
#
# url = "https://github.com/datapackage-examples/sample-csv/raw/master/sample.csv"
# s = requests.get(url).content
# c = pd.read_csv(io.StringIO(s.decode('utf-8')))
# # print(c)
#
# k = pd.DataFrame(c)
# print(k)

import pandas as pd

df = pd.read_csv('/Users/boonstation/DATA gis/covid-gistda_basic/covid19.csv')

print(df.head())
