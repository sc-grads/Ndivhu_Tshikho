use IPLAnalysisDB

CREATE TABLE ipl_ball_by_ball_2008_2022
(
    id int NOT NULL,
    innings int,
    overs int,
    ball_number int,
    batter varchar(50),
    bowler varchar(50),
    non_striker varchar(50),
    extra_type varchar(50),
    batsman_run int,
    extras_run int,
    total_run int,
    non_boundary bit,
    iswicket_delivery bit,
    player_out varchar(50),
    dismissal_kind varchar(50),
    fielders_involved varchar(50),
    batting_team varchar(50)
);

BULK INSERT ipl_ball_by_ball_2008_2022
FROM 'C:\Users\NdivhudzannyiT\OneDrive - Northern Data (Pty) Ltd\Documents\Udemy Course\IPL\ipl_ball_by_ball_2008_2022.csv'
WITH
(
    FIRSTROW = 2,  -- Skip the header row
    FIELDTERMINATOR = ',',  -- Delimiter for fields
    ROWTERMINATOR = '\n',  -- Delimiter for rows
    TABLOCK
);
Select * from [dbo].[ipl_ball_by_ball_2008_2022]
Select * from ipl_matches_2008_2022


CREATE TABLE ipl_matches_2008_2022
(
    id int PRIMARY KEY,
    city varchar(50),
    match_date date,
    season varchar(50),
    match_number varchar(50),
    team1 varchar(50),
    team2 varchar(50),
    venue varchar(100),
    toss_winner varchar(50),
    toss_decision varchar(50),
    superover varchar(50),
    winning_team varchar(50),
    won_by varchar(50),
    margin varchar(50),
    method varchar(50),
    player_of_match varchar(50),
    umpire1 varchar(50),
    umpire2 varchar(50)
);


BULK INSERT ipl_matches_2008_2022
FROM 'C:\Users\NdivhudzannyiT\OneDrive - Northern Data (Pty) Ltd\Documents\Udemy Course\IPL\ipl_matches_2008_2022.csv'
WITH
(
    FIRSTROW = 2,  -- Skip the header row
    FIELDTERMINATOR = ',',  -- Delimiter for fields
    ROWTERMINATOR = '\n',  -- Delimiter for rows
    TABLOCK
);

