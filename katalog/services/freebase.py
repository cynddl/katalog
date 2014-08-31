import json
import requests


def find_by_imdb_id(id):
    service_url = "https://www.googleapis.com/freebase/v1/mqlread?query=%s"
    params = [{
        'type': '/film/film',
        '/imdb/topic/title_id': id,
        'id': None,
        'genre': [],
        "limit": 1
    }]
    params_json = json.dumps(params)

    r = requests.get(service_url % params_json)

    if r.status_code == 200:
        result = json.loads(r.content.decode('utf-8'))['result'][0]
        return {'genre': result['genre'],
                'freebase_id': result['id']}
    else:
        return None
