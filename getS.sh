#!/bin/bash

curl -s "http://172.20.1.88:8983/solr/colors/select?q=id:$1&fl=id,hue_mea&wt=json&indent=true"
