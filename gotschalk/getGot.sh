#!/bin/bash

curl http://solr-02.smk.dk:8080/solr/prod_SAFO/select?q=artist_name:*$1*\&wt=csv\&indent=true\&rows=$2\&fl=id,medium_image_url,object_production_date_earliest,artist_name,title_dk,acq_date,object_production_date_latest -s
