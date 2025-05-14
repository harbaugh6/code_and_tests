from flask import Flask, request, jsonify
from flask_restful import Api, Resource, abort, reqparse

app = Flask(__name__)
api = Api(app)

# Example data, this will eventually be removed but is
# present for testing purposes right now
teams = {1: {"team": "Washington", "mascot": "Huskies"},
         2: {"team": "Villanova", "mascot": "Wildcats"}}
# teams = {}

def team_does_not_exist(team_id):
    if team_id not in teams:
        abort(404, message="Team does not exist")

# Teams related endpoints
class Teams(Resource):
    # Get all teams
    def get(self):
        return teams, 200
    
    # Create team
    def put(self):
        data = request.get_json()
        if not data or "name" not in data or "mascot" not in data:
          return {"message": "Missing 'name' or 'mascot' in request body"}, 400
        
        team_name = data["name"]
        
        # Check if team already exists
        for _, team_info in teams.items():
            if team_info["team"].lower() == team_name.lower():
                return {"message": "Team already exists"}, 409
        
        # If the team doesn't exist, create a new team
        new_id = max(teams.keys(), default = 0) + 1
        teams[new_id] = {
            "team": team_name,
            "mascot": data["mascot"]
        }
        return teams[new_id], 201
    
# Get team by id
class GetTeamById(Resource):
    def get(self, team_id):
        team_does_not_exist(team_id)
        return teams[team_id], 200

class GetTeamByName(Resource):
    # Get team by team name
    def get(self, team_name):
        for team in teams.values():
            if team["team"].lower() == team_name.lower():
                return team
        return {"message": "Team not found"}, 404
    
    # Update team
    def put(self, team_name):
        data = request.get_json()
        team_name = data["name"]
        for team_id, team_info in teams.items():
            if team_info["team"].lower() == team_name.lower():
                teams[team_id]["mascot"] = data["mascot"]
                return {"message": "Team updated", "team": [team_id]}, 200

# TODO
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
api.add_resource(GetTeamByName, '/teams/<string:team_name>')



if (__name__) == "__main__":
    app.run(debug=True)