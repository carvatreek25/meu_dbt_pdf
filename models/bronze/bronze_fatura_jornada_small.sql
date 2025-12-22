WITH formatted AS (
    SELECT
        n_nota,
        STR_TO_DATE(data_de_pregao, '%d%m%Y') AS data_de_pregao,
        CAST(REPLACE(corretagem, ',', '.') AS DECIMAL(10, 2)) AS tx_corretagem,
        CAST(REPLACE(taxa_de_registro, ',', '.') AS DECIMAL(10, 2)) AS taxa
    FROM
        {{ source('investimentos', 'fatura_jornada_small') }}
)

SELECT * FROM formatted