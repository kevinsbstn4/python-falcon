import json, falcon

class ObjRequestClass:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        data = json.loads(req.stream.read())

        # content = {
        #    'name' : 'kevin',
        #    'kelas' : '2',
        #    'asal' : 'semarang'
        # }


        output = {
            'msg' : 'Hello {0}'.format(data['method'])
        }

        resp.body = json.dumps(output)

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200

        data = json.loads(req.stream.read())

        equal = int(data['x']) + int(data['y']) 

        output = {
            'msg' : 'x: {x} + y: {y} is equal to {e}'.format(x=data['x'],y=data['y'],e=equal) 
        }

        resp.body = json.dumps(output)
    def on_put(self, req, resp):
        resp.status = falcon.HTTP_200

        output = {
            'msg' : 'tidak terdapat put disini :('
        }

        resp.body = json.dumps(output)

    def on_delete(self, req, resp):
        resp.status = falcon.HTTP_200

        output = {
            'msg' : 'tidak terdapat delete disini'
        }

        resp.body = json.dumps(output)

api = falcon.API()
api.add_route('/test', ObjRequestClass())