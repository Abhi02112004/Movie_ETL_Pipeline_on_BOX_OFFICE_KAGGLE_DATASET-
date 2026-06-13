CREATE DATABASE movie_db;
USE movie_db;

DROP TABLE movie_records;

CREATE TABLE movie_records(
ranking INT PRIMARY KEY,
title VARCHAR(30) NOT NULL,
worldwide_lifetime_gross INT,
domestic_lifetime_gross INT,
domestic_percentage FLOAT,
foreign_lifetime_gross INT,
foreign_percentage INT,
years VARCHAR(10),
movie_age INT,
gross_in_crores DECIMAL(20,10)
);
