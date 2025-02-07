import psycopg2 as pg2

conn = pg2.connect(database="SUA_BASE_DADOS", user="USUARIO_BANCO_DADOS", password="SUA_SENHA", host="127.0.0.1", port="5432")

comando_sql = '''CREATE TABLE produtos (
                codigo SERIAL PRIMARY KEY,
                nome TEXT NOT NULL,
                preco REAL NOT NULL
            );'''

setDB = conn.cursor()
setDB.execute(comando_sql)
conn.commit()
setDB.close()
conn.close()