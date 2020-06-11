import json, falcon

class ObjRequestClass:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        data = json.loads(req.stream.read())

        content = {
           'name' : 'kevin',
           'kelas' : '2',
           'asal' : 'semarang'
        }


        output = {}
        if('method' not in data):
           resp.status = falcon.HTTP_501
           output['value'] = 'tidak ada method'
        else:
            if(data['method'] == 'get-name'): 
                output['value'] = content['name']
            else: 
                resp.status = falcon.HTTP_404
                output['value'] = None
         
        resp.body = json.dumps(output)


api = falcon.API()
api.add_route('/test', ObjRequestClass())