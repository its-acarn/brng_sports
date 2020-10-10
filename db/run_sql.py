import psycopg2  
import psycopg2.extras as ext

def run_sql(sql, values = None):
    conn = None
    results = []
    
    try:
        conn=psycopg2.connect("dbname='postgres://usxgbeocilcais:bb23b554c2d5002767e60615684e43912b893104e91fe96f84875210c7cec8ad@ec2-54-246-87-132.eu-west-1.compute.amazonaws.com:5432/df47ikncj3r9tc'")
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