# Data modeling with Postgres
## Files
- create_tables.py: drops and creates tables. Run this file to reset your tables before each time you run your ETL scripts.
- etl.ipynb: reads and processes a single file from song_data and log_data and loads the data into your tables. This notebook contains detailed instructions on the ETL process for each of the tables.
- etl.py: reads and processes files from song_data and log_data and loads them into your tables. You can fill this out based on your work in the ETL notebook.
- sql_queries.py: contains all your sql queries, and is imported into the last three files above.
- test.ipynb: displays the first few rows of each table to check your database

## How to run?
- Run create_tables.py to create your database and tables
- Run test.ipynb to confirm the creation of your tables with the correct columns. Make sure to click "Restart kernel" to close the connection to the database after running this notebook.
- Running etl.py to reset tables

## Notes
### Discuss the purpose of this database in the context of the startup, Sparkify, and their analytical goals.
- purpose:Model the raw data in JSON format and create song and log datasets
- analytical goals:Find the songs that users listen to most often, find the time when users listen most often, and analyze the listening preferences of different user groups. All of these can help Sparkify better serve users.


### State and justify your database schema design and ETL pipeline.
- The star schema is made up of 5 tables(1 fact table (songplays), and 4 dimension tables (users, songs, artists, time))
- First, DDL(DROP, CREATE, INSERT) and queries(SELECT) are defined in sql_queries.py
- Then,  sparkifydb is created in create_tables.py with functions(create_database, drop_tables, and create_tables to create the database).
- Finaly, run etl.py to reset tables.



![](star.png?raw=true)