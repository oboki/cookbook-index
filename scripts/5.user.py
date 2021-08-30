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
    "_id": 'Anonymous',
    "_source": {
        "username": 'Anonymous',
        "bookmark": [
            {
                "id": "7c3b431656114270d4ae",
                "db_name": "DB_D",
                "table_name": "TAB_A",
                "entity_name": "테이블_A"
            },
            {
                "id": "1fa187e64f2448d9db6c",
                "db_name": "DB_A",
                "table_name": "TAB_D",
                "entity_name": "테이블_D"
            }
        ],
        "search_opt": "tables",
        "recent_search_keywords": [
            "Vestibulum",
            "massa,",
            "lacinia,",
            "amet"
        ],
        "created_ts": current_ts_isof(),
        "modified_ts": current_ts_isof()
    }
}
actions.append(a)

#print(json.dumps(actions,indent=2))
helpers.bulk(es_client, actions)
