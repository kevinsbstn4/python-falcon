import json, falcon

class ObjRequestClass:
    def on_get(self, req, resp):
        content = {
           'name' : 'kevin',
           'kelas' : '2',
           'asal' : 'semarang'
        }

        resp.body = json.dumps(content)


api = falcon.API()
api.add_route('/test', ObjRequestClass())