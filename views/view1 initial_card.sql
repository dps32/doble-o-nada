use sieteymedio;

CREATE VIEW player_initial_card_statistics AS
SELECT 
    pr.player_id AS player_id, -- Identificador del jugador
    p.name AS player_name, -- Nombre del jugador
    c.priority AS suit,  -- Palo de la carta
    c.name AS initial_card_name, -- Nombre de la carta inicial
    COUNT(*) AS times_repeated, -- Número de veces que la carta fue la inicial
    COUNT(DISTINCT r.game_id) AS total_games -- Total de partidas jugadas por el jugador
FROM 
    player_rounds pr
JOIN 
    rounds r ON pr.round_id = r.round_id -- Relación con las rondas
JOIN 
    games g ON r.game_id = g.game_id -- Relación con las partidas
JOIN 
    players p ON pr.player_id = p.player_id -- Relación con los jugadores
JOIN 
    cards c ON pr.first_card_in_hand = c.card_id -- Relación con las cartas
WHERE 
    r.round_number = 1 -- Solo considerar la primera ronda
GROUP BY 
    pr.player_id, c.card_id -- Agrupar por jugador y carta inicial
HAVING
	total_games > 3 -- Colegon cuenta el total de juegos
ORDER BY 
    pr.player_id, times_repeated DESC; -- Ordenar por jugador y veces repetidas

