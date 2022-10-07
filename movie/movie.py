from ariadne import graphql_sync, make_executable_schema, load_schema_from_path, ObjectType, QueryType, MutationType
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, request, jsonify, make_response

import resolvers as r

PORT = 5000
HOST = 'localhost'
app = Flask(__name__)

### ADD THINGS HERE

type_defs = load_schema_from_path('movie.graphql')

# GRAPHQL_TYPES
query = QueryType()
mutation = MutationType()

# MY_TYPES
movie = ObjectType('Movie')
actor = ObjectType('Actor')

# MOVIE_WITH_ID
query.set_field('movie_with_id', r.movie_with_id)

# ACTOR_WITH_ID
query.set_field('actor_with_id', r.actor_with_id)

# UPDATE_MOVIE_RATE
mutation.set_field('update_movie_rate', r.update_movie_rate)

# ASSOCIATION ACTOR IN MOVIE
movie.set_field('actors', r.resolve_actors_in_movie)



# SCHEMA ASSOCIATION
schema = make_executable_schema(type_defs, movie, query, mutation, actor)

###

# root message
@app.route("/", methods=['GET'])
def home():
    return make_response("<h1 style='color:blue'>Welcome to the Movie service!</h1>",200)

#####
# graphql entry points

@app.route('/graphql', methods=['GET'])
def playground():
    return PLAYGROUND_HTML, 200
    
@app.route('/graphql', methods=['POST'])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
                        schema,
                        data,
                        context_value=None,
                        debug=app.debug
                    )
    status_code = 200 if success else 400
    return jsonify(result), status_code

if __name__ == "__main__":
    print("Server running in port %s"%(PORT))
    app.run(host=HOST, port=PORT)
