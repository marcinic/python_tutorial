
import requests
import json
import pandas as pd


# Youths in school in Brazil, aged 15-24 Male and Female
brazil_school_m = "http://api.worldbank.org/countries/BRA/indicators/4.1.stud.15a24?per_page=100&date=1960:2015&format=json"
brazil_school_f = "http://api.worldbank.org/countries/BRA/indicators/4.2.stud.15a24?per_page=100&date=1960:2015&format=json"


request_m = requests.get(brazil_school_m)
json_m = json.loads(request_m.text)

request_f = requests.get(brazil_school_f)
json_f = json.loads(request_f.text)

data_frame = pd.DataFrame()
for row in json_m[1]:
	df = pd.io.json.json_normalize(row)
	data_frame = data_frame.append(df)
for row in json_f[1]:
	df = pd.io.json.json_normalize(row)
	data_frame = data_frame.append(df)

print(data_frame)

data_frame.to_csv("brazil_youth_education.csv")