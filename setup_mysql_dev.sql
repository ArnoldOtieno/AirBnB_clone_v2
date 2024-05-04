-- Script that prepares MYSQL server for project
CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;
CREATE OR REPLACE USER `hbnb_dev`@`localhost` IDENTIFIED BY `hbnb_test_pwd`;
GRANT USAGE ON *.* TO `hbnb_dev`@`localhost`
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO `hbnb_dev`@`localhost`;
GRANT SELECT ON performance_schema.* TO `hbnb_dev`@`localhost`;
