from db_config import get_connection

sql = '''
    insert into towns(name, population)
    values(%s, %s)
'''

towns = [
    ('Nairobi', 2000000),
    ('Kikuyu', 200000),
    ('Kericho', 400000)
]

with get_connection() as conn:
    with conn.cursor() as cur:
        cur.executemany(sql,towns )
        conn.commit()
        print("added new town")

        cur.execute("select * from towns;")
        rows = cur.fetchall()
        for row in rows:
            print(row)
