import json

    # Fonction crée par Tournier Quentin et Marche Jules
    # But: Récuperer un film via son id
    # En entrée: racine de l'objet, info, _id
    #En sortie: L'objet Movie demandé
def movie_with_id(_,info,_id):
    with open('{}/data/movies.json'.format("."), "r") as file:
        movies = json.load(file)
        for movie in movies['movies']:
            if movie['id'] == _id:
                return movie

    # Fonction crée par Tournier Quentin et Marche Jules
    # But: Resoudre le type 'Actor' lorsqu'il se trouve dans un objet Movie
    # En entrée: racine de l'objet, info
    #En sortie: liste des acteurs du film se trouvant a la racine
def resolve_actors_in_movie(movie, info):
    with open('{}/data/actors.json'.format("."), "r") as file:
        data = json.load(file)
        actors = [actor for actor in data['actors'] if movie['id'] in actor['films']]
        return actors

    # Fonction crée par Tournier Quentin et Marche Jules
    # But: Recuperer tous les films
    # En entrée: racine de l'objet, info
    #En sortie: tous les films de la bd
def list_movies(_,info):
    with open('{}/data/movies.json'.format("."), "r") as file:
        movies = json.load(file)
        return movies["movies"]

    # Fonction crée par Tournier Quentin et Marche Jules
    # But: mettre a jour la note d'un film
    # En entrée: racine de l'objet, info, _rate
    #En sortie: le film modifie
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

    # Fonction crée par Tournier Quentin et Marche Jules
    # But: Recuperer un film via son titre
    # En entrée: racine de l'objet, info, _title
    #En sortie: film demande
def movie_with_title(_,info,_title):
    with open('{}/data/movies.json'.format("."), "r") as file:
        movies = json.load(file)
        for movie in movies['movies']:
            if movie['title'] == _title:
                return movie

    # Fonction crée par Tournier Quentin et Marche Jules
    # But: Créer un film
    # En entrée: racine de l'objet, _movieInput
    #En sortie: Message notifiant l'ajout ou non du film
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

    # Fonction crée par Tournier Quentin et Marche Jules
    # But: Recuperer un film via son directeur
    # En entrée: racine de l'objet, info, _director
    #En sortie: film demandé
def movie_with_director(_,info,_director):
    with open('{}/data/movies.json'.format("."), "r") as file:
        movies = json.load(file)
        for movie in movies['movies']:
            if movie['director'] == _director:
                return movie

    # Fonction crée par Tournier Quentin et Marche Jules
    # But: supprimer un film
    # En entrée: racine de l'objet, info, _id
    #En sortie: message notifiant la deletion ou non
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
    # Fonction crée par Tournier Quentin et Marche Jules
    # But: recuperer un actor via son id
    # En entrée: racine de l'objet, info, _id
    #En sortie: l'acteur demandé
def actor_with_id(_,info,_id):
    with open('{}/data/actors.json'.format("."), "r") as file:
        actors = json.load(file)
        for actor in actors["actors"]:
            if actor['id'] == _id:
                return actor