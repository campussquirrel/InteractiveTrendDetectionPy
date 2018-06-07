import os
import sys
from elasticsearch import Elasticsearch, helpers
import sys, json
from os import listdir
import subprocess
from elasticsearch import Elasticsearch
#subprocess.Popen('C:/Users/Noushin/Downloads/elasticsearch-6.2.4/elasticsearch-6.2.4/bin/elasticsearch.bat')
es = Elasticsearch()
es.reindex
#es.indices.refresh(index="myindex")
#es.indices.create(index='myindex6')
#sys.stdout=open("RESULT.txt","w")
f = open('RESULT', 'a', encoding='utf-8')
i=0
for dirpath, dirs, files in os.walk("TestSamples/Data/"):
    for filename in files:
        fname = os.path.join(dirpath, filename)
        if(fname.endswith("json")):
            with open(fname, encoding="utf8") as myfile:
                print(fname)
                for line in myfile.readlines():
                    if(line.__contains__("{\"index\":{")):
                        continue
                    myres = es.index(index="myindex", doc_type='patent', id=i+1, body=line)
                    i=i+1
                    #f.write(line)

f.write(myres['result'])
f.close()
print(myres['result'])

myres1=es.search(index="myindex",q='PRYF="1986"')
print("Got %d Hits:" % myres1['hits']['total'])
for hit in myres1['hits']['hits']:
    #print(hit)
    #print(hit['_source'])
    print("%(IN.CTY)s %(PRY)s: %(PRYF)s %(TIEN)s" % hit["_source"])
#sys.stdout.close()
