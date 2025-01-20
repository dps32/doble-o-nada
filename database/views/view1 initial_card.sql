use sieteymedio;

CREATE OR REPLACE VIEW player_initial_card_statistic AS
SELECT 
    p.player_id AS player_id, -- Identificador del jugador
    p.name AS player_name, -- Nombre del jugador
    SUBSTRING_INDEX(c.name, ' ', -1) AS suit, -- Palo de la carta inicial más repetida
    c.name AS most_repeated_card, -- Nombre completo de la carta inicial más repetida
    COUNT(*) AS times_repeated, -- Número de veces que se ha repetido
    COUNT(DISTINCT r.game_id) AS total_games -- Total de partidas jugadas
FROM 
    players p
JOIN 
    player_rounds pr ON p.player_id = pr.player_id -- Relación jugadores y rondas
JOIN 
    rounds r ON pr.round_id = r.round_id -- Relación rondas y partidas
JOIN 
    games g ON r.game_id = g.game_id -- Relación partidas
JOIN 
    cards c ON pr.first_card_in_hand = c.card_id -- Relación cartas iniciales
WHERE 
    r.round_number = 0 AND p.deleted = 0 -- Considerar solo la ronda inicial (ronda 0) y jugadores no borrados
GROUP BY 
    p.player_id, c.card_id -- Agrupar por jugador y carta inicial
HAVING 
    total_games >= 3 -- Solo jugadores con al menos 3 partidas
ORDER BY 
    player_id, times_repeated DESC; -- Ordenar por jugador y frecuencia