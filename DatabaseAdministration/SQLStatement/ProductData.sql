
CREATE TABLE Product(
    ProductID INT primary key ,
    SubCategoryKey INT,
    Color VARCHAR(50),
    ProductName VARCHAR(100),
    RetailPrice DECIMAL(10, 2),
    StandardCost DECIMAL(10, 2)
);

INSERT INTO Product (ProductID, SubCategoryKey, Color, ProductName, RetailPrice, StandardCost) VALUES
(1, 3, 'Red', 'Alder', 23.95, 7.55),
(2, 2, 'Blue', 'Linder', 23.95, 7.55),
(3, 1, 'Green', 'Magnum', 23.95, 7.55),
(4, 1, 'Red', 'Quad', 43.95, 13.75),
(5, 1, 'Blue', 'Black Monk', 43.95, 13.75),
(6, 1, 'Green', 'Quad', 43.95, 13.75),
(7, 1, 'Red', 'Bing', 26.95, 8.25),
(8, 1, 'Blue', 'VanHelen', 26.95, 8.25),
(9, 1, 'Green', 'Magnum', 26.95, 8.25),
(10, 1, 'Florescent Pink', 'Carlota', 29.95, 9.15),
(11, 4, 'Florescent Blue', 'Carlota', 29.95, 9.15);

Select * from Product 
