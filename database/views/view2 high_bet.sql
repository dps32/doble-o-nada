use sieteymedio;

CREATE VIEW highest_bet_per_game AS
SELECT
    r.game_id,
    pr.player_id,
    pr.player_bet
FROM
    player_rounds pr
JOIN rounds r ON pr.round_id = r.round_id
WHERE
    (r.game_id, pr.player_bet, pr.player_id) IN (
        SELECT
            r2.game_id,
            MAX(pr2.player_bet) AS max_bet,
            MIN(pr2.player_id) AS min_player_id
        FROM
            player_rounds pr2
        JOIN rounds r2 ON pr2.round_id = r2.round_id
        GROUP BY
            r2.game_id
    )
ORDER BY
    pr.player_bet DESC;