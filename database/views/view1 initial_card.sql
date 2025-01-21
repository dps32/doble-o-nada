use sieteymedio;

CREATE VIEW player_initial_card_statistics AS
SELECT 
    player_id,
    player_name,
    suit,
    most_repeated_card,
    times_repeated,
    total_games
FROM
(
    SELECT 
        p.player_id,
        p.name AS player_name,
        SUBSTRING_INDEX(c.name, ' ', -1) AS suit,
        c.name AS most_repeated_card,
        COUNT(*) AS times_repeated,
        (
            SELECT COUNT(DISTINCT gp.game_id)
            FROM game_players gp
            WHERE gp.player_id = p.player_id
        ) AS total_games,
        
        -- Asignamos un "ranking" según la cantidad de repeticiones (descendente)
        ROW_NUMBER() OVER (
            PARTITION BY p.player_id
            ORDER BY COUNT(*) DESC
        ) AS rn
        
    FROM players p
    JOIN player_rounds pr 
        ON p.player_id = pr.player_id
    JOIN rounds r 
        ON pr.round_id = r.round_id
    JOIN games g 
        ON r.game_id = g.game_id
    JOIN cards c 
        ON pr.first_card_in_hand = c.card_id
    WHERE r.round_number = 0       -- Cartas iniciales (ronda 0)
      AND p.deleted = 0            -- Jugadores no eliminados
    GROUP BY p.player_id, c.card_id, suit, c.name
) AS sub
WHERE 
    sub.total_games >= 3  -- Solo jugadores con al menos 3 partidas
    AND sub.rn = 1        -- Solo la carta más repetida (la "número 1" en el ranking)
ORDER BY 
    sub.player_id;
