import os
import sys
from elasticsearch import Elasticsearch, helpers
import sys, json
from os import listdir
import subprocess
from elasticsearch import Elasticsearch
#subprocess.Popen('C:/Users/Noushin/Downloads/elasticsearch-6.2.4/elasticsearch-6.2.4/bin/elasticsearch.bat')
es = Elasticsearch()
#es.reindex
es.indices.refresh(index="myindex1")
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
                    if not dataObject["DETD"]:
                        continue

                    my_json = {item: dataObject[item] for item, dataObject[item] in dataObject.items() if not "." in item and not "FR" in item and not "ABDE" in item and not "INA" in item}
                    myres = es.index(index="myindex1", doc_type='patent', id=i, body=json.dumps(my_json))
                    i = i + 1
                    print("Indexed DETD: {}".format(i))
                    print(dataObject["DETD"])

                   #f.write(line)


f.write(myres['result'])
f.close()
#print(myres['result'])
#num=0
myres1=es.search(index="myindex1",q='PRYF="2003"',size="10000")
print("Got %d Hits:" % myres1['hits']['total'])
#for hit in myres1['hits']['hits']:
    #num=num+1
    #print(hit)
    #print(hit['_source'])
    #print("%(PRY)s: %(PRYF)s %(TIEN)s" % hit["_source"])
#sys.stdout.close()
#print(num)