from datetime import datetime
from elasticsearch import Elasticsearch

# connection to elastic
es = Elasticsearch(
            ["https://elastic:c1+=-8fC3kMvGJ-JLb_J@localhost:9200"],
            use_ssl=True,
            verify_certs=True,
            ca_certs='./first/config/certs/http_ca.crt',
        )

# verify connection
# print(es.ping())

# Create index
# es.indices.create(index='test-index-23_02_2023', ignore=400)

# get all indices
# indices = es.indices.get_alias("*")

# delete index
# es.indices.delete(index='test-index-23_02_2023', ignore=[400, 404])

# Search for index
# index = "products"
# try:
#     resp = es.search(index=index)
#     print(resp["_shards"]["total"])
# except Exception as e:
#     print("Index does not exist")

# search if index exists based on pattern
# index = "reviews*"
# try:
#     resp = es.search(index=index)
#     print(resp["_shards"]["total"])
# except Exception as e:
#     print("Index does not exist")


