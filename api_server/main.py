import csv
import json
import requests
import xml.etree.ElementTree as ET
def csv_to_json(csv_file, json_file):
    with open(csv_file, 'r', encoding='cp949') as file:
        reader = csv.DictReader(file)
        with open(json_file, 'w', encoding='utf-8') as json_output:
            json_output.write(json.dumps([row for row in reader], indent=4, ensure_ascii=False))

route_id = 100100118
url = f"http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRouteAll?serviceKey=WVI7ZtvAVX6hik3qi1Y37dBT8JHku9C%2BWhfM2MKgmcnMqJvckqqUdOpGAf9EpWdzA5gsaTyth86%2FJnvo10Xxwg%3D%3D&busRouteId={route_id}"

response = requests.get(url)
tree = ET.ElementTree(ET.fromstring(response.content))

if tree.findtext('.//msgHeader/headerCd') == '0':
    stNm_list = [item.findtext('stNm') for item in tree.findall('.//itemList')]


csv_filename = 'bus.csv'
json_filename = 'test.json'

csv_to_json(csv_filename, json_filename)