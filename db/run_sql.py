import psycopg2, os  
import psycopg2.extras as ext

def run_sql(sql, values = None):
    conn = None
    results = []
    database_url = os.getenv('DATABASE_URL')

    try:
        conn=psycopg2.connect(database_url)
        cur = conn.cursor(cursor_factory=ext.DictCursor)   
        cur.execute(sql, values)
        conn.commit()
        results = cur.fetchall()
        cur.close()           
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return results