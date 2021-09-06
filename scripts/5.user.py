from elasticsearch import Elasticsearch, helpers
from os import environ as osenv
from hashlib import blake2b
from datetime import datetime
import json


def current_ts_isof():
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%S")


es_host = osenv.get('ES_HOST') if osenv.get('ES_HOST') else 'localhost:9200'
es_client = Elasticsearch(es_host, timeout=10)

actions = []
a = {
    "_index": "users-v1",
    "_id": 'oboki',
    "_source": {
        "username": 'oboki',
        "bookmark": [
            {
                "db_name": "DB_B",
                "entity_name": "\ud14c\uc774\ube14_D",
                "id": "bd2a4022d13b3e4860eb",
                "table_name": "TAB_D"
            },
            {
                "db_name": "DB_D",
                "entity_name": "\ud14c\uc774\ube14_A",
                "id": "7c3b431656114270d4ae",
                "table_name": "TAB_A"
            },
            {
                "db_name": "DB_C",
                "entity_name": "\ud14c\uc774\ube14_A",
                "id": "82f1e039fa08e8b2095a",
                "table_name": "TAB_A"
            },
            {
                "db_name": "DB_A",
                "entity_name": "\ud14c\uc774\ube14_R",
                "id": "66e6f31b829cb695e929",
                "table_name": "TAB_R"
            }
        ],
        "search_opts": {
            "target":"tables",
            "pagesize": {
                "all": 4,
                "single": 10,
            },
            "advanced": {
                "enabled": False,
                "items": []
            }
        },
        "recent_search_keywords": [],
        "created_ts": current_ts_isof(),
        "modified_ts": current_ts_isof()
    }
}
actions.append(a)

#print(json.dumps(actions,indent=2))
helpers.bulk(es_client, actions)
