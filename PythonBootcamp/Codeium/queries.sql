-- database: SSMS

-- Get all users from the users table
SELECT * FROM users

-- Get all users from the users table with the name "John"
SELECT * FROM users WHERE name = 'John'

-- Show all the tables in the database
SELECT * FROM INFORMATION_SCHEMA.TABLES

-- get all the users from the users table ordered by the salary
SELECT * FROM users ORDER BY salary

-- get  all the users from the users table and join them wt the addres table
SELECT * FROM users JOIN addresses ON users.id = addresses.user_id

-- get all the users table that have the name that end with b
SELECT * FROM users WHERE name LIKE '%b'
