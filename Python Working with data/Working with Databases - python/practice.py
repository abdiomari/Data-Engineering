from db_config import get_connection

sql = '''
    create table towns(
    name varchar(100) not null,
    population int
    )
'''

with get_connection() as conn:
    with conn.cursor() as cur:
        cur.execute(sql)
        print("Table 'towns' created successfully.")