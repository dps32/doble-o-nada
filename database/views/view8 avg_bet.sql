use sieteymedio;

CREATE VIEW average_bet_per_game AS
SELECT
    r.game_id AS game_id, -- Identificador de la partida
    AVG(pr.player_bet) AS average_bet -- Apuesta media por partida
FROM
    player_rounds pr -- Tabla de rondas por jugador
JOIN
    rounds r ON pr.round_id = r.round_id -- Relacionar las rondas con las partidas
WHERE
	pr.player_bet > 0 -- Ignora las apuestas que son igual a 0 (las de la banca)
GROUP BY
    r.game_id; -- Agrupar por partida

SELECT * FROM average_bet_per_game;
