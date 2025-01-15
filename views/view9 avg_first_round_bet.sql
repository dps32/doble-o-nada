use sieteymedio;

CREATE VIEW average_first_round_bet AS
SELECT 
    r.game_id AS "Game ID",
    AVG(pr.player_bet) AS "Average Bet (First Round)"
FROM rounds r
JOIN player_rounds pr ON r.round_id = pr.round_id
WHERE r.round_number = 1
GROUP BY r.game_id;