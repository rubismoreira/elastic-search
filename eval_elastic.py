#! /usr/bin/python
from elasticsearch import Elasticsearch
import json
import warnings

warnings.filterwarnings("ignore")

# Connection to the cluster
client = Elasticsearch(hosts = "https://elastic:datascientest@localhost:9200",
                 ca_certs="./ca/ca.crt")

# Specify your question number here.
# If you are making multiple requests for the same question, write "1-1", "1-2" ext...
question_number = "1-2"

query = {
  "query": {
    "match_all": {}
  }
}


response = client.search(index="womens_clothing", body=query)

# Saving the request and response in a json file
with open("./eval/{}.json".format("q_" + question_number + "_response"), "w") as f:
  json.dump(dict(response), f, indent=2)

with open("./eval/{}.json".format("q_" + question_number + "_request"), "w") as f:
  json.dump(query, f, indent=2)