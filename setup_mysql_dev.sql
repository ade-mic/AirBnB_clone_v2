-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS
hbnb_dev_db;

-- Create a new user 'hbnb_dev'
-- with the password 'hbnb_dev_pwd'
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' 
IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all priviledges on 'hbnb_dev_db' to 'hbnb_dev'
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant  GRANT Priviledes to hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;