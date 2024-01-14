from elasticsearch import Elasticsearch
import json
import warnings

warnings.filterwarnings("ignore")

# Connection to the cluster
client = Elasticsearch(hosts = "https://elastic:datascientest@localhost:9200",
                 ca_certs="./ca/ca.crt")

# Retrieving the template
template = client.indices.get_template()

# Saving in a json file.
with open("./eval/{}.json".format("index_template"), "w") as f:
  json.dump(dict(template), f, indent=2)