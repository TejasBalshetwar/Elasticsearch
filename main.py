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
# es.update(index="employees", id='Oup-koYBJdUnV4UuZxEw', doc={'country': 'US'},)
# res = es.get(index="employees", id='O-p-koYBJdUnV4UuZxFA')
# print(res)

# delete a document
# res = es.delete(index="employees", id='O-p-koYBJdUnV4UuZxFA')
# print(res)

# Simplest search query
# print(es.search(index="employees", query={"match_all": {}}))

# basic term query
# print(es.search(index="employees", query={"match": {'name':'Sanjay'}}))

# term query with keyword field with case insensitive parameter
# print(es.search(index="employees", query={"term":{"programming_languages.keyword":{"value":"Python","case_insensitive":True}}}))

# terms query
# print(es.search(index="employees", query={"terms":{"programming_languages.keyword":["Ruby","nodejs"]}}))

# documents based on IDs
# print(es.search(index="employees",query={"ids":{"values":["OOp-koYBJdUnV4UuZREd","Oep-koYBJdUnV4UuZxEk"]}}))

# range search
# print(es.search(index="employees", query={"range": {'age':{"gte": 21, "lte": 30}}}))

# prefix search
# print(es.search(index="employees", query={"prefix": {'name':{"value":"A","case_insensitive":True}}}))

# single-char wildcard search
# print(es.search(index="employees",query={"wildcard":{"programming_languages.keyword":"?uby"}}))

# multi-char wildcard search
# print(es.search(index="employees",query={"wildcard":{"programming_languages.keyword":"p*"}}))

# regex search . stands for any character and * stands for any number of characters and ? stands for any single character
# print(es.search(index="employees", query={"regexp": {'name':'.*n.*'}}))

# querying by field existance
# print(es.search(index="employees", query={"exists": {"field": "country"}}))

# match query full-text search with operator and but default is or
# print(es.search(index="employees",query={"match":{"name":"arjun"}}))
# print(es.search(index="employees",query={"match":{"name":{"query":"vishnu arjun","operator":"and"}}}))

# searching multiple fields
# print(es.search(index="employees",query={"multi_match":{"query":"ruby","fields":["name","programming_languages"]}})) # searches for word in both name and programming_languages field
# We can also boost relevance score for a particular field which will give more importance to that field
# a tie_breaker attribute can also be used which will basically multiply the relevance score of the lower score field with what we give the arguement and will add to the field with higher relevance score

# phrase searches
# print(es.search(index="employees",query={"match_phrase":{"name":"arjun nepal"}}))
# in match_phrase the order of the words entered matters and in consecutive manner unlike the match query

# boolean compound query using must and must_not
# print(es.search(index="employees", query={"bool": {"must": {"term":{"programming_languages.keyword":"Python"}} }})) # must the query parameter

# print(es.search(index="employees", query={"bool": {"must": {"term":{"programming_languages.keyword":"python"}},"must_not": {"term":{"programming_languages.keyword":"nodejs"}} }})) # musn't contain the query paramter

# boolean compound query using should which will boost the score if found true
# print(es.search(index="employees", query={"bool": {"should": [{"term":{"programming_languages.keyword":"python"}}],"must": [{"term":{"programming_languages.keyword":"python"}}],"must_not": [{"term":{"programming_languages.keyword":"nodejs"}}] } }))


# boolean compound query using filter - similar to must difference is that filter ignores relevance scores
# filter is highly efficient and can be used to cache results
# print(es.search(index="employees",query={"bool":{"filter":{"term":{"programming_languages.keyword":"python"}}}}))


# SELECT * FROM employees WHERE programming_languages IN ("python") AND (name LIKE '%python%' OR description LIKE '%python%') AND age <= 30
# print(es.search(index="employees",query={
#     "bool": {
#         "filter": [
#             {
#                 "range": {
#                     "age": {
#                         "lte": 30
#                     }
#                 }
#             },
#             {
#                 "term": {
#                     "programming_languages.keyword": "python"
#                 }
#             }
#         ],
#         "must": [
#             {
#                 "multi_match": {
#                     "query": "python",
#                     "fields": [
#                         "name",
#                         "programming_languages"
#                     ]
#                 }
#             }
#         ]
#     }
# }))

# boosting query- changing 
# print(es.search(index="employees",query={
#     "boosting": {
#       "positive": {
#         "match_all": {}
#       },
#       "negative": {
#         "match": {
#           "name": "arjun"
#         }
#       },
#       "negative_boost": 0.5
#     }
#   }))


# disjunction max
# print(es.search(index="employees",query={
#     "dis_max": {
#       "queries": [
#         { "match": { "name": "python" } },
#         { "match": { "programming_language": "python" } }
#       ],
#       "tie_breaker": 0.3
#     }
# }))




# fuzzy search
# print(es.search(index="employees", query={"fuzzy": {'programming_languages':'python'}}))
