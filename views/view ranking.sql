use sieteymedio;
CREATE VIEW player_ranking AS
SELECT 
    p.player_id,
    p.name AS player_name,
    SUM(r.end_points - r.start_points) AS total_gains, -- Ganancias obtenidas
    COUNT(DISTINCT gp.game_id) AS games_played, -- Partidas jugadas
    SUM(TIMESTAMPDIFF(MINUTE, g.start_time, g.end_time)) AS total_minutes -- Minutos jugados
FROM 
    players p
LEFT JOIN 
    player_rounds r ON p.player_id = r.player_id -- Rondas jugadas por el jugador
LEFT JOIN 
    game_players gp ON p.player_id = gp.player_id -- Juegos en los que participó
LEFT JOIN 
    games g ON gp.game_id = g.game_id -- Juegos asociados a las rondas
GROUP BY 
    p.player_id, p.name;
    
SELECT * FROM player_ranking;

SELECT * FROM player_ranking ORDER BY total_gains DESC;

SELECT * FROM player_ranking ORDER BY games_played ASC;
