from db_config import get_connection

sql = '''
    ALTER table towns
    add column county varchar(100);
'''


with get_connection() as conn:
    with conn.cursor() as cur:
        cur.execute(sql )
        conn.commit()
        print("added new column - county")

        cur.execute("select * from towns;")
        rows = cur.fetchall()
        for row in rows:
            print(row)