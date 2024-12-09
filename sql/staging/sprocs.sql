-- SPROC- MERGE GAMES FROM STAGING TO MLS
CREATE PROCEDURE [STAGING].[MERGE_GAMES]
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON

    BEGIN TRAN

	MERGE INTO MLS.GAMES AS t
	USING STAGING.GAMES AS s
    ON t.GAME_ID = CAST(s.GAME_ID AS NVARCHAR(50))
    WHEN MATCHED THEN
        UPDATE SET
            t.DATE_TIME_UTC = CAST(s.DATE_TIME_UTC AS DATETIMEOFFSET),
            t.HOME_SCORE = CAST(s.HOME_SCORE AS INT),
            t.AWAY_SCORE = CAST(s.AWAY_SCORE AS INT),
            t.HOME_TEAM_ID = CAST(s.HOME_TEAM_ID AS NVARCHAR(50)),
            t.AWAY_TEAM_ID = CAST(s.AWAY_TEAM_ID AS NVARCHAR(50)),
            t.REFEREE_ID = CAST(s.REFEREE_ID AS NVARCHAR(50)),
            t.STADIUM_ID = CAST(s.STADIUM_ID AS NVARCHAR(50)),
            t.HOME_MANAGER_ID = CAST(s.HOME_MANAGER_ID AS NVARCHAR(50)),
            t.AWAY_MANAGER_ID = CAST(s.AWAY_MANAGER_ID AS NVARCHAR(50)),
            t.EXPANDED_MINUTES = CAST(s.EXPANDED_MINUTES AS INT),
            t.SEASON_NAME = CAST(s.SEASON_NAME AS NVARCHAR(10)),
            t.MATCHDAY = CAST(s.MATCHDAY AS INT),
            t.ATTENDANCE = CAST(s.ATTENDANCE AS INT),
            t.KNOCKOUT_GAME = CAST(s.KNOCKOUT_GAME AS BIT),
            t.LAST_UPDATED_UTC = CAST(s.LAST_UPDATED_UTC AS DATETIMEOFFSET)
    WHEN NOT MATCHED THEN
        INSERT (
            GAME_ID,
            DATE_TIME_UTC,
            HOME_SCORE,
            AWAY_SCORE,
            HOME_TEAM_ID,
            AWAY_TEAM_ID,
            REFEREE_ID,
            STADIUM_ID,
            HOME_MANAGER_ID,
            AWAY_MANAGER_ID,
            EXPANDED_MINUTES,
            SEASON_NAME,
            MATCHDAY,
            ATTENDANCE,
            KNOCKOUT_GAME,
            LAST_UPDATED_UTC
        )
        VALUES (
            CAST(s.GAME_ID AS NVARCHAR(50)),
            CAST(s.DATE_TIME_UTC AS DATETIMEOFFSET),
            CAST(s.HOME_SCORE AS INT),
            CAST(s.AWAY_SCORE AS INT),
            CAST(s.HOME_TEAM_ID AS NVARCHAR(50)),
            CAST(s.AWAY_TEAM_ID AS NVARCHAR(50)),
            CAST(s.REFEREE_ID AS NVARCHAR(50)),
            CAST(s.STADIUM_ID AS NVARCHAR(50)),
            CAST(s.HOME_MANAGER_ID AS NVARCHAR(50)),
            CAST(s.AWAY_MANAGER_ID AS NVARCHAR(50)),
            CAST(s.EXPANDED_MINUTES AS INT),
            CAST(s.SEASON_NAME AS NVARCHAR(10)),
            CAST(s.MATCHDAY AS INT),
            CAST(s.ATTENDANCE AS INT),
            CAST(s.KNOCKOUT_GAME AS BIT),
            CAST(s.LAST_UPDATED_UTC AS DATETIMEOFFSET)
        );
    
    COMMIT TRAN
            
END
