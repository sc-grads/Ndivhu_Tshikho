USE ECommerceDB; 

CREATE TABLE products (
    id INT PRIMARY KEY IDENTITY(1,1),
    name NVARCHAR(100) NOT NULL,
    description NVARCHAR(255),
    price DECIMAL(10, 2) NOT NULL
);

Select * from products
-------------------------------------------------------------------------

INSERT INTO Products (name, description, price) 
VALUES ('iPhone 14', 'The latest iPhone 14 with 128GB storage', 999.99),
       ('iPhone 13', 'iPhone 13 with 64GB storage', 799.99),
       ('iPhone 12', 'iPhone 12 with 64GB storage', 599.99);
-------------------------------------------------------------------------