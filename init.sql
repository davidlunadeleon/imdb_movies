CREATE TABLE IF NOT EXISTS movies (
    movie_id serial PRIMARY KEY,
    preference_key INTEGER NOT NULL,
    movie_title VARCHAR NOT NULL,
    rating DOUBLE NOT NULL,
    year INTEGER NOT NULL,
    created_at DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS users (
	created_at DATE NOT NULL,
	password_hash bytea NOT NULL,
	preference_key INTEGER NOT NULL,
	user_id serial PRIMARY KEY,
	username VARCHAR NOT NULL UNIQUE
)
