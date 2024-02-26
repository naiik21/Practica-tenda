import psycopg

def dbClient():
    try:
        # String per a la connexió amb la base de dades postgres usant les dades del docker-compose.yml
        conexio = """
            dbname = Botiga
            user = user_postgres
            password=pass_postgres
            host=localhost
            port=5432
            """

        # Guardem en una variable la connexió amb la BBDD
        return psycopg.connect(conexio)

    except Exception as e:
        print(f"ERROR: {e}")