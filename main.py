from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch('https://localhost:9200',ca_certs='./first/config/certs/http_ca.crt')

doc = {
    'author': 'author_name',
    'text': 'Interensting content...',
    'timestamp': datetime.now(),
}
resp = es.index(index="test-index", id=1, document=doc)
print(resp['result'])
# print(es.ping())