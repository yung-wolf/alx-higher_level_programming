-- lists all the cities of California that can be found in the database hbtn_0d_usa
-- results must be sorted in ascending order by cities.id
SELECT cities.id, cities.name
FROM cities
  JOIN states
WHERE states.name = 'California' AND cities.state_id = states.id
ORDER BY cities.id;
