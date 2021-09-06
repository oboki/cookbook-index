curl -X PUT "localhost:9200/_template/template_autocomplete_keywords?pretty" -H 'Content-Type: application/json' -d '
{
    "template": "autocomplete_keywords-*",
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0,
        "refresh_interval": "10s",
        "index": {
            "analysis": {
                "normalizer": {
                    "case_insensitive": {
                        "filter": [
                            "lowercase",
                            "asciifolding"
                        ],
                        "type": "custom",
                        "char_filter": []
                    }
				},
				"tokenizer": {
					"nori_user_dict": {
						"type": "nori_tokenizer",
						"user_dictionary": "userdict_ko.txt",
						"decompound_mode": "mixed"
					}
				},
				"analyzer": {
					"nori_korean": {
						"filter": [
							"lowercase"
						],
						"type": "custom",
						"tokenizer": "nori_user_dict"
					}
				}
            }
        }
    },
    "mappings": {
        "properties": {
            "keyword": {
                "type": "text",
                "analyzer": "nori_korean",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "normalizer": "case_insensitive"
                    }
                }
            },
            "created_ts": {
                "type": "date"
            },
            "modified_ts": {
                "type": "date"
            }
        }
    }
}
'

curl -X PUT "localhost:9200/_template/template_codes?pretty" -H 'Content-Type: application/json' -d '
{
    "template": "codes-*",
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0,
        "refresh_interval": "10s",
        "index": {
            "analysis": {
                "normalizer": {
                    "case_insensitive": {
                        "filter": [
                            "lowercase",
                            "asciifolding"
                        ],
                        "type": "custom",
                        "char_filter": []
                    }
				},
				"tokenizer": {
					"nori_user_dict": {
						"type": "nori_tokenizer",
						"user_dictionary": "userdict_ko.txt",
						"decompound_mode": "mixed"
					}
				},
				"analyzer": {
					"nori_korean": {
						"filter": [
							"lowercase"
						],
						"type": "custom",
						"tokenizer": "nori_user_dict"
					}
				}
            }
        }
    },
    "mappings": {
        "properties": {
            "parent_id": {
                "type": "keyword"
            },
            "column_name": {
                "type": "text",
                "analyzer": "nori_korean",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "normalizer": "case_insensitive"
                    }
                }
            },
            "attribute_name": {
                "type": "text",
                "analyzer": "nori_korean",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "normalizer": "case_insensitive"
                    }
                }
            },
            "code": {
                "type": "text",
                "analyzer": "nori_korean",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "normalizer": "case_insensitive"
                    }
                }
            },
            "description": {
                "type": "text",
                "analyzer": "nori_korean",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "normalizer": "case_insensitive"
                    }
                }
            },
            "created_ts": {
                "type": "date"
            },
            "modified_ts": {
                "type": "date"
            }
        }
    }
}
'

curl -X PUT "localhost:9200/_template/template_columns?pretty" -H 'Content-Type: application/json' -d '
{
    "template": "columns-*",
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0,
        "refresh_interval": "10s",
        "index": {
            "analysis": {
                "normalizer": {
                    "case_insensitive": {
                        "filter": [
                            "lowercase",
                            "asciifolding"
                        ],
                        "type": "custom",
                        "char_filter": []
                    }
				},
				"tokenizer": {
					"nori_user_dict": {
						"type": "nori_tokenizer",
						"user_dictionary": "userdict_ko.txt",
						"decompound_mode": "mixed"
					}
				},
				"analyzer": {
					"nori_korean": {
						"filter": [
							"lowercase"
						],
						"type": "custom",
						"tokenizer": "nori_user_dict"
					}
				}
            }
        }
    },
    "mappings": {
        "properties": {
            "db_name": {
                "type": "keyword",
                "normalizer": "case_insensitive"
            },
            "table_name": {
                "type": "text",
                "analyzer": "nori_korean",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "normalizer": "case_insensitive"
                    }
                }
            },
            "column_name": {
                "type": "text",
                "analyzer": "nori_korean",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "normalizer": "case_insensitive"
                    }
                }
            },
            "entity_name": {
                "type": "text",
                "analyzer": "nori_korean",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "normalizer": "case_insensitive"
                    }
                }
            },
            "attribute_name": {
                "type": "text",
                "analyzer": "nori_korean",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "normalizer": "case_insensitive"
                    }
                }
            },
            "data_type": {
                "type": "keyword"
            },
            "data_length": {
                "type": "integer"
            },
            "is_pk": {
                "type": "keyword"
            },
            "is_protected": {
                "type": "keyword"
            },
            "position": {
                "type": "integer"
            },
            "description": {
                "type": "text",
                "analyzer": "nori_korean"
            },
            "parent_id": {
                "type": "keyword"
            },
            "created_ts": {
                "type": "date"
            },
            "modified_ts": {
                "type": "date"
            }
        }
    }
}
'

