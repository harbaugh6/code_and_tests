from flask import Flask, request, jsonify
from flask_restful import Api, Resource, abort, reqparse
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
import pandas as pd

app = Flask(__name__)
api = Api(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:uraCAT4$@localhost:3306/canleague"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Team(db.Model):
    __tablename__ = "teams"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    mascot = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "mascot": self.mascot
        }

class Game(db.Model):
    __tablename__ = "games"

    id = db.Column(db.Integer, primary_key=True)
    home_team_id = db.Column(db.Integer, db.ForeignKey("teams.id"), nullable=False)
    away_team_id = db.Column(db.Integer, db.ForeignKey("teams.id"), nullable=False)
    date = db.Column(db.String(20))
    time = db.Column(db.String(20))
    location = db.Column(db.String(100), nullable=False)
    field = db.Column(db.String(50), nullable=False)
    home_score = db.Column(db.Integer, nullable=True)
    away_score = db.Column(db.Integer, nullable=True)

    # Relationships
    home_team = db.relationship("Team", foreign_keys=[home_team_id])
    away_team = db.relationship("Team", foreign_keys=[away_team_id])

    def to_dict(self):
        return {
            "id": self.id,
            "home_team": self.home_team.name if self.home_team else None,
            "away_team": self.away_team.name if self.away_team else None,
            "date": self.date,
            "time": self.time,
            "location": self.location,
            "field": self.field,
            "home_score": self.home_score,
            "away_score": self.away_score
        }

        return new_game.to_dict(), 201

REQUIRED_FIELDS = ["home_team", "away_team", "date", "time", "location", "field"]

# Helper functions
# This function will be used to check if a team exists before performing operations that require a valid team ID.  
# If the team does not exist, it will return a 404 error with an appropriate message.
def require_team(team_id):
    if team_id not in teams:
        abort(404, message="Team does not exist")

# Validates game data to fit the db model.
def validate_game_data(data):
    REQUIRED_FIELDS = ["home_team_id", "away_team_id", "date", "time", "location", "field"]

    missing = [field for field in REQUIRED_FIELDS if field not in data]
    if missing:
        return False, f"Missing fields: {', '.join(missing)}"
    
    try:
        home_id = int(data["home_team_id"])
        away_id = int(data["away_team_id"])
    except ValueError:
        return False, "Team IDs must be integers"

    if home_id == away_id:
        return False, "Home and away teams cannot be the same"
    
    if len(data["date"]) < 8:
        return False, "Invalid date format."

    if len(data["time"]) < 4:
        return False, "Invalid time format."
    
    return True, None


# This function will be used to create a new game object based on the provided data and the existing schedule. 
# It generates a new game ID by finding the maximum existing game ID in the schedule and adding 1. 
# It then constructs a new game dictionary with the provided data and initializes the home_score and away_score to None. 
# The new game object is returned for further processing, such as adding it to the schedule or returning it in a response.
def build_game_from_data(data):
    return Game(
        home_team_id=data["home_team_id"],
        away_team_id=data["away_team_id"],
        date=data["date"],
        time=data["time"],
        location=data["location"],
        field=data["field"],
        home_score=data.get("home_score"),
        away_score=data.get("away_score")
    )


# Teams related endpoints
class Teams(Resource):
    # Get all teams
    def get(self):
        teams = Team.query.all()
        return [team.to_dict() for team in teams], 200
    
    # Create team
    def post(self):
        data = request.get_json()

        if not data or "name" not in data or "mascot" not in data:
          return {"message": "Missing 'name' or 'mascot' in request body"}, 400
        
        # Check if team exists
        existing_team = Team.query.filter_by(name=data["name"]).first()
        if existing_team:
            return {"message": "Team with this name already exists"}, 409
        
        #Create new team
        new_team = Team(name=data["name"], mascot=data["mascot"])

        db.session.add(new_team)
        db.session.commit()

        return new_team.to_dict(), 201
        
    
