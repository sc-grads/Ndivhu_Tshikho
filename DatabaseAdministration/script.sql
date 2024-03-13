-- Create the database
CREATE DATABASE MyDatabase;

-- Use the created database
USE MyDatabase;
 
-- Create the Person table
CREATE TABLE Person (
        FirstName NVARCHAR(50),
        LastName NVARCHAR(50)
    );

-- Insert sample data into the Person table
INSERT INTO Person(FirstName, LastName) VALUES('John', 'Doe'),('Jane', 'Smith'),('Alice', 'Johnson');
