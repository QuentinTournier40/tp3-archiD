import json

def movie_with_id(_,info,_id):
    with open('{}/data/movies.json'.format("."), "r") as file:
        movies = json.load(file)
        for movie in movies['movies']:
            if movie['id'] == _id:
                return movie

def resolve_actors_in_movie(movie, info):
    with open('{}/data/actors.json'.format("."), "r") as file:
        data = json.load(file)
        actors = [actor for actor in data['actors'] if movie['id'] in actor['films']]
        return actors

def list_movies(_,info):
    with open('{}/data/movies.json'.format("."), "r") as file:
        movies = json.load(file)
        return movies["movies"]

def update_movie_rate(_,info,_id,_rate):
    newmovies = {}
    newmovie = {}
    with open('{}/data/movies.json'.format("."), "r") as rfile:
        movies = json.load(rfile)
        for movie in movies['movies']:
            if movie['id'] == _id:
                movie['rating'] = _rate
                newmovie = movie
                newmovies = movies
    with open('{}/data/movies.json'.format("."), "w") as wfile:
        json.dump(newmovies, wfile)
    return newmovie

def movie_with_title(_,info,_title):
    with open('{}/data/movies.json'.format("."), "r") as file:
        movies = json.load(file)
        for movie in movies['movies']:
            if movie['title'] == _title:
                return movie

def create_movie(_,info, _movieInput):
    with open('{}/data/movies.json'.format("."), "r") as file:
        movies = json.load(file)

    for movie in movies["movies"]:
        if _movieInput["id"] == movie["id"]:
            return {"message": "movieid already exist"}

    with open('{}/data/movies.json'.format("."), "w") as wfile:
        movies["movies"].append(_movieInput)
        json.dump(movies, wfile)
    return {"message": "movie added"}

def movie_with_director(_,info,_director):
    with open('{}/data/movies.json'.format("."), "r") as file:
        movies = json.load(file)
        for movie in movies['movies']:
            if movie['director'] == _director:
                return movie

def delete_movie(_,info,_id):
    with open('{}/data/movies.json'.format("."), "r") as file:
        movies = json.load(file)
    for movie in movies["movies"]:
        if movie["id"] == _id:
            movies["movies"].pop(movies["movies"].index(movie))
            with open('{}/data/movies.json'.format("."), "w") as wfile:
                json.dump(movies, wfile)
            return {"message": "movie deleted"}
    return {"message": "error, movieid not found"}


# ---------------------------------------------------------------------
def actor_with_id(_,info,_id):
    with open('{}/data/actors.json'.format("."), "r") as file:
        actors = json.load(file)
        for actor in actors["actors"]:
            if actor['id'] == _id:
                return actor