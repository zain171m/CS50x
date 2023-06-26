SELECT DISTINCT people.name FROM people JOIN
stars ON stars.person_id = people.id
JOIN movies ON stars.movie_id = movies.id
WHERE movies.title IN (SELECT title FROM movies
JOIN stars ON stars.movie_id = movies.id
JOIN people ON stars.person_id = people.id
WHERE people.name = 'Kevin Bacon' AND people.birth = 1958)
AND people.name != 'Kevin Bacon';
