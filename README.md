 Box Office Movie ETL Project 🎬
Project Overview

This project demonstrates the ETL (Extract, Transform, Load) process using a Box Office Movie Dataset sourced from Kaggle. The objective is to transform raw movie data into a clean, structured format and store it in a MySQL database for efficient querying and analysis.

The project showcases fundamental Data Engineering concepts such as data extraction, preprocessing, data cleaning, transformation, and database loading using Python and SQL.

Dataset

Source: Kaggle Box Office Movie Dataset

The dataset contains information related to movies, including:

Movie Title
Genre
Release Date
Budget
Revenue
Runtime
Ratings
Other movie-related attributes
Tech Stack
Python
Pandas
MySQL
VS Code
ETL Workflow
Extract
Loaded raw movie data from CSV files.
Imported the dataset into Pandas DataFrames for processing.

Transform
Removed duplicate records.
Handled missing and inconsistent values.
Converted columns to appropriate data types.
Standardized and cleaned dataset attributes.
Prepared data for database storage.

Load
Created the required database schema and tables.
Loaded the transformed data into MySQL.
Validated successful data insertion using SQL queries.


Project Structure
movie-etl-project/
│
├── data
│   └── box_office_movies.csv
│
├── scripts
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── database
│   └── movie_database.sql
│
├── README.md
└── requirements.txt
