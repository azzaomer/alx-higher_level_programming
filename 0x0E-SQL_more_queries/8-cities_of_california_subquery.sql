-- script that lists all the cities of California that can be found in the database
SELECT id, name FORM cities WHERE state_id = (SELECT id FROM states WHERe name = 'California') ORDER BY id ASC;
