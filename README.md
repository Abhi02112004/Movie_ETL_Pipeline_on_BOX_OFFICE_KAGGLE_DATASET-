 Box Office Movie ETL Project
 Project Overview

This project focuses on extracting, cleaning, transforming, and loading box office movie data into a SQL database. 
The goal is to prepare raw movie data for efficient querying and analysis using Python and SQL.

Dataset
Source: Kaggle Box Office Movie Dataset
Contains information such as:
Movie Title
Genre
Release Date
Budget
Revenue
Runtime
Ratings and other movie-related attributes
🛠️ Tech Stack
Python
Pandas
MySQL
VS Code
ETL Workflow
Extract
Loaded raw movie dataset from CSV files into Pandas DataFrames.
Transform
Removed duplicate records.
Handled missing values.
Converted columns to appropriate data types.
Cleaned and standardized data.
Prepared data for database storage.
Load
Created database tables.
Inserted transformed movie data into MySQL.
Verified successful data loading through SQL queries.
📂 Project Structure
movie-etl-project/
│
├── data
│   └── box_office_movies.csv
│
├── scripts
│   └── extract.py
│   |__transform.py
|   |__load.py
├── database
│   └── movie_database.sql
│
├── README.md
└── requirements.txt
