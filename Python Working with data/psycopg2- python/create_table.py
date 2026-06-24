from helper import get_connection

conn = get_connection()
cur = conn.cursor()
cur.execute(
    '''create table if not exists books (
        id serial primary key,
        title varchar(100), 
        author varchar(100),
        genre varchar(50),
        year_published int
        )
    ''')

conn.commit()
print("Table created successfully")

cur.close()
conn.close()