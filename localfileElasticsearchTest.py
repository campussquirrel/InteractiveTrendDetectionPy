from elasticsearch import Elasticsearch, helpers
import sys, json
from os import listdir
import subprocess
from elasticsearch import Elasticsearch
import os
#subprocess.Popen('C:/Users/Noushin/Downloads/elasticsearch-6.2.4/elasticsearch-6.2.4/bin/elasticsearch.bat')
es = Elasticsearch()
#es.reindex

directory='Data/'
#for filename in os.listdir(directory):
 #      if filename.endswith('.json'):
  #        print(filename)
   #       open(filename,'r') as open_file:


#print(os.getcwd())


doc1 = {"IN.CTY":["73269 Hochdorf"],"PRY":["2000"],"PRYF":["2000"],"TIEN":"DEVICE, ESPECIALLY A COMBINED MOTOR/GENERATOR DEVICE, FOR CONVERTING ELECTRIC ENERGY INTO MECHANICAL ENERGY AND/OR VICE VERSA","DT":"patent"}
doc2 = {"IN.CTY":["4816 Noushin"],"PRY":["1986"],"PRYF":["1984"],"TIEN":" NOUSHIN HAS ALWAYS BEEN THE BEST. SHE WOULD FIND THE SOLUTION AS LONG AS SHE IS THERE. A SUPER HERO.","DT":"patent"}
doc3 = {"IN.CTY":["2354 Nehzat"],"PRY":["1984"],"PRYF":["1984"],"TIEN":" NEHZAT HAS ALWAYS BEEN THE BEST. SHE WOULD FIND THE SOLUTION AS LONG AS SHE IS THERE. A SUPER HERO.","DT":"patent"}


#,"DETDL":null}
res = es.index(index="test-index", doc_type='tweet', id=1, body=doc1)
res = es.index(index="test-index", doc_type='tweet', id=2, body=doc2)
res = es.index(index="test-index", doc_type='tweet', id=3, body=doc3)


#print(res['result'])

#res = es.get(index="test-index", doc_type='tweet', id=1)

#print(res['_source'])

es.indices.refresh(index="test-index")

#res = es.search(index="test-index", body={"query": {"match_all": {}}})
res2=es.search(index="test-index", q='PRYF="1984"')
print("Got %d Hits:" % res2['hits']['total'])
for hit in res2['hits']['hits']:
    print(hit)
    #print(hit['_source'])
    print("%(IN.CTY)s %(PRY)s: %(PRYF)s %(TIEN)s" % hit["_source"])