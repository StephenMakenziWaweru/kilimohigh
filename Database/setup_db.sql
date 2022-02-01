-- Creates the database hbnb_dev_db with specified paramenters
-- Create database
CREATE DATABASE IF NOT EXISTS kilimohigh;
-- Creates user if doesn't exist
CREATE USER IF NOT EXISTS 'kilimouser'@'localhost';
-- Sets password for user
SET PASSWORD FOR 'kilimouser'@'localhost' = 'kilimo_dev_pwd';
-- Grants privileges to user on database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'kilimohigh'@'localhost';
-- Flush privileges
FLUSH PRIVILEGES;

CREATE TABLE IF NOT EXISTS students (
	id INT,
       first_name VARCHAR(100) NOT NULL,
	last_name VARCHAR(100) NOT NULL,
	date_of_admission ;
	guardian VARCHAR(100) NOT NULL,
	stream_name VARCHAR(100) NOT NULL,
       PRIMARY KEY (`id`),
	CONSTRAINT `streams_ibfk_1` FOREIGN KEY (`stream_name`) REFERENCES `streams` (`stream_name`));

CREATE TABLE IF NOT EXISTS streams (
	id INT PRIMARY KEY,
	stream_name VARCHAR(20));
