from sqlite3 import Cursor
import psycopg2

def read_db_entries(cur: Cursor, limit):
    cur.execute("SELECT * FROM actor ORDER BY first_name DESC;")
    lines = cur.fetchmany(limit)
    for line in lines:
        print(line)

def insert_actor(cur: Cursor,  firstName, lastName):
    cur.execute("INSERT INTO actor (first_name, last_name) VALUES (%s, %s)", (firstName, lastName))


conn = psycopg2.connect("dbname=dvdrental user=postgres password=postgrespw")
with conn:
    with conn.cursor() as cur:
        read_db_entries(cur, 15)
        insert_actor(cur, "Vin", "Diesel")
        read_db_entries(cur, 15)
        conn.commit()



