# Import the framework
from flask import Flask, g
from flask_restful import Resource, Api, reqparse


import markdown
import os
import shelve

# Create an instance of Flask
app = Flask(__name__)

# Create the API
api = Api(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("chores.db")
    return db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route("/")
def index():
    """Present some documentation"""
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:

        content = markdown_file.read()

        return markdown.markdown(content)

class ChoreList(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())

        chores = []

        for key in keys:
            chores.append(shelf[key])

        return {'message': 'Success', 'data': chores}, 200

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('identifier', required=True)
        parser.add_argument('name', required=True)
        parser.add_argument('description', required=True)
        parser.add_argument('repeating', required=True)

        # Parse the arguments into an object
        args = parser.parse_args()

        shelf = get_db()
        shelf[args['identifier']] = args

        return {'message': 'Chore created', 'data': args}, 201

class Chore(Resource):
    def get(self, identifier):
        shelf = get_db()

        if not (identifier in shelf):
            return {'message' : 'Chore not found', 'data':{}}, 404
        return {'message' : 'Chore found', 'data': shelf[identifier]}, 200

    def delete(self, identifier):
        shelf = get_db()

        if not (identifier in shelf):
            return {'message' : 'Chore not found', 'data':{}}, 404

        del shelf[identifier]
        return '', 204
        

api.add_resource(ChoreList, '/chores')
api.add_resource(Chore, '/chore/<string:identifier>')
