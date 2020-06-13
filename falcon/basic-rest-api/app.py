import json, falcon

class ObjRequestClass:
    __json_content = {}


    def __validate_json_input(self, req):
        try:
            self.__json_content = json.loads(req.stream.read())
            print 'json from client validate'
            return True

        except ValueError, e:
            self.__json_content = {}
            print 'json from client not validate'
            return False

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        

        # content = {
        #    'name' : 'kevin',
        #    'kelas' : '2',
        #    'asal' : 'semarang'
        # }
        validated = self.__validate_json_input(req)
        
        output = {
            'status' : 200,
            'msg' : None
        }

        if(validated == True):

            output['msg'] = 'Hello {name}'.format(name=self.__json_content['name'])  
        else:
            output['status'] = 404
            output['msg'] = 'json input is not validated'

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