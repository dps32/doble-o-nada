use sieteymedio;

CREATE VIEW players_ranking AS
SELECT 
    p.player_id AS player_id,  -- ID del jugador
    p.name AS player_name,  -- Nombre del jugador
    SUM(pr.end_points - pr.start_points) AS total_gains, -- Ganancias totales obtenidas
    COUNT(DISTINCT r.game_id) AS total_games, -- Total de partidas jugadas
    p.time AS total_minutes_played -- Minutos totales jugados acumulados
FROM 
    players p
JOIN 
    player_rounds pr ON p.player_id = pr.player_id   -- Relación entre jugadores y rondas
JOIN 
    rounds r ON pr.round_id = r.round_id -- Relación entre rondas y partidas
JOIN 
    games g ON r.game_id = g.game_id  -- Relación entre partidas y su duración
GROUP BY 
    p.player_id  -- Agrupar por jugador
ORDER BY 
    total_gains DESC, total_games DESC; -- Ordenar por ganancias y partidas jugadas
