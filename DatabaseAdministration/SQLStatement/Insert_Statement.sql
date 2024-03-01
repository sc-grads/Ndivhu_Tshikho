CREATE TABLE salesstaff(
   staffid int NOT NULL PRIMARY KEY,
   fName nvarchar(50),
   lName nvarchar(50) 
)


INSERT INTO salesstaff (staffid, fName, lName) VALUES(200, 'Israel', 'Ndivhudzannyi')
SELECT * From salesstaff

INSERT INTO salesstaff (staffid, fName, lName) VALUES (300, 'John', 'Wick'), (400, 'lesedi', 'Ndou')
SELECT * From salesstaff

-----------------------------------------------------------------------------------------------------

CREATE TABLE salesstaffNew(
   ID int NOT NULL IDENTITY PRIMARY KEY,
   staffid int NOT NULL,
   fName nvarchar(50),
   lName nvarchar(50) 
)

INSERT INTO salesstaffNew(staffid, fName, lName) VALUES (200, 'Israel', 'Ndivhudzannyi')
SELECT * From salesstaffNew

INSERT INTO salesstaffNew(staffid, fName, lName) VALUES (300, 'John', 'Wick'), (400, 'lesedi', 'Ndou')
SELECT * From salesstaffNew

--------------------------------------------------------------------------------------------------------

CREATE TABLE nameOnlyTable(
    fName nvarchar(50),
   lName nvarchar(50)
  )

  SELECT * From nameOnlyTable

  INSERT nameOnlyTable (fName, lName)
  SELECT fName, lName From salesstaffNew

---------------------------------------------------------------------------------------------------------

SELECT * INTO salesstaffNew_bkp from salesstaffNew
SELECT * From salesstaffNew_bkp

----------------------------------------------------------------------------------------------------------

