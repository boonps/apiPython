import pandas as pd

df = pd.read_excel(
    "/Users/boonstation/OneDrive - Naresuan University/GISTDA/DATA_portal/สถิติประชากรศาสตร์ ประชากรและเคหะ/ประชากรศาสตร์:ประชากร/ครัวเรือนและครอบครัว/sector_01_11551_TH_.xlsx",
    engine='openpyxl',
    sheet_name="ข้อมูล",
    skiprows=5,
    nrows=240,
    usecols="A:F")
dev = pd.DataFrame(df)
# print(dev)
value = []
index = []
# for i, k in enumerate(dev["province"]):
#     # print(i, k.strip())
#     if "ในเขตเทศบาล" in k:
#         value.append(dev.strip())
# # print(value)
# dev2 = pd.Series(dev['hh_sum'])
# # print(dev2)
# show = dev2.loc[[0, 1]]
# print(show)

# df = dev.columns.str.strip()
# df2 = dev.columns[3:]
#
# print(df)
# print(df2)

keyword_list = dev["province"]
text = 'ในเขตเทศบาล'

# if any(d in text for d in d):
lists = ['hh_sum': [2], 'hh_private': [2], 'hh_group': [2], 'test': [2], 'test2': [2]]
select = pd.DataFrame(data=lists)

print(select)

# for key, item in enumerate(keyword_list):
#     item = item.strip()
#     print(key, item)
# if item in text:
# pp = pd.DataFrame({'test': dev['hh_sum'],
#                    'test2': dev['hh_private'],
#                    'test3': dev['hh_group']},
#                   index=[key - 1, key - 1, key - 1])
# index=[key])
# print(item)

# print(pp)
# print(dev)
# print(value)
