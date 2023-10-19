-- lists all the cities of California that can be found in the database hbtn_0d_usa
-- Results must be sorted in ascending order by cities.id
USE hbtn_0d_usa;
SELECT id, name FROM cities
  WHERE state_id = 1
  ORDER BY id;
