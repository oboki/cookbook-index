import requests
import json
from elasticsearch import Elasticsearch

es_client = Elasticsearch(
    "localhost:9200",
    timeout=10
)

indices = [
    'tables',
    'columns',
    'codes',
    'comments',
    'users',
    'autocomplete_keywords'
]

for index in indices:
    # create index template
    with open("".join([
            'templates/', index, '.json'
        ]), 'rt'
    ) as f:
        template = json.load(f)
        url = "".join(['http://localhost:9200/_template/template_', index])

        res = requests.post(
            url,
            headers={
                "Content-Type": "application/json"
            },
            json=template
        )
        print(res)

    # index dummy doc
    res = es_client.index(
        index = "".join([index, "-v1"]),
        id = "dummy",
        body = {}
    )
    print(res)

    # set alias
    res = requests.post(
        "http://localhost:9200/_aliases",
        headers={
            "Content-Type": "application/json"
        },
        json= {
            "actions": [{
                "add":{
                    "index": "".join([index, "-v1"]),
                    "alias": index
                }
            }]
        }
    )
    print(res)

    # delete dummy doc
    res = es_client.delete(
        index = "".join([index, "-v1"]),
        id = "dummy",
    )
    print(res)