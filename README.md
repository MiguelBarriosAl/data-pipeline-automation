<h1 align="center"> Data Pipeline </h1>

 <p align="left">
   <img src="https://img.shields.io/badge/STATUS-%20DEV-green">
</p>

# Introduction
Project consists of implementing a tool that is able to analyze files containing position of all vehicles in its fleet 
in real-time via a GPS sensor in each vehicle. These vehicles run in operating periods that are managed by door2door’s 
operators. Therefore it is separated into Chunks with a choice of size.

Using chunks in a data pipeline in Python can have several advantages when reading JSON files and storing them in a local 
database.

* Memory efficiency: Processing large JSON files can consume a lot of memory, but using chunks allows for processing smaller 
pieces of the data at a time, reducing memory usage.

* Speed: Processing large files in chunks can also make the pipeline faster, as it can begin processing and storing data 
it is still being read.

* Resilience: If the pipeline encounters an error while processing a chunk, it can continue with the next chunk, rather 
  than stopping the entire pipeline. This can make the pipeline more resilient to errors and allow for more efficient processing.

* Able to handle large datasets: when reading large datasets, the chunking allows to handle them in smaller pieces which
can make it easier to store and process them.

* Error handling: if there is an error in the data, it can be handled with a smaller set of data instead of the entire dataset.

The project consists of the following files:

### src/*

- **src/main.py:** Initial execution of data processing
- **src/constant.py:** Pipeline configuration constants. With the constants you can set the number of batches and chunks that 
best fit the project, thus making it more scalable. with the constants you can set the number of batches and chunks that best fit the project, thus making it more scalable.
It also makes it possible to schedule a daily execution through the DATE constant. A possible solution could be to include 
**crontab** and include in the date variable the current date for the execution of specific files.
- **src/data:** Local json files

### src/database/*

- **src/database/connector:** Database connection object and execution of queries
- **src/database/query:** Development of all the queries to execute in mysql database

### src/app/*
- **src/app/pipeline.py:** Pipeline object that executes the different data load depending on its configuration
- **src/app/checkers.py:** Data input supervision functions for data processing and loading into the database
- **src/app/data_extract_files.py:** Loading data into chunks
- **src/app/data_transformer_db.py:** Data processing and load in Mysql database
- **src/app/utils.py:** Complementary functions for the smooth operation of the pipeline
- **src/app/logs.py:**: Logging of operations during application operation

### tests/*

- **tests/***: Running of Unit Tests

### Dockerfile
- Set of commands for to set up a MySQL server. The first line specifies that the image being used is "mysql/mysql-server". 
The next lines use the ENV command to set environment variables for the database name, root password, and root host. 
The next line uses the ADD command to add a file called "schema.sql" to the "/docker-entrypoint-initdb.d" directory. 
Finally, the last line uses the EXPOSE command to make port 3306 available to the host

### schema.sql
SQL script that creates three tables in a MySQL database named "door2door".

The first table named "events" has six columns: id, file, event, on_event, at_event and organization_id. The "id" column 
is set as the primary key and is unique and not null.

The second table named "vehicles" has five columns: id_event, id_vehicle, lat, lng and at_vehicle. The "id_event" column 
is set as a foreign key referencing the "id" column in the "events" table and on delete it is set to cascade.

The third table named "operating_period" has five columns: id_event, id_operating, start, finish and on_finish. 
The "id_event" column is set as a foreign key referencing the "id" column in the "events" table and on delete it is set to cascade.

These commands create the structure of the database and the relationships between the tables, so that data can be inserted 
and queried in a logical and consistent way.

# Requirements

- SO == Windows 10
- Python == 3.9.7
- Pip == 21.3.1

# Installation and Run

Install python==3.9

        sudo apt update

        sudo apt install python3.9.7

        python --version

Clone the repository

        git clone https://github.com/MiguelBarriosAl/data-pipeline-automation.

Create file `.env:` with enviroment variables:

*   DB_ADDRESS=*****
*   DB_PASS=*****
*   DB_DATABASE=*****
*   DB_USER=*****

  Docker run Database:
  

    docker build -t <name> . 

    docker run -dp 3306:3306 --env-file .env <name>

* Run Pipeline

`python .\src\main.py`

* Tests Database

`  docker exec -it <container_id> bash`

    mysql -h 127.0.0.1 -p

    Use door2door

    SELECT * FROM events JOIN operating_period ON events.id = operating_period.id_event WHERE operating_period.start >= '2015-01-01' AND operating_period.start <= '2022-12-31';


# Conclusion

For this project I did not want to make use of excessive libraries or third party services, but to focus the solution 
from the management of data.
In case you want to speed up the process by reducing execution times, you could multithread the process
It could also be interesting to add a log system for those chunks that have not been able to load the data to the database, 
so that the process could continue loading the other data without losing the record of those that have not been loaded.







