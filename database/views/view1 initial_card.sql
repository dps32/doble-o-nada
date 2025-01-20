use sieteymedio;
CREATE VIEW player_initial_card_statistics AS
SELECT 
    p.player_id AS player_id, -- ID del player
    p.name AS player_name, -- name del player
    SUBSTRING_INDEX(c.name, ' ', -1) AS suit, -- Palo de la carta 
    c.name AS most_repeated_card, -- Nombre completo de la carta 
    COUNT(*) AS times_repeated, -- Número de veces repetida
    COUNT(DISTINCT r.game_id) AS total_games -- Total games
FROM 
    players p
JOIN 
    player_rounds pr ON p.player_id = pr.player_id -- Relación jugadores-rondas
JOIN 
    rounds r ON pr.round_id = r.round_id -- Relación rondas-partidas
JOIN 
    games g ON r.game_id = g.game_id -- Relación partidas
JOIN 
    cards c ON pr.first_card_in_hand = c.card_id -- Relación cartas iniciales
WHERE 
    r.round_number = 0 -- Considerar primera ronda
GROUP BY 
    p.player_id, c.card_id, suit -- Agrupar jugador y carta inicial
HAVING 
    COUNT(DISTINCT r.game_id) >= 3 -- Solo players que hayan jugado al menos 3 partidas
ORDER BY 
    p.player_id, times_repeated DESC; -- Ordenar por jugador y frecuencia