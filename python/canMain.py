from flask import Flask, request, jsonify
from flask_restful import Api, Resource, abort, reqparse

app = Flask(__name__)
api = Api(app)

# Example data
teams = {1: {"team": "Washington", "mascot": "Huskies"},
         2: {"team": "Villanova", "mascot": "Wildcats"}}
# teams = {}

def team_does_not_exist(team_id):
    if team_id not in teams:
        abort(404, message="Team does not exist")

team_args = reqparse.RequestParser()
team_args.add_argument("team", type=str, help="Team name is required", required=True)

# Teams related endpoints
# Get all teams
class Teams(Resource):
    def get(self):
        return teams, 200
    
    def put(self, team_id):
        args = team_args.parse_args()
        teams[team_id] = args
        return teams[team_id], 201

    
# Get team by id
class GetTeamById(Resource):
    def get(self, team_id):
        team_does_not_exist(team_id)
        return teams[team_id], 200

# Create team  <--POST

# Update team  <--PUT

# Delete team  <--DELETE

# Schedule related endpoints
# Upload schedule <---biggest lift
# Get entire schedule
# Get team schedule
# Update schedule with score  <----put method
# Update schedule with location <---put method
# Get standings for all teams
# Get division standings

api.add_resource(Teams, '/teams')
api.add_resource(GetTeamById, '/teams/<int:team_id>')



if (__name__) == "__main__":
    app.run(debug=True)