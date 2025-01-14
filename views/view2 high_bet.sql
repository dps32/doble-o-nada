use sieteymedio;

CREATE VIEW highest_bet_per_game AS
SELECT
    r.game_id AS game_id,                  -- Identificador de la partida
    pr.player_id AS player_id,             -- Identificador del jugador
    MAX(pr.player_bet) AS highest_bet      -- Apuesta más alta en la partida
FROM 
    player_rounds pr                       -- Tabla de rondas por jugador
JOIN 
    rounds r ON pr.round_id = r.round_id   -- Relacionar las rondas con las partidas
GROUP BY 
    r.game_id, pr.player_id                -- Agrupar por partida y jugador
HAVING 
    highest_bet = (
        SELECT MAX(pr2.player_bet)
        FROM player_rounds pr2
        JOIN rounds r2 ON pr2.round_id = r2.round_id
        WHERE r2.game_id = r.game_id
    )
ORDER BY 
    highest_bet DESC,                      -- Ordenar por apuesta más alta (descendente)
    pr.player_id ASC;                      -- En caso de empate, mostrar el jugador con menor ID
    
SELECT * FROM highest_bet_per_game;