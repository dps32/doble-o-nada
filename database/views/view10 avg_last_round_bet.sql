use sieteymedio;

CREATE VIEW average_last_round_bet AS
    SELECT 
        r.game_id AS 'Game ID', -- ID del game
        AVG(pr.player_bet) AS 'Average Bet (Last Round)' -- apuesta media en la primera ronda
    FROM
        rounds r -- Tabla de rondas
            JOIN
        player_rounds pr ON r.round_id = pr.round_id -- Relacionar los players round con round
    WHERE
        r.round_number = (SELECT 
                MAX(r2.round_number) -- encontrar la ultima ronda poniendo el max ya que puede variar la ultima ronda de cada partida
            FROM
                rounds r2 -- tabla de rounds
            WHERE
                r2.game_id = r.game_id) -- que partida ha sido
    GROUP BY r.game_id; -- agrupar por ID