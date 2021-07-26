from elasticsearch import Elasticsearch, helpers
from os import environ as osenv
from hashlib import blake2b
import json

def hash_id(s):
    h = blake2b(digest_size=10)
    h.update(s.encode('utf-8'))
    return h.hexdigest()


es_host = osenv.get('ES_HOST') if osenv.get('ES_HOST') else 'localhost:9200'
es_client = Elasticsearch(es_host,timeout=10)

actions = []
a = {
    "_index": "codes-v1",
    "_id": hash_id(''),
    "_source": {
        "dummy": ''
    }
}
actions.append(a)

a = {
    "_index": "tables-v1",
    "_id": hash_id(''),
    "_source": {
        "dummy": ''
    }
}
actions.append(a)

a = {
    "_index": "columns-v1",
    "_id": hash_id(''),
    "_source": {
        "dummy": ''
    }
}
actions.append(a)

a = {
    "_index": "comments-v1",
    "_id": hash_id(''),
    "_source": {
        "dummy": ''
    }
}
actions.append(a)

a = {
    "_index": "autocomplete_keywords-v1",
    "_id": hash_id(''),
    "_source": {
        "dummy": ''
    }
}
actions.append(a)

print(json.dumps(actions,indent=2))

helpers.bulk(es_client, actions)