
<h1 align="center"> Data Pipeline </h1>

 <p align="left">
   <img src="https://img.shields.io/badge/STATUS-%20DEV-green">
</p>

# Introduction
Project consists of implementing a tool that is able to analyze files containing position of all vehicles in its fleet 
in real-time via a GPS sensor in each vehicle. These vehicles run in operating periods that are managed by door2door’s 
operators. Therefore it is separated into Chunks with a choice of size.
The project consists of the following file packages:

### src/*
- src/main.py: Initial execution of data processing
- src/constant.py: Pipeline configuration constants
- src/data: Local json files

### src/database/*
- src/database/connector: Database connection object and execution of queries
- src/database/query: Development of all the queries to execute in mysql database

### src/app/*
- src/app/pipeline.py: Pipeline object that executes the different data load depending on its configuration
- src/app/checkers.py: Data input supervision functions for data processing and loading into the database
- src/app/data_extract_files.py: Loading data into chunks
- src/app/data_transformer_db.py: Data processing and load in Mysql database
- src/app/utils: Complementary functions for the smooth operation of the pipeline

### tests/*
- tests/*: Running of Unit Tests


# Requirements
- SO == Windows 10
- Python == 3.9.7
- Pip == 21.3.1

# Installation and Run

- Install python==3.9.7

        sudo apt update

        sudo apt install python3.9.7

        python --version

- Clone the repository

        git clone https://github.com/MiguelBarriosAl/data-pipeline-automation.git

- Run Unit Test

         

- Run Pipeline
        
         


# Recommendations

