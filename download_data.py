import requests

for i in range(1, 5):
    link = 'http://statbbi.nso.go.th/staticreport/Page/sector/TH/report/sector_01_1110{}_TH_.xlsx'.format(i)
    resp = requests.get(link)

    output = open('sector_01_1110{}.xlsx'.format(i), 'wb')
    output.write(resp.content)
    output.close()
