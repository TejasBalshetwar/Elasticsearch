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

# inserting documents
# employees_data = [
#     {
#     'name': 'Vishnu',
#     'age': 21,
#     'programming_languages': ['C++', 'python', 'nodejs']
#     },
#     {
#     'name': 'Sanjay',
#     'age': 23,
#     'programming_languages': ['python', 'C#']
#     },
#     {
#     'name': 'Arjun',
#     'age': 33,
#     'programming_languages': ['C++', 'Ruby']
#     },
#     {
#     'name': 'Ram',
#     'age': 27,
#     'programming_languages': ['Rust', 'python']
#     }
# ]
# for data in employees_data: es.index(index='employees', document=data)


# get a document
# res = es.get(index="employees", id='O-p-koYBJdUnV4UuZxFA') # fetch doc
# print(res['_source'])


# update a document
# es.update(index="employees", id='O-p-koYBJdUnV4UuZxFA', doc={'country': 'US'},)
# res = es.get(index="employees", id='O-p-koYBJdUnV4UuZxFA')
# print(res)

# delete a document
# res = es.delete(index="employees", id='O-p-koYBJdUnV4UuZxFA')
# print(res)

# basic term query
# print(es.search(index="employees", query={"match": {'name':'Sanjay'}}))

# full-text search
# print(es.search(index="employees", query={"fuzzy": {'programming_languages':'python'}}))

# regex search
print(es.search(index="employees", query={"regexp": {'name':'.*n.*'}}))