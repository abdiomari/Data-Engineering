from helper import get_connection

conn = get_connection()
cur = conn.cursor()

books =[
    ("The River and the Source", "Margaret Ogola", "Fiction", 2009 ),
    ("The River and the Sources", "Margaret Ogola 1", "Historical", 2010 ),
    ("The River and the Source 2", "Margaret Ogola 2", "Fiction", 2020 )
]

cur.executemany(
'''
INSERT INTO books (title, author,genre,year_published)
values(%s, %s, %s, %s)
''', 
books
)

conn.commit()
cur.close()
conn.close()
