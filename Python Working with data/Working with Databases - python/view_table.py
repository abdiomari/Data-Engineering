from db_config import get_connection

sql = '''
    select * from towns
    order by population desc;
'''

with get_connection() as conn:
    with conn.cursor() as cur:
        cur.execute(sql )
        rows = cur.fetchall()
        for row in rows:
            print(row)