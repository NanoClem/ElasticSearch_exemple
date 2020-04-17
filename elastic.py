import json
import settings as stg
from elasticsearch import Elasticsearch


client = Elasticsearch(
    cloud_id=stg.CLOUD,
    http_auth=(stg.HOST, stg.PASSWORD),
    verify_certs=False
)


if __name__ == "__main__":
    
    filename = stg.DATASET

    with open(filename) as json_file:
        data = json.load(json_file)     # loading dataset
        for k,v in data.items():
            try:
                del data[k]['id']   # removing useless key
                res = client.index(index='xhamster', body=v)    # post data to index
                print( json.dumps(res, indent=4) )              # show results
            except KeyError as e:
                print('Key {} not found'.format(e))