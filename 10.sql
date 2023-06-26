SELECT DISTINCT name FROM people JOIN directors
ON directors.person_id = people.id
WHERE movie_id IN (SELECT id FROM movies JOIN ratings
ON movies.id = ratings.movie_id WHERE ratings.rating >= 9.0)