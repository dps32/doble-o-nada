use sieteymedio;

CREATE VIEW average_last_round_bet AS
SELECT 
    r.game_id AS "Game ID",
    AVG(pr.player_bet) AS "Average Bet (Last Round)"
FROM rounds r
JOIN player_rounds pr ON r.round_id = pr.round_id
WHERE r.round_number = (
    SELECT MAX(r2.round_number)
    FROM rounds r2
    WHERE r2.game_id = r.game_id
)
GROUP BY r.game_id;