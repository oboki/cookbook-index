curl -X POST "localhost:9200/_aliases?pretty" -H 'Content-Type: application/json' -d '
{
    "actions":[
        {
            "add":{
                "index":"tables-v1",
                "alias":"tables"
            }
        }
    ]
}
'

curl -X POST "localhost:9200/_aliases?pretty" -H 'Content-Type: application/json' -d '
{
    "actions":[
        {
            "add":{
                "index":"columns-v1",
                "alias":"columns"
            }
        }
    ]
}
'

curl -X POST "localhost:9200/_aliases?pretty" -H 'Content-Type: application/json' -d '
{
    "actions":[
        {
            "add":{
                "index":"codes-v1",
                "alias":"codes"
            }
        }
    ]
}
'

curl -X POST "localhost:9200/_aliases?pretty" -H 'Content-Type: application/json' -d '
{
    "actions":[
        {
            "add":{
                "index":"comments-v1",
                "alias":"comments"
            }
        }
    ]
}
'

curl -X POST "localhost:9200/_aliases?pretty" -H 'Content-Type: application/json' -d '
{
    "actions":[
        {
            "add":{
                "index":"autocomplete_keywords-v1",
                "alias":"autocomplete_keywords"
            }
        }
    ]
}
'