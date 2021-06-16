CREATE DATABASE IF NOT EXISTS dbgama_academy;

USE dbgama_academy;

CREATE TABLE IF NOT EXISTS  `Countries` (
	`country_name` varchar(50) NOT NULL,
    `slug` varchar(255) NOT NULL,
	`country_code` varchar(2) NOT NULL,
	PRIMARY KEY (`country_name`)
);

CREATE TABLE IF NOT EXISTS `Cases_covid` (
	`cases_covid_id` int NOT NULL AUTO_INCREMENT,
	`country_name` varchar(50) NOT NULL,
	`province_name` varchar(50),
	`lat` FLOAT(10,2) NOT NULL,
	`long` FLOAT(10,2) NOT NULL,
	`confirmed` int NOT NULL,
	`deaths` int NOT NULL,
	`recovered` int NOT NULL,
	`active` int NOT NULL,
	`date` DATE NOT NULL,
	PRIMARY KEY (`cases_covid_id`)
);

ALTER TABLE `Cases_covid` ADD CONSTRAINT `Cases_covid_fk0` FOREIGN KEY (`country_name`) REFERENCES `Countries`(`country_name`);
