from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

names = {"Kyle": {"age": 38, "gender": "male"},
         "Jessica": {"age": 39, "gender": "female"}}

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Number of views the video has is required", required=True)
video_put_args.add_argument("likes", type=int, help="Number of likes the video has is required", required=True)

videos = {}

def abort_if_video_id_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404, message="Fuck you")

class HelloWorldByName(Resource):
    def get(self, name):
        return names[name]
    
    def post(self):
        return {"data": "Posted"}
    
class HelloWorld(Resource):
    def get(self):
        return names
    
class Video(Resource):
    def get(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        return videos[video_id]
    
    def put(self, video_id):
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201
    
api.add_resource(HelloWorldByName, "/helloworld/<string:name>")
api.add_resource(HelloWorld, "/helloworld")
api.add_resource(Video, "/video/<int:video_id>")


if __name__ == "__main__":
    app.run(debug=True)