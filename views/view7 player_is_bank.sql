use sieteymedio;

CREATE VIEW bank_users_per_game AS
SELECT
    r.game_id AS game_id,               -- Identificador de la partida
    COUNT(DISTINCT pr.player_id) AS bank_users_count -- Cantidad de usuarios que han sido banca
FROM
    player_rounds pr                    -- Tabla de rondas por jugador
JOIN
    rounds r ON pr.round_id = r.round_id -- Relacionar las rondas con las partidas
WHERE
    pr.is_bank = 1                      -- Solo considerar usuarios que han sido banca
GROUP BY
    r.game_id;                          -- Agrupar por partida
    
SELECT * FROM bank_users_per_game;