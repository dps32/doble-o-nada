use sieteymedio;

CREATE VIEW player_initial_card_statistics AS
SELECT 
    p.player_id AS player_id,
    p.name AS player_name,
    SUBSTRING_INDEX(c.name, ' ', -1) AS suit, -- Palo de la c.inicial más repetida
    c.name AS most_repeated_card, -- Nombre completo de la c.inicial más repetida
    COUNT(*) AS times_repeated, -- Número de veces que se ha repetido
    COUNT(DISTINCT gp.game_id) AS total_games -- Total de partidas jugadas
FROM 
    players p
JOIN 
    player_rounds r ON p.player_id = r.player_id -- Relacionar jugadores con rondas
JOIN 
    cards c ON c.card_id = r.first_card_in_hand -- Usar columna first_card_in_hand
JOIN 
    game_players gp ON p.player_id = gp.player_id -- Relacionar jugadores con juegos
WHERE 
    r.round_number = 1 -- Considerar solo la primera carta de cada ronda
GROUP BY 
    p.player_id, c.card_id -- Agrupar por jugador y carta inicial
HAVING 
    total_games >= 3 -- Solo players en 3 o más partidas
ORDER BY 
    player_id, times_repeated DESC; -- ordenado descendente.

SELECT * FROM player_initial_card_statistics;