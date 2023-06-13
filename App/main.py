import psycopg2

conn = psycopg2.connect("dbname=kms user=postgres password=aldim host=db")
cur = conn.cursor()
# cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (55, "Aldi Ganteng"))
cur.execute("SELECT * FROM test;")
a = cur.fetchall()
conn.commit()
cur.close()
conn.close()
print(a)