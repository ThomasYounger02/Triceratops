# Data modeling with Cassandra
## Files
- event_data: the original dataset
- images: data appearance
- event_datafile_new.csv:
- Project_1B_Project_Template.ipynb: Extract data, Connect to database, Create table, Insert data, use SELECT statement to find insights.

## Build ETL Pipeline
- CREATE keyspace
- INSERT data
- write SELECT statement and run it

## Notification
- Include IF NOT EXISTS clauses in your CREATE statements to create tables only if the tables do not already exist
- include DROP TABLE statement for each table, this way you can run drop and create tables whenever you want to reset your database and test your ETL pipeline