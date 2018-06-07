import os
import sys
from elasticsearch import Elasticsearch, helpers
import sys, json
from os import listdir
import subprocess
from elasticsearch import Elasticsearch
import os
#subprocess.Popen('C:/Users/Noushin/Downloads/elasticsearch-6.2.4/elasticsearch-6.2.4/bin/elasticsearch.bat')
es = Elasticsearch()
#es.reindex
#es.indices.refresh(index="myindex")
#es.indices.create(index='myindex')
#es.indices.delete(index='myindex', ignore=[400, 404])