#!C:/Python27/python.exe
import json

print "Content-type: text/html\r\n\r\n"

with open("excel_data_demo.json", "r") as outfile:
    data = json.dumps(json.load(outfile), indent=4, separators=(',', ': '))
type(data)
new_data = [
    {
        "impact": 0.4,
        "is_parent": 1,
        "name": "NPS Score",
        "key": "NPS_Telstra_NA_NA_NPS-CVA-NPSScore"
    },
    {
        "impact": 0.1,
        "is_parent": 0,
        "name": "% Promoters",
        "key": "NPS_Telstra_NA_NA_NPS-CVA-Promoters"
    },
    {
        "impact": 0,
        "is_parent": 0,
        "name": "% Passives",
        "key": "NPS_Telstra_NA_NA_NPS-CVA-Passives"
    },
    {
        "impact": -0.9,
        "is_parent": 0,
        "name": "% Detractors",
        "key": "NPS_Telstra_NA_NA_NPS-CVA-Detractors"
    },
    {
        "impact": 1,
        "is_parent": 0,
        "name": "% Reactors",
        "key": "NPS_Telstra_NA_NA_NPS-CVA-Reactors"
    },
    {
        "impact": 0.5,
        "is_parent": 1,
        "name": "%XYZ",
        "key": "NPS_Telstra_NA_NA_NPS-CVA-XYZ"
    },
    {
        "impact": 0.2,
        "is_parent": 0,
        "name": "%ABC",
        "key": "NPS_Telstra_NA_NA_NPS-CVA-ABC"
    },
    {
        "impact": -0.7,
        "is_parent": 0,
        "name": "%UV",
        "key": "NPS_Telstra_NA_NA_NPS-CVA-UV"
    },
    {
        "impact": 0.6,
        "is_parent": 0,
        "name": "%MN",
        "key": "NPS_Telstra_NA_NA_NPS-CVA-MN"
    },
    {
        "impact": -0.4,
        "is_parent": 0,
        "name": "%JKL",
        "key": "NPS_Telstra_NA_NA_NPS-CVA-JKL"
    }
]
type(new_data)
# print data
