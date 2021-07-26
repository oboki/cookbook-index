from elasticsearch import Elasticsearch, helpers
from os import environ as osenv
from hashlib import blake2b
from datetime import datetime
import json

def lorem(num):
    if num == 1: return 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer aliquam felis lacinia, tincidunt sem ut, tristique massa. Suspendisse molestie eros ut lacus facilisis hendrerit.'
    elif num == 2: return 'Integer aliquam felis lacinia, tincidunt sem ut, tristique massa.'
    elif num == 3: return 'Suspendisse molestie eros ut lacus facilisis hendrerit.'
    elif num == 4: return 'In in mauris nec mi bibendum rhoncus vel vel arcu.'
    elif num == 5: return 'Ut fringilla purus vel dapibus vehicula. Quisque sodales purus ut magna consequat viverra.'
    elif num == 6: return 'Quisque sodales purus ut magna consequat viverra.'
    elif num == 7: return 'In ut quam sit amet dui accumsan vulputate in vitae magna. Donec ut sapien sed urna feugiat fringilla.'
    elif num == 8: return 'Donec ut sapien sed urna feugiat fringilla.'
    elif num == 9: return 'Vestibulum dictum sem in lorem efficitur varius.'
    elif num == 10: return 'Praesent sed enim malesuada libero lobortis semper. Nunc sodales urna in mollis pharetra. Fusce eu magna id dui malesuada iaculis quis ac tellus.'
    elif num == 11: return 'Nunc sodales urna in mollis pharetra.'
    elif num == 12: return 'Fusce eu magna id dui malesuada iaculis quis ac tellus.'
    elif num == 13: return 'Duis sodales turpis suscipit, feugiat leo iaculis, condimentum nulla.'
    elif num == 14: return 'Quisque viverra enim non tellus viverra, a consectetur nulla bibendum. Sed elementum felis rhoncus justo accumsan tempor.'
    elif num == 0: return 'Sed elementum felis rhoncus justo accumsan tempor.'


def hash_id(s):
    h = blake2b(digest_size=10)
    h.update(s.encode('utf-8'))
    return h.hexdigest()


def current_ts_isof():
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%S")


es_host = osenv.get('ES_HOST') if osenv.get('ES_HOST') else 'localhost:9200'
es_client = Elasticsearch(es_host,timeout=10)

actions = []
for i in range(65,91):
    CHR_I = chr(i)
    db_name = "DB_"+CHR_I
    for j in range(65,91):
        CHR_J = chr(j)
        column_name = "COL_" + CHR_I
        attribute_name = "컬럼_" + CHR_I
        code_name = CHR_J
        a = {
            "_index": "codes-v1",
            "_id": hash_id(column_name+code_name),
            "_source": {
                "column_name": column_name,
                "attribute_name": attribute_name,
                "code": str(j),
                "description": code_name,
                "created_ts": current_ts_isof(),
                "modified_ts": current_ts_isof()
            }
        }
        actions.append(a)
    for j in range(65,91):
        CHR_J = chr(j)
        table_name = "TAB_"+CHR_J
        a = {
            "_index": "tables-v1",
            "_id": hash_id(db_name+table_name),
            "_source": {
                "db_name": db_name,
                "table_name": table_name,
                "entity_name": "테이블_" + CHR_J,
                "description": lorem(j%15),
                "created_ts": current_ts_isof(),
                "modified_ts": current_ts_isof()
            }
        }
        actions.append(a)
        for k in range(65,91):
            CHR_K = chr(k)
            column_name = "COL_"+CHR_K
            a = {
                "_index": "columns-v1",
                "_id": hash_id(db_name+table_name+column_name),
                "_source": {
                    "db_name": db_name,
                    "table_name": table_name,
                    "entity_name": "테이블_" + CHR_J,
                    "column_name": column_name,
                    "attribute_name": "컬럼_"+CHR_K,
                    "data_type": "VARCHAR2",
                    "data_length": 5,
                    "position": k - 64,
                    "is_pk": 'N',
                    "description": lorem(k%15),
                    "created_ts": current_ts_isof(),
                    "modified_ts": current_ts_isof()
                }
            }
            actions.append(a)
            a = {
                "_index": "comments-v1",
                "_source": {
                    "db_name": db_name,
                    "table_name": table_name,
                    "column_name": "",
                    "code": "",
                    "author": 'oboki',
                    "comment": lorem(k%15),
                    "is_deleted": "N",
                    "created_ts": current_ts_isof(),
                    "modified_ts": current_ts_isof()
                }
            }
            actions.append(a)
            for l in range(15):
                a = {
                    "_index": "comments-v1",
                    "_source": {
                        "db_name": db_name,
                        "table_name": table_name,
                        "column_name": column_name,
                        "code": "",
                        "author": 'oboki',
                        "comment": lorem(l%15),
                        "is_deleted": "N",
                        "created_ts": current_ts_isof(),
                        "modified_ts": current_ts_isof()
                    }
                }
                actions.append(a)

#print(json.dumps(actions,indent=2))
helpers.bulk(es_client, actions)