-- Create an AdventureWorks2022 database if it doesn't exist
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'AdventureWorks2022')
BEGIN
    CREATE DATABASE AdventureWorks2022;
END
GO

USE AdventureWorks2022;
GO

-- Drop stored procedure if it already exists
IF OBJECT_ID('InsertSampleData', 'P') IS NOT NULL
    DROP PROCEDURE InsertSampleData;
GO

IF OBJECT_ID('Product', 'U') IS NOT NULL
    DROP TABLE Product;
IF OBJECT_ID('Orders', 'U') IS NOT NULL
    DROP TABLE Orders;
IF OBJECT_ID('Customer', 'U') IS NOT NULL
    DROP TABLE Customer;
GO

-- Create the Customer table
CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY IDENTITY(1,1),
    FirstName NVARCHAR(50),
    LastName NVARCHAR(50)
);
GO

-- Create the Order table
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY IDENTITY(1,1),
    CustomerID INT FOREIGN KEY REFERENCES Customer(CustomerID),
    OrderDate DATE
);
GO

-- Create the Product table
CREATE TABLE Product (
    ProductID INT PRIMARY KEY IDENTITY(1,1),
    ProductName NVARCHAR(100),
    Price DECIMAL(10, 2)
);
GO

-- Create a stored procedure for inserting data
CREATE PROCEDURE InsertSampleData
AS
BEGIN
    -- Insert sample data into the Customer table
    INSERT INTO Customer (FirstName, LastName)
    VALUES ('John', 'Doe'),
           ('Jane', 'Doe'),
           ('Alice', 'Smith');

    -- Insert sample data into the Order table
    INSERT INTO Orders (CustomerID, OrderDate)
    VALUES (1, '2024-03-18'),
           (2, '2024-03-17'),
           (3, '2024-03-16');

    -- Insert sample data into the Product table
    INSERT INTO Product (ProductName, Price)
    VALUES ('ProductA', 10.99),
           ('ProductB', 20.50),
           ('ProductC', 5.75);
END;
GO

-- Execute the stored procedure to insert sample data
EXEC InsertSampleData;


-- Execute the stored procedure to insert sample data
EXEC InsertSampleData;
