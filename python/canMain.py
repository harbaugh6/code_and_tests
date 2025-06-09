from flask import Flask, request, jsonify
from flask_restful import Api, Resource, abort, reqparse

app = Flask(__name__)
api = Api(app)

# Example data, this will eventually be removed but is
# present for testing purposes right now
teams = {1: {"team": "Washington", "mascot": "Huskies"},
         2: {"team": "Villanova", "mascot": "Wildcats"}}
# teams = {}

schedule = [
    {
        "game_id": 1,
        "home_team": "Washington",
        "away_team": "Villanova",
        "date": "07/12/2025",
        "time": "9:00am",
        "location": "West Potomac Park",
        "field": "Field 5",
        "home_score": None,
        "away_score": None
    },
    {
        "game_id": 2,
        "home_team": "Washington",
        "away_team": "Georgetown",
        "date": "07/12/2025",
        "time": "10:30am",
        "location": "West Potomac Park",
        "field": "Field 5",
        "home_score": None,
        "away_score": None
    }
]


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
# Upload Schedule
# Get entire schedule

class Schedule(Resource):
    # Endpoints belonging to this class will be the GET schedule,
    # which will get the entire schedule for viewing.  PUT/POST
    # will create the schedule and allow for mass updates.  DELETE
    # will allow us to nuke the schedule if necessary
    def get(self):
        return schedule, 200

# Get team schedule
class GetScheduleByTeam(Resource):
    # This class will have the endpoint which retrieves all games by team.
    def get(self, team_name):
        team_games = [
            game for game in schedule
            if game["home_team"].lower() == team_name.lower()
            or game["away_team"].lower() == team_name.lower()
        ]

        if team_games:
            return team_games
        else:
            return {"message": f"No schedule found for {team_name}."}, 404

# Get game
# Update game; can be used to update score, date and location.
class GetGameById(Resource):
    def get(self, game_id):
        for game in schedule:
            if game["game_id"] == game_id:
                return game
        return {"message": f"Game with ID {game_id} cannot be found"}, 404
    
    def put(self, game_id):
        data = request.get_json()

        for game in schedule:
            if game["game_id"] == game_id:
                if "home_score" in data:
                    game["home_score"] = data["home_score"]
                if "away_score" in data:
                    game["away_score"] = data["away_score"]
                if "date" in data:
                    game["date"] = data["date"]
                if "time" in data:
                    game["time"] = data["time"]
                if "location" in data:
                    game["location"] = data["location"]
                if "field" in data:
                    game["field"] = data["field"]
            return game



# Get standings for all teams

# Get division standings

api.add_resource(Teams, '/teams')
api.add_resource(GetTeamById, '/teams/<int:team_id>')
api.add_resource(GetTeamByName, '/teams/<string:team_name>')
api.add_resource(Schedule, '/schedule')
api.add_resource(GetScheduleByTeam, '/schedule/<string:team_name>')
api.add_resource(GetGameById, '/schedule/<int:game_id>')



if (__name__) == "__main__":
    app.run(debug=True)