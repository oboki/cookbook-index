from elasticsearch import Elasticsearch, helpers
from hashlib import blake2b
from datetime import datetime

def create_hash_id(s):
    h = blake2b(digest_size=10)
    h.update(s.encode('utf-8'))
    return h.hexdigest()


def current_ts_isof():
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%S")


def lorem(num):
    dummy = [
        'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
        'Integer aliquam felis lacinia, tincidunt sem ut, tristique massa.',
        'Suspendisse molestie eros ut lacus facilisis hendrerit.',
        'In in mauris nec mi bibendum rhoncus vel vel arcu.',
        'Ut fringilla purus vel dapibus vehicula.',
        'Quisque sodales purus ut magna consequat viverra.',
        'In ut quam sit amet dui accumsan vulputate in vitae magna.',
        'Donec ut sapien sed urna feugiat fringilla.',
        'Vestibulum dictum sem in lorem efficitur varius.',
        'Praesent sed enim malesuada libero lobortis semper.',
        'Nunc sodales urna in mollis pharetra.',
        'Fusce eu magna id dui malesuada iaculis quis ac tellus.',
        'Duis sodales turpis suscipit, feugiat leo iaculis, condimentum nulla.',
        'Quisque viverra enim non tellus viverra, a consectetur nulla bibendum.',
        'Sed elementum felis rhoncus justo accumsan tempor.'
    ]
    return dummy[num % len(dummy)]


keywords = []
for i in range(15):
    keywords.extend(lorem(i).split())


es_client = Elasticsearch(
    'localhost:9200',
    timeout=10
)

actions = []
for i in range(65, 91):
    db_name = "".join(["DB_", chr(i)])
    for j in range(65, 91):
        table_name = "".join(["TAB_", chr(j)])
        actions.append({
            "_index": "tables-v1",
            "_id": create_hash_id("".join([
                db_name,
                table_name
            ])),
            "_source": {
                "db_name": db_name,
                "table_name": table_name,
                "entity_name": table_name.replace('TAB', '테이블'),
                "description": lorem(j),
                "storage_type": 'Parquet',
                "partition_key": 'base_dt',
                "partition_range_from": '20170701',
                "partition_range_to": '20210801',
                "created_ts": current_ts_isof(),
                "modified_ts": current_ts_isof()
            }
        })
        for k in range(65, 77):
            column_name = "".join(["COL_", chr(k)])
            actions.append({
                "_index": "columns-v1",
                "_id": create_hash_id("".join([
                    db_name,
                    table_name,
                    column_name
                ])),
                "_source": {
                    "db_name": db_name,
                    "table_name": table_name,
                    "entity_name": table_name.replace('TAB', '테이블'),
                    "column_name": column_name,
                    "attribute_name": column_name.replace('COL', '컬럼'),
                    "data_type": "VARCHAR2",
                    "data_length": k,
                    "position": k - 64,
                    "is_pk": 'N',
                    "is_protected": 'N',
                    "parent_id": create_hash_id("".join([
                        db_name,
                        table_name
                    ])),
                    "description": lorem(k),
                    "created_ts": current_ts_isof(),
                    "modified_ts": current_ts_isof()
                }
            })
            for l in range(65, 72):
                if j > 65: continue

                code_name = chr(l)
                actions.append({
                    "_index": "codes-v1",
                    "_id": create_hash_id("".join([
                        column_name,
                        code_name
                    ])),
                    "_source": {
                        "column_name": column_name,
                        "attribute_name": column_name.replace('COL', '컬럼'),
                        "code": keywords[l % len(keywords)],
                        "description": keywords[(l + 7) % len(keywords)],
                        "parent_id": create_hash_id("".join([
                            db_name,
                            table_name
                        ])),
                        "created_ts": current_ts_isof(),
                        "modified_ts": current_ts_isof()
                    }
                })


for i in range(len(keywords)):
    actions.append({
        "_index": "autocomplete_keywords-v1",
        "_source": {
            "keyword": keywords[i],
            "created_ts": current_ts_isof(),
            "modified_ts": current_ts_isof()
        }
    })

actions.append({
    "_index": "users-v1",
    "_id": 'anonymous',
    "_source": {
        "username": 'Anonymous',
        "bookmark": [],
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
})


helpers.bulk(es_client, actions)
