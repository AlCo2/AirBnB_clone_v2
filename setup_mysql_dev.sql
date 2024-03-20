--script that prepares a MySQL server for the project
CREATE DATABASE IF NOT EXIST `hbnb_dev_db`;
CREATE USER IF NOT EXIST 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGE ON hbnb_dev_db TO 'hbnb_dev'@'localhost';
GRANT SELECT PRIVILEGE ON performance_schema TO 'hbmb_dev'@'localhost';
