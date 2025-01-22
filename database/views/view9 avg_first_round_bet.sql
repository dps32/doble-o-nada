use sieteymedio;

CREATE VIEW average_first_round_bet AS
    SELECT 
        r.game_id AS 'Game ID', -- ID del game
        AVG(pr.player_bet) AS 'Average Bet (First Round)' -- apuesta media en la primera ronda
    FROM
        rounds r -- Tabla de rondas
            JOIN
        player_rounds pr ON r.round_id = pr.round_id -- Relacionar los players round con round
    WHERE
        r.round_number = 1 -- buscar en la primera ronda
        AND
        pr.player_bet > 0 -- Ignora las apuestas = 0 (las de la banca)
    GROUP BY r.game_id; -- agrupar por partida