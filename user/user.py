from flask import Flask, render_template, request, jsonify, make_response
import requests
import json

app = Flask(__name__)

PORT = 3004
HOST = 'localhost'

with open('{}/data/users.json'.format("."), "r") as jsf:
   users = json.load(jsf)["users"]

@app.route("/get-movies-infos-of-selected-movies-by-userid/<userid>", methods=['GET'])
def get_movies_infos_of_selected_movies_by_userid(userid):
   moviesInfos = json.loads('{"movies": []}')
   for user in users:
      if str(user["id"]) == str(userid):
         booking = requests.get("http://localhost:3003/bookings/" + userid)

   if not 'booking' in locals():
      return make_response(jsonify({"error": "user for this userid not found"}), 400)

   if booking.status_code != 200:
      return make_response(jsonify({"error": "this userid doesn't have bookings"}), 400)

   for date in booking.json()["dates"]:
      for movieid in date["movies"]:
         query = """
         {movie_with_id(_id: \""""+  movieid + """\")
            {
               id
               title
               rating
               director
            }
         }"""
         movie = requests.post("http://localhost:5000/graphql",json={'query': query})
         moviesInfos["movies"].append(movie.json())

   return make_response(jsonify(moviesInfos), 200)

if __name__ == "__main__":
   print("Server running in port %s"%(PORT))
   app.run(host=HOST, port=PORT)
