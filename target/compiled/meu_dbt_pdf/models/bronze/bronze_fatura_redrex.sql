WITH formatted AS (
    SELECT
        n_nota,
        cv,
        merc,
        tipo,
        STR_TO_DATE(vecto, '%d%m%Y') AS vecto,
        CAST(qted AS SIGNED) AS qted,
        mercadoria,
        CAST(REPLACE(cotacao, ',', '.') AS DECIMAL(10, 2)) AS cotacao,
        STR_TO_DATE(data_de_pregao, '%d%m%Y') AS data_de_pregao,
        CAST(REPLACE(txop, ',', '.') AS DECIMAL(10, 2)) AS txop
    FROM
        `analytics`.`fatura_redrex`
)

SELECT * FROM formatted