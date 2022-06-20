import pandas as pd
import requests

url = "https://api.nso.go.th/api/v1.0/branch2/dataset/36?year=2562"

payload = {}
headers = {
    'Authorize': '9330bb95-e5af-4aca-a253-f1e8d26c7176',
    'Acceptt': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)
j = response.json()
dev = pd.DataFrame(j["Result"]["data"])
print(dev)

##set type
# dev = dev.astype({"Column9": int, "Column11": float})
# print(dev.dtypes)

## check info(encoding)##
# data = open("apitest.csv", "r")
# print(data)
#
# with open("name_1.txt", "rt", encoding="utf8") as f:
#     classNames = f.read().rstrip("\n").split("\n")
#
#     dev_re = dev.columns = [i for i in classNames]
#     dev = dev.astype({"DIM_ID": int, "จำนวน": float, "UNIT1T": str})
#     print(dev.dtypes)
#     dev.to_csv("apitest2.csv", encoding="utf8")

# for i in (j["Result"]["data"]):
#     print(i["Column0"])
