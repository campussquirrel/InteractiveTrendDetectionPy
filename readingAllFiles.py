import os
import sys
from elasticsearch import Elasticsearch, helpers
import sys, json
from os import listdir
import subprocess
from elasticsearch import Elasticsearch
import requests
#subprocess.Popen('C:/Users/Noushin/Downloads/elasticsearch-6.2.4/elasticsearch-6.2.4/bin/elasticsearch.bat')
es = Elasticsearch()
#es.reindex
#es.indices.refresh(index="myindex1")
#es.indices.create(index='myindex6')
#sys.stdout=open("RESULT.txt","w")
f = open('RESULT', 'a', encoding='utf-8')
i=0
count=0
#data=[]
for dirpath, dirs, files in os.walk("Data/"):
    for filename in files:
        fname = os.path.join(dirpath, filename)
        if(fname.endswith("json")):
            with open(fname, encoding="utf8") as myfile:
                print(fname)
                #data = json.load(myfile)
                for line in myfile.readlines():
                    if(line.__contains__("{\"index\":{")):
                        continue
                    dataObject=json.loads(line)
                    #Filtering patents
                    if ("A1" != str(dataObject["PK"]) and "A2" != str(dataObject["PK"])) or (not dataObject["DETD"]) or (dataObject["LA"] != "en (English)"):#or int(dataObject["AY"][0]) < 2007:
                        continue
                    #if "2003"!= str(dataObject["PRYF"][0]):
                     #   print("It was this year: "+dataObject["PRYF"][0])
                    #fields to be included in json output
                    my_json = {item: dataObject[item] for item, dataObject[item] in dataObject.items() if not "." in item and not "FR" in item and not "ABDE" in item and not "INA" in item}
                    indexed_res = es.index(index="myindex1", doc_type='patent', id=i, body=json.dumps(my_json))
                    i = i + 1
                    print(my_json["PK"])
                    print(my_json["AY"][0])

                   #f.write(line)
print(i)
#print(myres['result'])
#print(es.indices.get_mapping(index='myindex1', doc_type='patent'))



num=0
#indexed_res=es.search(index="myindex1",body={"query": {"match": {"TIEN": "EXTRACTING OILS"}}},size="10000")
"""indexed_res=es.search(index="myindex1",body={"query": {"exists": {"field":"TIEN"}}},size="10000")"""



print("%d documents found:" % indexed_res['hits']['total'])
for doc in indexed_res['hits']['hits']:
    print("%s) %s" % (doc['_id'], doc['_source']['TIEN']))


""""print("Got %d Hits:" % indexed_res['hits']['total'])
for hit in indexed_res['hits']['hits']:
    num=num+1
    #print(hit)
    #print(hit['_source'], file=f)
    #print("%(AY)s: %(PRYF)s %(TIEN)s" % hit["_source"])
#sys.stdout.close()
f.close()
print(num)"""