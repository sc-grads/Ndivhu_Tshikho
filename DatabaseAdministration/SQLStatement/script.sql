-- Create MyDatabase if it doesn't exist
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'MyDatabase')
BEGIN
    CREATE DATABASE MyDatabase;
END
GO
-- Your existing SQL commands here
USE MyDatabase;

-- Create the Person table
CREATE TABLE Person (
        FirstName NVARCHAR(50),
        LastName NVARCHAR(50)
    );

-- Insert sample data into the Person table
INSERT INTO Person(FirstName, LastName) VALUES('John', 'Doe'),('Jane', 'Smith'),('Alice', 'Johnson');

-- Create a stored procedure to insert data into the Person table
CREATE PROCEDURE InsertPerson
    @FirstName NVARCHAR(50),
    @LastName NVARCHAR(50)
AS
BEGIN
    INSERT INTO Person (FirstName, LastName) VALUES (@FirstName, @LastName);
END
GO

-- Use the stored procedure to insert more data
EXEC InsertPerson 'Michael', 'Jordan';
EXEC InsertPerson 'LeBron', 'James';
EXEC InsertPerson 'Kobe', 'Bryant';
GO
