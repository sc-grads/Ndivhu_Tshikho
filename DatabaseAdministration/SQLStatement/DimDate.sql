-- Function to calculate Easter Sunday

GO
CREATE FUNCTION dbo.CalculateEasterSunday(@Year INT)
RETURNS DATE
AS
BEGIN
    DECLARE @a INT = @Year % 19;
    DECLARE @b INT = @Year / 100;
    DECLARE @c INT = @Year % 100;
    DECLARE @d INT = @b / 4;
    DECLARE @e INT = @b % 4;
    DECLARE @f INT = (@b + 8) / 25;
    DECLARE @g INT = (@b - @f + 1) / 3;
    DECLARE @h INT = (19 * @a + @b - @d - @g + 15) % 30;
    DECLARE @i INT = @c / 4;
    DECLARE @k INT = @c % 4;
    DECLARE @l INT = (32 + 2 * @e + 2 * @i - @h - @k) % 7;
    DECLARE @m INT = (@a + 11 * @h + 22 * @l) / 451;
    DECLARE @Month INT = (@h + @l - 7 * @m + 114) / 31;
    DECLARE @Day INT = ((@h + @l - 7 * @m + 114) % 31) + 1;
    RETURN DATEFROMPARTS(@Year, @Month, @Day);
END;
GO

-- Create the Holidays table
CREATE TABLE Holidays (
    HolidayID INT PRIMARY KEY IDENTITY(1,1),
    HolidayDate DATE NOT NULL,
    HolidayName VARCHAR(100) NOT NULL,
    IsFixedDate BIT NOT NULL -- Indicates if the holiday is on a fixed date every year
);

-- Insert fixed-date holidays for South Africa
INSERT INTO Holidays (HolidayDate, HolidayName, IsFixedDate) VALUES
('2024-01-01', 'New Year''s Day', 1),
('2024-03-21', 'Human Rights Day', 1),
('2024-04-27', 'Freedom Day', 1),
('2024-05-01', 'Workers'' Day', 1),
('2024-06-16', 'Youth Day', 1),
('2024-08-09', 'National Women''s Day', 1),
('2024-09-24', 'Heritage Day', 1),
('2024-12-16', 'Day of Reconciliation', 1),
('2024-12-25', 'Christmas Day', 1),
('2024-12-26', 'Day of Goodwill', 1);

-- Declare the range of years for variable date holidays
DECLARE @StartYear INT = 2024;
DECLARE @EndYear INT = 2030;

-- Loop through each year and calculate variable date holidays
WHILE @StartYear <= @EndYear
BEGIN
    DECLARE @EasterSunday DATE = dbo.CalculateEasterSunday(@StartYear);
    DECLARE @GoodFriday DATE = DATEADD(DAY, -2, @EasterSunday);
    DECLARE @FamilyDay DATE = DATEADD(DAY, 1, @EasterSunday);

    -- Insert variable date holidays
    INSERT INTO Holidays (HolidayDate, HolidayName, IsFixedDate) VALUES
    (@GoodFriday, 'Good Friday', 0),
    (@FamilyDay, 'Family Day', 0);

    -- Increment the year
    SET @StartYear = @StartYear + 1;
END;

-- Create the DimDate table if it doesn't already exist
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[DimDate]') AND type in (N'U'))
BEGIN
    CREATE TABLE DimDate (
        DateID INT PRIMARY KEY IDENTITY(1,1),
        Date DATE NOT NULL,
        DayOfWeek VARCHAR(50) NOT NULL,
        DayOfMonth INT NOT NULL,
        Month INT NOT NULL,
        MonthName VARCHAR(50) NOT NULL,
        Quarter INT NOT NULL,
        Year INT NOT NULL,
        WeekOfYear INT NOT NULL,
        IsHoliday BIT DEFAULT 0,
        HolidayName VARCHAR(100) NULL
    );
END;

-- Declare the date range
DECLARE @StartDate DATE = '2024-01-01'; -- Start date of your range
DECLARE @EndDate DATE = '2030-12-31';   -- End date of your range

-- Use a recursive CTE to generate the date range
WITH DateRange AS (
    SELECT @StartDate AS Date
    UNION ALL
    SELECT DATEADD(DAY, 1, Date)
    FROM DateRange
    WHERE DATEADD(DAY, 1, Date) <= @EndDate
)
INSERT INTO DimDate (Date, DayOfWeek, DayOfMonth, Month, MonthName, Quarter, Year, WeekOfYear)
SELECT 
    Date,
    DATENAME(WEEKDAY, Date) AS DayOfWeek,
    DATEPART(DAY, Date) AS DayOfMonth,
    DATEPART(MONTH, Date) AS Month,
    DATENAME(MONTH, Date) AS MonthName,
    DATEPART(QUARTER, Date) AS Quarter,
    DATEPART(YEAR, Date) AS Year,
    DATEPART(WEEK, Date) AS WeekOfYear
FROM DateRange
OPTION (MAXRECURSION 0);

-- Update DimDate with holiday information
UPDATE d
SET d.IsHoliday = 1,
    d.HolidayName = h.HolidayName
FROM DimDate d
JOIN Holidays h ON d.Date = h.HolidayDate;

-- Verify the inserted data in DimDate
SELECT TOP 10 * FROM DimDate 