# Get team by id
class GetTeamById(Resource):
    def get(self, team_id):
        require_team(team_id)
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

# Delete team  <--DELETE
class DeleteTeam(Resource):
    def delete(self, team_id):
        require_team(team_id)
        del teams[team_id]
        return '', 204
        
# TODO
# Schedule related endpoints
# Upload Schedule

# Endpoints belonging to this class will be the GET schedule,
# which will get the entire schedule for viewing.  PUT/POST
# will create the schedule and allow for mass updates.  DELETE
# will allow us to nuke the schedule if necessary
class Schedule(Resource):
    # This endpoint will retrieve the entire schedule.
    def get(self):
        games = Game.query.all()
        return [game.to_dict() for game in games], 200
    
    def post(self):
        # Case 1: JSON
        if request.is_json:
            data = request.get_json()

            is_valid, error = validate_game_data(data or {})
            if not is_valid:
                return {"message": error}, 400
            
            game = build_game_from_data(data)
            db.session.add(game)
            db.session.commit()
            return game.to_dict(), 201
        
        # Case 2: File upload
        if "file" not in request.files:
            return {"message": "No file provided"}, 400
        
        file = request.files["file"]

        try:
            if file.filename.endswith(".csv"):
                df = pd.read_csv(file)
            elif file.filename.endswith((".xls", "xlsx")):
                df = pd.read_excel(file)
            else:
                return {"message": "Unsupported file type"}, 400
        except Exception as e:
            return {"message": "Error processing file"}, 400
        
        created_games = []
        errors = []

        for index, row in df.iterrows():
            data = row.to_dict()

            is_valid, error = validate_game_data(data)
            if not is_valid:
                errors.append({"row": index, "error": error})
                continue

            game = build_game_from_data(data)
            db.session.add(game)
            created_games.append(game)
        
        db.session.commit()

        return {
            "created": [g.to_dict() for g in created_games],
            "errors": errors
        }, 201

# Get team schedule

class GetScheduleByTeam(Resource):
    def get(self, team_name):
        team_name = team_name.lower()

        games = Game.query.join(Team, or_(
            Game.home_team_id == Team.id,
            Game.away_team_id == Team.id
        )).filter(
            Team.name.ilike(team_name)
        ).all()

        if not games:
            return {"message": f"No schedule found for {team_name}."}, 404

        return [game.to_dict() for game in games], 200

# Get game
# Update game; can be used to update score, date and location.
class GetGameById(Resource):
    def get(self, game_id):
        game = Game.query.get(game_id)
        if not game:
            return {"message": "Game not found"}, 404
        return game.to_dict(), 200
    
    def put(self, game_id):
        game = Game.query.get(game_id)
        if not game:
            return {"message": "Game not found"}, 404

        data = request.get_json() or {}
        
        # Update only provided fields
        if "home_score" in data:
            game.home_score = data["home_score"]

        if "away_score" in data:
            game.away_score = data["away_score"]

        if "date" in data:
            game.date = data["date"]

        if "time" in data:
            game.time = data["time"]

        if "location" in data:
            game.location = data["location"]

        if "field" in data:
            game.field = data["field"]

        db.session.commit()

        return game.to_dict(), 200



# Get standings for all teams

# Get division standings

api.add_resource(Teams, '/teams')
api.add_resource(GetTeamById, '/teams/<int:team_id>')
api.add_resource(GetTeamByName, '/teams/<string:team_name>')
api.add_resource(DeleteTeam, '/teams/<int:team_id>')

api.add_resource(Schedule, '/schedule')
api.add_resource(GetScheduleByTeam, '/schedule/<string:team_name>')
api.add_resource(GetGameById, '/schedule/<int:game_id>')



if (__name__) == "__main__":
    with app.app_context():
        # db.drop_all() <-- Uncomment this line if you want to reset the database (WARNING: This will delete all data)
        db.create_all()
    app.run(debug=True)