# 🎬 Box Office Movie ETL Project

# Overview

This project demonstrates the ETL (Extract, Transform, Load) process using a Box Office Movie Dataset sourced from Kaggle. The objective is to convert raw movie data into a clean, structured format and load it into a MySQL database for efficient storage, querying, and analysis.

The project highlights core Data Engineering concepts including data extraction, preprocessing, cleaning, transformation, and database integration using Python and SQL.


# Dataset

**Source:** Kaggle – Box Office Movie Dataset

**Dataset Size:** 800+ Movie Records

The dataset contains movie-related information such as:

* Movie Title
* Genre
* Release Date
* Budget
* Revenue
* Runtime
* Ratings
* Production Details
* Additional Movie Attributes

---

# Tech Stack

* Python
* Pandas
* MySQL
* VS Code



## ETL Workflow

### Extract

* Imported raw movie data from CSV files.
* Loaded the dataset into Pandas DataFrames for processing and analysis.

### Transform

* Removed duplicate records.
* Handled missing and inconsistent values.
* Standardized column names and formats.
* Converted columns to appropriate data types.
* Performed data cleaning and preprocessing to improve data quality.

### Load

* Created the database schema and tables in MySQL.
* Loaded transformed movie data into the database.
* Validated successful data insertion using SQL queries.

---

## Project Structure

```text
movie-etl-project/
│
├── data/
│   └── box_office_movies.csv
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── database/
│   └── movie_database.sql
│
├── README.md
└── requirements.txt
```

---

## Key Features

* Processed 800+ box office movie records
* Automated data extraction from CSV files
* Cleaned and transformed raw movie data
* Loaded structured data into MySQL
* Improved data quality through preprocessing
* Enabled efficient querying and analysis

---

## Skills Demonstrated

* ETL Fundamentals
* Data Cleaning and Transformation
* Python Programming
* Pandas
* SQL
* MySQL Database Management
* Data Preprocessing
* Data Engineering Basics

---

## Future Enhancements

* Automate the ETL workflow using scheduling tools
* Add data validation and quality checks
* Integrate data visualization dashboards
* Extend support for multiple movie datasets

---

## Project Outcome

Successfully transformed and loaded 800+ box office movie records into a MySQL database, creating a structured dataset suitable for analysis and reporting. The project provided hands-on experience with ETL processes and strengthened practical Data Engineering skills.

---


**Abhinav Tiwari**

BCA Student 

GitHub: Abhi02112004

LinkedIn: abhinav02112004

