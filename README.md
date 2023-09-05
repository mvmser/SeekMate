# SeekMate

## Summary

SeekMate is an all-in-one job-seeking platform engineered by Data Scientists for all data-driven professionals. This robust application provides a full pipeline to make your job search more efficient and effective.

## Goals

Develop the following features in the most generic way to easily scale to various sources.

- **Automated Job Scraping**: Collect job postings from various platforms in real-time.
- **Data Storage**: Use a database to store, manage, and update job listings.
- **User-Friendly Interface**: Create an intuitive user interface to search, filter, and manage job applications.

## Components

- **Scrapers**: Scrapers are orchestrated using Apache Airflow and are designed to gather job postings from multiple sources such as LinkedIn and Indeed.
  
- **Database**: A PostgreSQL database is used to store a comprehensive set of job attributes like the retrieval timestamp, company, posting date, job description, and source URL.
  
- **User Portal**: Built on Streamlit, the user portal allows for seamless browsing and filtering of job listings based on keywords, skills, and companies. It also provides functionality to manage applied jobs.

## Technologies Used

- Python
- Streamlit
- PostgreSQL
- Apache Airflow

## Get Started

/!\ It is highly recommended for Windows user to use WSL system: https://learn.microsoft.com/fr-fr/windows/wsl/install

### Installation Steps

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/mvmser/SeekMate.git
    ```
  
2. **Set up a Virtual Environment**:

    ```bash
    py -m venv venv
    .\venv\Scripts\activate
    ```
  
3. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```
  
4. **Install PostgreSQL Database**:

    Install PostgreSQL from official source:
    `https://www.postgresql.org/download/`

    Setup your password, port (e.g.: 5432) and locale to US.

5. **Initialize PostgreSQL Database**:

    For Linux Users

    ```bash
        # Start PostgreSQL service
        sudo service postgresql start

        # Create a new database
        createdb seekmate_db

        # Run migration scripts if applicable
        psql -U your_username -d seekmate_db -a -f database/sql_scripts/init.sql
    ```

    For Windows Users

    ```bash
        # Start PostgreSQL service
        # You can start it manually via Windows Services or use pg_ctl
        "C:\path\to\PostgreSQL\pg_ctl.exe" start -D "C:\path\to\PostgreSQL\data"

        # Open SQL Shell (psql) from Start Menu and run:
        CREATE DATABASE seekmate_db;

        # Run migration scripts if applicable (please complete the path)
        \i '.\database\sql_scripts\init.sql'

        # Example:
        # \i 'C:/Users/Mohamed/Documents/GitHub/SeekMate/database/sql_scripts/init.sql'
    ```

6. **Initialize Airflow for Job Scraping**:
    Notes:
    - Airflow already installed with requirements
    - Windows users should remove &
    - Windows users should install WSL


    ```bash
        # Initialize Airflow Database
        airflow db init

        # Run Scheduler (in dedicated terminal)
        airflow scheduler &

        # Run Webserver (in dedicated terminal)
        airflow webserver -p 8080 &

        # Create user
        airflow users  create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin
    ```
  
7. **Launch Streamlit Application**:

    ```bash
    streamlit run portal/app.py
    ```

## Contributing

We welcome contributions! Feel free to comment any ideas.
