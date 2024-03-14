-- Use transactions for atomicity
BEGIN TRANSACTION;

-- Drop the existing database if it exists
DROP DATABASE IF EXISTS MyDatabase;

-- Create the new database
CREATE DATABASE MyDatabase;

-- Use the newly created database
USE MyDatabase;

-- Create the Person table
CREATE TABLE Person (
    FirstName NVARCHAR(20),
    LastName NVARCHAR(20)
);

-- Insert sample data into the Person table
INSERT INTO Person (FirstName, LastName) 
VALUES ('John', 'Doe'), ('Jane', 'Smith'), ('Alice', 'Johnson');

-- Create a stored procedure to insert data into the Person table
CREATE OR ALTER PROCEDURE InsertPerson
    @FirstName NVARCHAR(20),
    @LastName NVARCHAR(20)
AS
BEGIN
    INSERT INTO Person (FirstName, LastName) VALUES (@FirstName, @LastName);
END;

-- Use the stored procedure to insert more data
EXEC InsertPerson 'Michael', 'Jordan';
EXEC InsertPerson 'LeBron', 'James';
EXEC InsertPerson 'Kobe', 'Bryant';

-- Commit the transaction
COMMIT TRANSACTION;