curl -X PUT "localhost:9200/_template/template_comments?pretty" -H 'Content-Type: application/json' -d '
{
    "template": "comments-*",
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0,
        "refresh_interval": "10s",
        "index": {
            "analysis": {
                "normalizer": {
                    "case_insensitive": {
                        "filter": [
                            "lowercase",
                            "asciifolding"
                        ],
                        "type": "custom",
                        "char_filter": []
                    }
				},
				"tokenizer": {
					"nori_user_dict": {
						"type": "nori_tokenizer",
						"user_dictionary": "userdict_ko.txt",
						"decompound_mode": "mixed"
					}
				},
				"analyzer": {
					"nori_korean": {
						"filter": [
							"lowercase"
						],
						"type": "custom",
						"tokenizer": "nori_user_dict"
					}
				}
            }
        }
    },
    "mappings": {
        "properties": {
            "db_name": {
                "type": "keyword",
                "normalizer": "case_insensitive"
            },
            "table_name": {
                "type": "text",
                "analyzer": "nori_korean",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "normalizer": "case_insensitive"
                    }
                }
            },
            "author": {
                "type": "keyword"
            },
            "comment": {
                "type": "text",
                "analyzer": "nori_korean"
            },
            "parent_id": {
                "type": "keyword"
            },
            "created_ts": {
                "type": "date"
            },
            "modified_ts": {
                "type": "date"
            }
        }
    }
}
'

curl -X PUT "localhost:9200/_template/template_tables?pretty" -H 'Content-Type: application/json' -d '
{
    "template": "tables-*",
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0,
        "refresh_interval": "10s",
        "index": {
            "analysis": {
                "normalizer": {
                    "case_insensitive": {
                        "filter": [
                            "lowercase",
                            "asciifolding"
                        ],
                        "type": "custom",
                        "char_filter": []
                    }
				},
				"tokenizer": {
					"nori_user_dict": {
						"type": "nori_tokenizer",
						"user_dictionary": "userdict_ko.txt",
						"decompound_mode": "mixed"
					}
				},
				"analyzer": {
					"nori_korean": {
						"filter": [
							"lowercase"
						],
						"type": "custom",
						"tokenizer": "nori_user_dict"
					}
				}
            }
        }
    },
    "mappings": {
        "properties": {
            "db_name": {
                "type": "keyword",
                "normalizer": "case_insensitive"
            },
            "table_name": {
                "type": "text",
                "analyzer": "nori_korean",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "normalizer": "case_insensitive"
                    }
                }
            },
            "entity_name": {
                "type": "text",
                "analyzer": "nori_korean",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "normalizer": "case_insensitive"
                    }
                }
            },
            "storage_type": {
                "type": "keyword"
            },
            "partition_key": {
                "type": "keyword"
            },
            "partition_range_from": {
                "type": "keyword"
            },
            "partition_range_to": {
                "type": "keyword"
            },
            "description": {
                "type": "text",
                "analyzer": "nori_korean"
            },
            "created_ts": {
                "type": "date"
            },
            "modified_ts": {
                "type": "date"
            }
        }
    }
}
'

curl -X PUT "localhost:9200/_template/template_users?pretty" -H 'Content-Type: application/json' -d '
{
    "template": "users-*",
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0,
        "refresh_interval": "10s",
        "index": {
            "analysis": {
                "normalizer": {
                    "case_insensitive": {
                        "filter": [
                            "lowercase",
                            "asciifolding"
                        ],
                        "type": "custom",
                        "char_filter": []
                    }
				},
				"tokenizer": {
					"nori_user_dict": {
						"type": "nori_tokenizer",
						"user_dictionary": "userdict_ko.txt",
						"decompound_mode": "mixed"
					}
				},
				"analyzer": {
					"nori_korean": {
						"filter": [
							"lowercase"
						],
						"type": "custom",
						"tokenizer": "nori_user_dict"
					}
				}
            }
        }
    },
    "mappings": {
        "properties": {
            "username": {
                "type": "keyword"
            }
        }
    }
}
'
