#! /usr/bin/python
from elasticsearch import Elasticsearch, helpers
import csv

# Connection to the cluster
# es = Elasticsearch(hosts = "http://@localhost:9200")

# Uncomment this command if you are using the secure installation with 3 nodes

es = Elasticsearch(hosts = "https://elastic:datascientest@localhost:9200",
                 ca_certs="./ca/ca.crt")
try:
    with open('Womens_Clothing.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        helpers.bulk(es, reader, index='test_women')
except Exception as ela :
    print(str(ela))