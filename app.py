from flask import Flask # type: ignore
from flask_restful import Api, Resource, request # type: ignore

app = Flask(__name__)
api = Api(app)


class Devil(Resource):
    def get(self):
        return {"message":"Hey Buddy"}
api.add_resource(Devil, '/')


class Shadow(Resource):
    list =  []
    def post(self):
        x = request.get_json()
        print(x.get("Message"))
        # # x = x.Message
        # list.append(str(x.get("Message")))
        return "hi"
api.add_resource(Shadow, '/post')
if __name__ == '__main__':  
    app.run(debug=True , port=5006) 