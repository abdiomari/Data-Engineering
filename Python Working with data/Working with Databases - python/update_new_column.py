from db_config import get_connection

sql = '''
    Update towns
    set county = %s
    where name = %s
'''


with get_connection() as conn:
    with conn.cursor() as cur:
        cur.execute(sql, ("Kericho", "Kericho"))
        conn.commit()
        print("updated new column - county")

        cur.execute("select * from towns;")
        rows = cur.fetchall()
        for row in rows:
            print(row)