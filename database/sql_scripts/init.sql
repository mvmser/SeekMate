-- Drop existing tables if they exist
DROP TABLE IF EXISTS jobs CASCADE;
DROP TABLE IF EXISTS applied_jobs CASCADE;

-- Create jobs table
CREATE TABLE jobs (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    company VARCHAR(255) NOT NULL,
    location VARCHAR(255),
    posting_date DATE,
    description TEXT,
    source_url VARCHAR(255) UNIQUE,
    retrieval_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create applied_jobs table
CREATE TABLE applied_jobs (
    id SERIAL PRIMARY KEY,
    job_id INT REFERENCES jobs(id),
    user_id VARCHAR(255) NOT NULL,  -- Assuming user_id is a string; this could be an INT or another type depending on your system
    application_date DATE,
    status VARCHAR(50)
);

-- Optional: Indexes for faster queries
CREATE INDEX idx_jobs_title ON jobs(title);
CREATE INDEX idx_applied_jobs_user ON applied_jobs(user_id);
