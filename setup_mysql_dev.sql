-- Script that prepares MYSQL server for project
CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;
CREATE USER IF NOT EXISTS `hbnb_dev`@`localhost` IDENTIFIED BY `hbnb_test_pwd`;
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO `hbnb_dev`@`localhost`;
FLUSH PRIVILEGES;
GRANT SELECT ON performance_schema.* TO `hbnb_dev`@`localhost`;
FLUSH PRIVILEGES;
