-- Create MyDatabase if it doesn't exist
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'AdventureWorks2022')
BEGIN
    CREATE DATABASE AdventureWorks2022;
END
GO

USE AdventureWorks2022;

    -- Drop tables if they already exist
    IF OBJECT_ID('dbo.Customer', 'U') IS NOT NULL
        DROP TABLE dbo.Customer;
    IF OBJECT_ID('dbo.Order', 'U') IS NOT NULL
        DROP TABLE dbo.Order;
    IF OBJECT_ID('dbo.Product', 'U') IS NOT NULL
        DROP TABLE dbo.Product;

    -- Create the Customer table
    CREATE TABLE dbo.Customer (
        CustomerID INT PRIMARY KEY IDENTITY(1,1),
        FirstName NVARCHAR(50),
        LastName NVARCHAR(50)
    );

    -- Create the Order table
    CREATE TABLE dbo.Order (
        OrderID INT PRIMARY KEY IDENTITY(1,1),
        CustomerID INT FOREIGN KEY REFERENCES dbo.Customer(CustomerID),
        OrderDate DATE
    );

    -- Create the Product table
    CREATE TABLE dbo.Product (
        ProductID INT PRIMARY KEY IDENTITY(1,1),
        ProductName NVARCHAR(100),
        Price DECIMAL(10, 2)
    );

    -- Insert sample data into the Customer table
    INSERT INTO dbo.Customer (FirstName, LastName)
    VALUES ('John', 'Doe'),
           ('Jane', 'Doe'),
           ('Alice', 'Smith');

    -- Insert sample data into the Order table
    INSERT INTO dbo.Order (CustomerID, OrderDate)
    VALUES (1, '2024-03-18'),
           (2, '2024-03-17'),
           (3, '2024-03-16');

    -- Insert sample data into the Product table
    INSERT INTO dbo.Product (ProductName, Price)
    VALUES ('ProductA', 10.99),
           ('ProductB', 20.50),
           ('ProductC', 5.75);

