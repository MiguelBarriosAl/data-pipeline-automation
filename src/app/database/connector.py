import mysql.connector


class Database:
    def __init__(self, host: str, database: str, user: str, password: str):
        """
        Connexion database SQL and query
        return: Output query
        """
        self.database = database
        self.user = user
        self.password = password
        self.host = host

    def _connect_db(self) -> object:
        return conn_db(self.host, self.database, self.user, self.password)

    def status_con(self):
        conn = self._connect_db()
        return "Status connection: %s" % conn.is_connected()

    def query(self, query) -> str:
        conn = self._connect_db()
        return query_db(conn, query)



def conn_db(host, database, user, password) -> list:
    try:
        conn = mysql.connector.connect(host=host,
                                       database=database,
                                       user=user,
                                       password=password)

    except Exception as e:
        conn = False
        print('Error connecting to Mysql', e)
    return conn


def query_db(conn: object, query: str) -> str:
    results = []
    try:
        with conn.cursor(buffered=True) as cur:
            cur.execute(query)
            conn.commit()
    except Exception as e:
        print('Error query %s to Mysql with error %s' % e)
    finally:
        if conn.is_connected():
            conn.close()
            cur.close()
    return results