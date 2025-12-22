import os
import pymysql # Driver para MySQL
from sqlalchemy import create_engine

class RDSMySQLManager:
    def __init__(
        self, db_name=None, db_user=None, db_password=None, db_host=None, db_port="3306"
    ):
        # Verifica se as variáveis de ambiente existem ou usa os argumentos
        self.db_name = db_name or os.getenv("DB_NAME") or "analytics"
        self.db_user = db_user or os.getenv("DB_USER") or "root"
        self.db_password = db_password or os.getenv("DB_PASSWORD") or "amanda"
        self.db_host = db_host or os.getenv("DB_HOST") or "localhost"
        self.db_port = db_port

    def connect(self):
        try:
            # Conexão usando PyMySQL
            connection = pymysql.connect(
                host=self.db_host,
                user=self.db_user,
                password=self.db_password,
                database=self.db_name,
                port=int(self.db_port)
            )
            print("Conexão bem-sucedida ao MySQL.")
            return connection
        except Exception as e:
            print(f"Erro ao conectar ao MySQL: {e}")
            return None

    def alchemy(self):
        # String de conexão mudou o prefixo para mysql+pymysql
        self.engine = create_engine(
            f"mysql+pymysql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
        )
        return self.engine
   