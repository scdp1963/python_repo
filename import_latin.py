from glob import iglob
from datetime import datetime
import nltk
from elasticsearch import Elasticsearch
import codecs
es = Elasticsearch(['localhost:9200'])


def clean_text(text):
    return text

template= {"title":"This is a title","author":"so and so","data":"","sentence_id":1,"filename":""}
for filename in iglob("*.txt"):
    doc=template
    doc['filename']=filename
    try:
        with codecs.open(filename, encoding='utf-8', mode='r+') as f1:
            data= f1.read()
        doc['data']=clean_text(data)
        res = es.index(index="latin", doc_type='library',body=doc)
    except Exception as exp:
        raise exp
        print("ERROR: {0}: {1}".format(filename,exp))


res = es.search(index="latin",doc_type='library', body={"query": {"match_all": {}}})
print(res)
for hit in res['hits']['hits']:
    print("******************** {0} ***************************".format(hit["_source"]["filename"]))
    print (hit["_source"])

