-- script to prepare a MySQL server for the project
-- create hbnb_test_db if ot doesnt exsist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- create hbnb_test_user with password hbnb_test_pwd
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_test_pwd';

-- Grant ll privileges on the databse hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;

-- Grant SELECT privilege on performance_schema to hbnb_test
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- change changes
FLUSH PRIVILEGES;
