# Programming for Data Science with Python - Udacity

- [Programming for Data Science with Python - Udacity](#programming-for-data-science-with-python---udacity)
  - [Project 01 - SQL](#project-01---sql)
    - [Project Overview](#project-overview)
    - [Introduction](#introduction)
    - [Dependencies](#dependencies)
    - [Folder Structure](#folder-structure)
    - [How to run the script](#how-to-run-the-script)
  - [Project 02 - Python](#project-02---python)
    - [Project Overview](#project-overview-1)
    - [Tools or Dependencies](#tools-or-dependencies)
    - [Folder Structure](#folder-structure-1)
    - [How to run the script](#how-to-run-the-script-1)


## Project 01 - SQL

### Project Overview

In this project, you will use SQL to explore a database related to movie rentals. You will write SQL code to run SQL queries and answer interesting questions about the database. As part of your project submission, you will run SQL queries and build visualizations to showcase the output of your queries.

We will begin by getting familiar with the database. We have included Practice Quizzes that include a series of questions that will assure you have mastered the main concepts taught throughout the SQL lessons. These practice quizzes will not be "graded" by a reviewer, but they will help you self-assess and make sure you are on the right track. The quizzes are there to assist you in understanding the database before developing the questions that you wish to include for the project.

The project submission is a presentation, which will be reviewed, and for which you will need to Meet Expectations to pass. For the presentation component, you will create four slides. Each slide will:

Have a question of interest.
Have a supporting SQL query needed to answer the question.
Have a supporting visualization created using the final data of your SQL query that answers your question of interest.
You will submit your project at the end of the project lessons. Your project will include:

A set of slides with a question, visualization, and small summary on each slide.
A text file with your queries needed to answer each of the four questions.
The essentials of your project submission are discussed on the page labeled as Project Submission.

### Introduction

In this project, you will query the Sakila DVD Rental database. The Sakila Database holds information about a company that rents movie DVDs. For this project, you will be querying the database to gain an understanding of the customer base, such as what the patterns in movie watching are across different customer groups, how they compare on payment earnings, and how the stores compare in their performance. To assist you in the queries ahead, the schema for the DVD Rental database is provided below.

(Note: One quirk you may notice as you explore this "fake" database is that the rental dates are all from 2005 and 2006, while the payment dates are all from 2007. Don't worry about this. )

<img src="https://video.udacity-data.com/topher/2018/September/5ba95d23_dvd-rental-erd-2/dvd-rental-erd-2.png">

Source: 
[http://www.postgresqltutorial.com/postgresql-sample-database/](http://www.postgresqltutorial.com/postgresql-sample-database/)

Supporting Materials:
[DVD Rental ERD 2](https://video.udacity-data.com/topher/2018/September/5ba96b12_dvd-rental-erd-2/dvd-rental-erd-2.pdf)

### Dependencies

To complete this project, the following software requirements apply:

- Download and install PostgreSQL. You can find installation instructions for your operating system here: [PostgreSQL Downloads](https://www.postgresql.org/download/).
- Download and install Azure Data Studio. You can find installation instructions for your operating system here: [Azure Data Studio Installation](https://docs.microsoft.com/en-us/sql/azure-data-studio/download?view=sql-server-ver15).

- Download the DVD Rental database from here: [PostgreSQL Sample Database](http://www.postgresqltutorial.com/postgresql-sample-database/)

- Download PGAdmin from here: [PGAdmin](https://www.pgadmin.org/download/)

### Folder Structure

Go to project-01-sql and you will find the following

```
    ├── set_01
    ├── set_02
    ├── SQL_Project_Submission.pdf
    ├── SQL_Project_Submission.pptx
    ├── SQL_Project_Submission.txt
```

### How to run the script

Open the Azure Data Studio and connect to the database

Execute the queries in the set_01 or set_02 folder

You can execute python script to generate the visualizations

```bash
    python q_*.py
```

## Project 02 - Python

### Project Overview

In this project, you will make use of Python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. You will write code to import the data and answer interesting questions about it by computing descriptive statistics. You will also write a script that takes in raw input to create an interactive experience in the terminal to present these statistics.

### Tools or Dependencies

To complete this project, the following software requirements apply:

- You should have Python 3, NumPy, and pandas installed using Anaconda
- A text editor, like Sublime or Atom.
- A terminal application (Terminal on Mac and Linux or Cygwin on Windows).

<img src="https://video.udacity-data.com/topher/2018/March/5aa7718d_divvy/divvy.jpg">

### Folder Structure

Go to project-02-python folder and you will find the following:

```bash
    ├── bikeshare_2.py
    ├── chicago.csv
    ├── new_york_city.csv
    └── washington.csv
```

### How to run the script

Download the data from the following links and place all of csv files in the project-02-python folder:
Data Source: [Divvy Data](https://drive.google.com/file/d/1F3bp6IXNZhE7SVzNU7VGblTTmT3iarlR/view?usp=sharing)

Open the terminal and go to the project-02-python folder

Create a virtual environment and activate it

```bash
    python -m venv venv
    source venv/bin/activate
```

Install the dependencies

```bash
    pip install -r requirements.txt
```

Run the script

```bash
    python bikeshare_2.py
```

Follow the instructions on the screen.